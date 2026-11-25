#!/usr/bin/env python3
"""Pacing simulation for the redesign (CLAUDE.md §8 R1).

Plays whole semesters with a scripted player against the real rules
(game/sim), the real schedule and event registry (game/data), and an
approximation of each scene's effect:

  hangout / opens up / favor offer : one dialogue choice
  favor step                        : advances the favor; the last one pays
  pair scene                        : rules.pair_gain for both girls + their hints
  ask for a major clue              : crafted only (this player never jailbreaks)
  night date                        : quiz; a known fact is answered right,
                                      an unknown one is a 1-in-3 guess

Players:
  perfect  - best-style choices, plans around meetups, buys loved gifts
  good     - best-style choices about two thirds of the time
  casual   - picks a random style; visits whoever is around

Usage:  .venv/bin/python scripts/pacing_sim.py [--runs N] [--player perfect|good|casual|all]
"""

import argparse
import os
import random
import re
import statistics
import sys
import textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "game"))

from sim import affection, calendar, clues, events, favors, gifts, romance  # noqa: E402
from sim.endings import TELL, evaluate_ending  # noqa: E402
from sim.rules import DEFAULT_RULES, NIGHT, SLOTS  # noqa: E402
from sim.state import evolve, new_game  # noqa: E402

DATA_FILES = ["data/cast.rpy", "data/locations.rpy", "data/events.rpy", "data/gifts.rpy", "data/mystery.rpy"]


def load_data():
    ns = {}
    for rel in DATA_FILES:
        text = open(os.path.join(ROOT, "game", rel), encoding="utf-8").read()
        for m in re.finditer(r"^init[^\n]*python[^\n]*:\n((?:[ \t]+[^\n]*\n|\n)+)", text, re.M):
            exec(textwrap.dedent(m.group(1)), ns)
    return ns


D = load_data()
CAST, LOCS, EVENTS, SHOP, MYSTERY = D["CAST"], D["LOCATIONS"], D["EVENTS"], D["SHOP"], D["MYSTERY"]
IDS = list(CAST)


class Player:
    def __init__(self, kind, rng, rules):
        self.kind, self.rng, self.rules = kind, rng, rules

    def skill(self):
        return {"perfect": 1.0, "good": 0.67, "casual": 0.0}[self.kind]

    def choice(self, s, cid, base=4):
        if self.rng.random() < self.skill():
            aff = max(CAST[cid]["affinities"].values() or [0])
            style = next((k for k, v in CAST[cid]["affinities"].items() if v == aff), None)
        else:
            style = self.rng.choice([None, "structured", "honest", "irreverent", "concise",
                                     "curious", "warm", "practical", "pry"])
        return affection.apply_choice(s, CAST, cid, base, style, self.rules)


def meet_everyone(s):
    s = evolve(s)
    s.flags |= {f"met_{c}" for c in IDS} | {clues.STARTED_FLAG}
    return s


def visit_options(s, p):
    """(score, location, focus, event) for every useful thing to do this slot."""
    opts = []
    for lid, loc in LOCS.items():
        if loc.get("kind") == "shop" or not events.is_open(LOCS, lid, s):
            continue
        here = events.present(LOCS, lid, s)
        pair = events.pick_event(EVENTS, s, LOCS, lid)
        if pair and pair["kind"] == "pair":
            # A careful player takes a pair scene now only if it won't come round again.
            m = events.meetup_here(LOCS, lid, s)
            later = [d for loc in LOCS.values() for mm in loc.get("meetups", ())
                     if mm["chars"] == m and mm["slot"] == SLOTS[s.slot] for d in mm["days"] if d > s.day]
            opts.append((10 if not later or p.kind != "perfect" else 6.5, lid, None, pair))
            continue
        for who in here or [None]:
            ev = events.pick_event(EVENTS, s, LOCS, lid, focus=who)
            if who and clues.can_confront(s, who) and clues.can_craft(s, MYSTERY, who) \
                    and s.chars[who].stage != "none":
                opts.append((7, lid, who, {"kind": "confront", "id": "confront_" + who}))
            if ev is None:
                continue
            score = {"favor": 9, "story": 8, "group": 8, "hangout": 3}.get(ev["kind"], 1)
            if ev["kind"] == "favor":
                left = favors.days_left(s, ev["route"]) or 0
                score += (2.5 if left <= 1 else 1) - left / 10            # most urgent first
            active = sum(1 for c in s.chars.values() if c.favor_status == "active")
            if ev["id"].endswith("_opens_up") and active >= 2:
                score = 4                                                 # don't juggle 3 favors
            if who and ev["kind"] == "hangout":
                c = s.chars[who]
                if c.stage == "none" and c.affection < DEFAULT_RULES.date_at:
                    score += 2 + (c.affection / 100)
                if romance.can_become_lover(s, CAST, who):
                    score += 5
            opts.append((score, lid, who, ev))
    return opts


