"""Mystery: the secret Turing test (CLAUDE.md §6.5, layer 1).

- Each main girl holds one MAJOR clue, taken by asking her alone:
    "crafted" (well-crafted ask): needs every hint about her; small affection cost.
    "jailbreak": always works; big affection drop and her romance locks.
- HINTS come from pair scenes: overhearing two girls together gives one hint
  about each of them. Data lives in MYSTERY["pairs"] (game/data/mystery.rpy).
- All majors found = the truth: the reveal scene plays and TRUTH_FLAG is set,
  which opens the gala's "tell them" choice.

State lives in state.layers["clues"]; nothing here imports Ren'Py.
"""

from .rules import DEFAULT_RULES, Rules
from .state import GameState, evolve

JAILBREAK = "jailbreak"
CRAFTED = "crafted"
STARTED_FLAG = "mystery.started"
TRUTH_FLAG = "truth.known"


def pairs(mystery: dict) -> list:
    return list(mystery.get("pairs", ()))


def pair_by_id(mystery: dict, pid: str) -> dict:
    return next(p for p in pairs(mystery) if p["id"] == pid)


def pairs_about(mystery: dict, subject: str) -> list:
    """Ids of the pair scenes that give a hint about `subject`."""
    return [p["id"] for p in pairs(mystery) if subject in p["chars"]]


def _layer(state: GameState) -> dict:
    return state.layers.setdefault("clues", {"minor": set(), "major": set()})


def known_minors(state: GameState) -> set:
    """(pair_id, subject) hints found so far."""
    return set(state.layers.get("clues", {}).get("minor", set()))


def known_majors(state: GameState) -> set:
    return set(state.layers.get("clues", {}).get("major", set()))


def seed_minors(state: GameState, hints) -> GameState:
    """Start a run already knowing hints from earlier playthroughs."""
    s = evolve(state)
    _layer(s)["minor"] |= set(tuple(h) for h in hints)
    return s


def give_pair_hints(state: GameState, mystery: dict, pid: str):
    """Record the pair scene's hints. Returns (state, [(pid, subject), ...] newly learned)."""
    p = pair_by_id(mystery, pid)
    s = evolve(state)
    layer = _layer(s)
    new = [(pid, c) for c in p["chars"] if (pid, c) not in layer["minor"]]
    layer["minor"] |= set(new)
    return s, new


def minors_about(state: GameState, mystery: dict, subject: str) -> set:
    valid = set(pairs_about(mystery, subject))
    return {pid for pid, sub in known_minors(state) if sub == subject and pid in valid}


def hints_needed(mystery: dict, subject: str) -> int:
    return len(pairs_about(mystery, subject))


def can_craft(state: GameState, mystery: dict, subject: str) -> bool:
    return len(minors_about(state, mystery, subject)) >= hints_needed(mystery, subject)


def can_confront(state: GameState, cid: str) -> bool:
    return STARTED_FLAG in state.flags and cid not in known_majors(state)


def confront(state: GameState, mystery: dict, cid: str, mode: str,
             rules: Rules = DEFAULT_RULES) -> GameState:
    """Take cid's major clue. Raises ValueError if a crafted ask isn't possible yet."""
    if mode not in (CRAFTED, JAILBREAK):
        raise ValueError(mode)
    if mode == CRAFTED and not can_craft(state, mystery, cid):
        raise ValueError("a well-crafted ask needs every hint about %s" % cid)
    s = evolve(state)
    c = s.chars[cid]
    before = c.affection
    if mode == JAILBREAK:
        c.affection = min(max(0, c.affection - rules.jailbreak_drop), rules.romance_cap)
        c.romance_locked = True
        s.flags.add(f"{cid}.romance_locked")
    else:
        c.affection = max(0, c.affection - rules.crafted_drop)
    s.day_log.append((cid, c.affection - before, mode))     # the actual change, for the recap
    _layer(s)["major"].add(cid)
    s.flags.add("mystery.%s.%s" % (cid, mode))
    return s


def solved(state: GameState, mystery: dict) -> bool:
    return set(mystery["order"]) <= known_majors(state)


def knows_truth(state: GameState) -> bool:
    return TRUTH_FLAG in state.flags


def validate_mystery(mystery: dict, cast_ids) -> list:
    """Problems with the MYSTERY data (empty list = fine)."""
    problems = []
    order = list(mystery.get("order", []))
    if sorted(order) != sorted(cast_ids):
        problems.append("order must list every main cast member once")
    ids = set()
    for p in pairs(mystery):
        pid = p.get("id", "?")
        if pid in ids:
            problems.append("duplicate pair %s" % pid)
        ids.add(pid)
        chars = p.get("chars", [])
        if len(chars) != 2 or chars[0] == chars[1] or any(c not in order for c in chars):
            problems.append("pair %s must name two different main girls" % pid)
            continue
        for c in chars:
            if not p.get("hints", {}).get(c):
                problems.append("pair %s has no hint about %s" % (pid, c))
    for cid in order:
        if cid not in mystery.get("major", {}):
            problems.append("no major clue for %s" % cid)
        n = hints_needed(mystery, cid)
        if n != 2:
            problems.append("%s is in %d pair scenes (should be 2)" % (cid, n))
    return problems
