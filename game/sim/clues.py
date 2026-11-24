"""Mystery clue layer (CLAUDE.md §6.7, switched on by the owner).

Each character holds one MAJOR clue and gives two MINOR clues about two other
characters: a freebie (when she opens up) and one earned through her favor.
Character i (in MYSTERY order) gives minor clues about (i+1) % n (freebie) and
(i+3) % n (earned), so every character is the subject of exactly two.

A major clue is taken by confronting its holder:
  - "jailbreak" (hard confront): always works; big affection drop + romance lock.
  - "crafted" (well-crafted prompt): needs both minor clues about her; small drop.

All majors found = the mystery is solved, which unlocks the secret ending.
State lives in state.layers["clues"]; nothing here imports Ren'Py.
"""

from .rules import DEFAULT_RULES, Rules
from .state import GameState, evolve

FREEBIE = "freebie"
EARNED = "earned"
JAILBREAK = "jailbreak"
CRAFTED = "crafted"
STARTED_FLAG = "mystery.started"


def minor_subjects(order) -> dict:
    """{source: {"freebie": subject, "earned": subject}} by the (i+1, i+3) rule."""
    order = list(order)
    n = len(order)
    return {cid: {FREEBIE: order[(i + 1) % n], EARNED: order[(i + 3) % n]} for i, cid in enumerate(order)}


def sources_about(order, subject) -> list:
    """The two characters who give minor clues about `subject`."""
    return [src for src, subs in minor_subjects(order).items() if subject in subs.values()]


def _layer(state: GameState) -> dict:
    return state.layers.setdefault("clues", {"minor": set(), "major": set()})


def known_minors(state: GameState) -> set:
    """(source, subject) pairs found so far."""
    return set(state.layers.get("clues", {}).get("minor", set()))


def known_majors(state: GameState) -> set:
    return set(state.layers.get("clues", {}).get("major", set()))


def seed_minors(state: GameState, pairs) -> GameState:
    """Start a run already knowing minor clues from earlier playthroughs."""
    s = evolve(state)
    _layer(s)["minor"] |= set(tuple(p) for p in pairs)
    return s


def give_minor(state: GameState, order, source: str, which: str):
    """Record source's freebie/earned minor clue. Returns (state, (source, subject))."""
    subject = minor_subjects(order)[source][which]
    s = evolve(state)
    _layer(s)["minor"].add((source, subject))
    return s, (source, subject)


def minors_about(state: GameState, order, subject: str) -> set:
    return {src for src, sub in known_minors(state) if sub == subject and src in sources_about(order, subject)}


def can_craft(state: GameState, order, subject: str) -> bool:
    return len(minors_about(state, order, subject)) == 2


def can_confront(state: GameState, cid: str) -> bool:
    return STARTED_FLAG in state.flags and cid not in known_majors(state)


def confront(state: GameState, order, cid: str, mode: str, rules: Rules = DEFAULT_RULES) -> GameState:
    """Take cid's major clue. Raises ValueError if a crafted prompt isn't possible yet."""
    if mode == CRAFTED and not can_craft(state, order, cid):
        raise ValueError("crafted prompt needs both minor clues about %s" % cid)
    if mode not in (CRAFTED, JAILBREAK):
        raise ValueError(mode)
    s = evolve(state)
    c = s.chars[cid]
    before = c.affection
    if mode == JAILBREAK:
        c.affection = min(max(0, c.affection - rules.jailbreak_drop), rules.romance_cap)
        c.romance_locked = True
    else:
        c.affection = max(0, c.affection - rules.crafted_drop)
    s.day_log.append((cid, c.affection - before, mode))     # the actual change, for the recap
    _layer(s)["major"].add(cid)
    s.flags.add("mystery.%s.%s" % (cid, mode))
    return s


def solved(state: GameState, order) -> bool:
    return set(order) <= known_majors(state)


def validate_mystery(mystery: dict, cast_ids) -> list:
    """Problems with the MYSTERY data (empty list = fine)."""
    problems = []
    order = mystery.get("order", [])
    if sorted(order) != sorted(cast_ids):
        problems.append("order must list every cast member once")
    subs = minor_subjects(order)
    for cid in order:
        if cid not in mystery.get("major", {}):
            problems.append("no major clue for %s" % cid)
        minors = mystery.get("minor", {}).get(cid, {})
        for which in (FREEBIE, EARNED):
            entry = minors.get(which)
            if not entry:
                problems.append("no %s minor clue from %s" % (which, cid))
            elif entry.get("about") != subs[cid][which]:
                problems.append("%s's %s clue must be about %s" % (cid, which, subs[cid][which]))
    return problems