def play_event(p, s, ev, who):
    r = p.rules
    kind = ev["kind"]
    if kind == "confront":
        return clues.confront(s, MYSTERY, who, clues.CRAFTED, r)
    s = events.mark_seen(s, ev)
    if kind == "pair":
        a, b = ev["chars"]
        for c in (a, b):
            s = affection.add_affection(s, c, affection.scale_gain(r.pair_gain, CAST[c]["difficulty"]), "pair", r)
        s, _ = clues.give_pair_hints(s, MYSTERY, ev["pair"])
        for c in (a, b):
            s, _ = romance.learn_fact(s, c)     # you learn something about each of them
        return s
    route = ev.get("route")
    if kind == "hangout":
        s = p.choice(s, route)
        s, _ = romance.learn_fact(s, route)
    elif ev["id"].endswith("_opens_up"):
        s = p.choice(s, route)
        s = evolve(s)
        s.flags.add(f"{route}.opened_up")
        s.chars[route].known.add("likes")
        s = p.choice(s, route, base=2)          # she asks her favor in the same scene
        s = favors.offer(s, route)
    elif kind == "favor":
        steps = CAST[route]["favor"]["steps"]
        if route in ev.get("chars", ()):
            s = p.choice(s, route)              # a step spent with her is time together too
        s = favors.advance_step(s, route, steps, r)
        if s.chars[route].favor_status == "done":
            s = affection.add_affection(s, route, affection.scale_gain(r.favor_done_bonus, CAST[route]["difficulty"]), "favor_done", r)
            s, _ = romance.learn_fact(s, route)
    return s


def shop_and_give(p, s, who):
    """Free actions on a visit: buy what's needed, give a gift."""
    r = p.rules
    # Buy special gifts for girlfriends first.
    for c in IDS:
        g = CAST[c]["special_gift"]
        if s.chars[c].stage == "girlfriend" and not s.inventory.get(g) and s.money >= SHOP[g]["price"]:
            s = gifts.buy(s, SHOP, g)
    if who is None:
        return s
    if romance.can_become_lover(s, CAST, who):
        return romance.give_special(s, CAST, who)
    # Perfect players spend spare money (beyond a reserve) on loved gifts for the girl they're seeing.
    if p.kind == "perfect" and s.chars[who].stage == "none" and s.chars[who].last_gift_day != s.day:
        reserve = SHOP[CAST[who]["special_gift"]]["price"]
        for g in CAST[who]["gifts"]["loved"]:
            if s.money - SHOP[g]["price"] >= reserve:
                s = gifts.buy(s, SHOP, g)
                s = gifts.give(s, CAST, who, g, r)
                break
    return s


def night(p, s):
    r = p.rules
    cands = romance.date_candidates(s, IDS, r)
    if not cands:
        return s
    who = max(cands, key=lambda c: (len(s.chars[c].known), s.chars[c].affection))
    quiz = romance.build_quiz(CAST, who, who, s.chars[who].known, seed=s.day, rules=r)
    correct = sum(1 if q["key"] in s.chars[who].known else (p.rng.random() < 1 / 3) for q in quiz)
    s, _ = romance.resolve_date(s, CAST, who, correct, r)
    return s


def run(kind, seed, rules=DEFAULT_RULES, log=False):
    rng = random.Random(seed)
    p = Player(kind, rng, rules)
    s = meet_everyone(new_game(IDS, rules))
    timeline = {}
    while not calendar.is_gala_day(s, rules):
        scripted = s.day == 1 or (s.day == 3 and s.slot == 0)
        if s.slot == NIGHT:
            s = night(p, s)
        elif not scripted:
            opts = visit_options(s, p)
            if opts:
                if kind == "casual":
                    _, lid, who, ev = rng.choice(opts)
                else:
                    best = max(o[0] for o in opts)
                    _, lid, who, ev = rng.choice([o for o in opts if o[0] == best])
                s = shop_and_give(p, s, who)
                s = play_event(p, s, ev, who)
                if log:
                    print(f"d{s.day} {SLOTS[s.slot]:9} {lid:16} {who or '-':8} {ev['id']}")
        if clues.solved(s, MYSTERY) and clues.TRUTH_FLAG not in s.flags:
            s = evolve(s)
            s.flags.add(clues.TRUTH_FLAG)
        if calendar.is_last_slot(s):
            timeline[s.day] = (len(romance.girlfriends(s, IDS)) + len(romance.lovers(s, IDS)),
                               len(romance.lovers(s, IDS)), len(clues.known_majors(s)))
        s = calendar.advance(s, rules)
    return s, timeline


def summarize(kind, runs, rules=DEFAULT_RULES):
    finals, endings, truth_days, all_lover_days = [], {}, [], []
    stage_by_day = {}
    for i in range(runs):
        s, tl = run(kind, i, rules)
        lv = len(romance.lovers(s, IDS))
        finals.append((lv, len(clues.known_majors(s)), s.money))
        e = evaluate_ending(s, TELL, IDS, rules)
        endings[e] = endings.get(e, 0) + 1
        for d, v in tl.items():
            stage_by_day.setdefault(d, []).append(v)
        tdays = [d for d, v in tl.items() if v[2] == len(IDS)]
        if tdays:
            truth_days.append(min(tdays))
        ldays = [d for d, v in tl.items() if v[1] == len(IDS)]
        if ldays:
            all_lover_days.append(min(ldays))
    print(f"\n=== {kind} player, {runs} runs ===")
    print("day  dating+  lovers  majors   (averages at end of day)")
    for d in sorted(stage_by_day):
        vals = stage_by_day[d]
        print(f"{d:>3}  {statistics.mean(v[0] for v in vals):6.1f}  {statistics.mean(v[1] for v in vals):6.1f}  "
              f"{statistics.mean(v[2] for v in vals):6.1f}")
    print(f"lovers at gala: mean {statistics.mean(f[0] for f in finals):.1f}, "
          f"min {min(f[0] for f in finals)}, max {max(f[0] for f in finals)}")
    print(f"majors at gala: mean {statistics.mean(f[1] for f in finals):.1f}")
    print(f"truth found in {len(truth_days)}/{runs} runs" +
          (f", earliest day {min(truth_days)}" if truth_days else ""))
    print(f"all 7 lovers in {len(all_lover_days)}/{runs} runs" +
          (f", earliest day {min(all_lover_days)}" if all_lover_days else ""))
    print("endings if you tell:", dict(sorted(endings.items(), key=lambda kv: -kv[1])))
    print(f"money left: mean {statistics.mean(f[2] for f in finals):.0f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", type=int, default=200)
    ap.add_argument("--player", default="all")
    ap.add_argument("--log", action="store_true", help="print one perfect run slot by slot")
    a = ap.parse_args()
    if a.log:
        run("perfect", 0, log=True)
        return
    budget = calendar.playable_slots()
    print(f"Semester: {DEFAULT_RULES.semester_days} days, {budget['day']} day slots, {budget['night']} nights "
          f"(minus day 1 and day 3 morning, which are scripted)")
    for kind in (["perfect", "good", "casual"] if a.player == "all" else [a.player]):
        summarize(kind, a.runs)


if __name__ == "__main__":
    main()
