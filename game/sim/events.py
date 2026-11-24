"""Locations, presence and the event picker (CLAUDE.md §5).

Event specs are plain dicts defined in game/data/events.rpy:

    {
        "id": "grace_day04_council",      # unique
        "label": "grace_day04_council",   # Ren'Py label to call
        "kind": "story",                  # story | group | favor | bonus | hangout
        "location": "council_office",
        "chars": ["grace"],               # all must be present
        "slots": ["afternoon"],           # optional, default any
        "day_min": 4, "day_max": 30,      # optional
        "min_affection": {"grace": 25},   # optional
        "max_affection": {"grace": 89},   # optional
        "requires_flags": [...],          # optional
        "forbids_flags": [...],           # optional
        "favor_status": {"grace": "active"},  # optional
        "favor_step": {"grace": 0},       # optional: exact step of an active favor
        "once": True,                     # default True except hangouts
        "daily": True,                    # default True for hangouts: once per day per daily_key
        "daily_key": "hangout_grace",     # default: "hangout_<first char>" for hangouts, else id
        "forced": True,                   # plays at the start of the slot, no map (location ignored)
        "priority": 0,                    # optional tie-breaker within a kind
    }
"""

from .rules import SLOTS
from .state import GameState, evolve

KIND_PRIORITY = {"story": 4, "group": 4, "favor": 3, "bonus": 2, "hangout": 1}


def present(locations: dict, location_id: str, state: GameState) -> list:
    """Characters at a location in the current slot."""
    sched = locations[location_id].get("schedule", {})
    return list(sched.get(SLOTS[state.slot], ()))


def is_open(locations: dict, location_id: str, state: GameState) -> bool:
    slots = locations[location_id].get("open", SLOTS)
    return SLOTS[state.slot] in slots


def is_once(event: dict) -> bool:
    return event.get("once", event["kind"] != "hangout")


def is_daily(event: dict) -> bool:
    return event.get("daily", event["kind"] == "hangout")


def daily_key(event: dict) -> str:
    if "daily_key" in event:
        return event["daily_key"]
    if event["kind"] == "hangout" and event.get("chars"):
        return "hangout_" + event["chars"][0]
    return event["id"]


def _common_ok(event: dict, state: GameState) -> bool:
    if is_once(event) and event["id"] in state.seen_events:
        return False
    if is_daily(event) and daily_key(event) in state.seen_today:
        return False
    if "slots" in event and SLOTS[state.slot] not in event["slots"]:
        return False
    if not event.get("day_min", 1) <= state.day <= event.get("day_max", 10**9):
        return False
    for cid, n in event.get("min_affection", {}).items():
        if state.chars[cid].affection < n:
            return False
    for cid, n in event.get("max_affection", {}).items():
        if state.chars[cid].affection > n:
            return False
    if any(f not in state.flags for f in event.get("requires_flags", ())):
        return False
    if any(f in state.flags for f in event.get("forbids_flags", ())):
        return False
    for cid, status in event.get("favor_status", {}).items():
        if state.chars[cid].favor_status != status:
            return False
    for cid, step in event.get("favor_step", {}).items():
        c = state.chars[cid]
        if c.favor_status != "active" or c.favor_step != step:
            return False
    return True


def eligible(event: dict, state: GameState, location_id: str, here: list) -> bool:
    if event.get("forced") or event.get("location") != location_id:
        return False
    if any(c not in here for c in event.get("chars", ())):
        return False
    return _common_ok(event, state)


def pick_forced(events: list, state: GameState) -> dict | None:
    """A scripted event that plays at the start of this slot, before the map."""
    candidates = [e for e in events if e.get("forced") and _common_ok(e, state)]
    if not candidates:
        return None
    return max(candidates, key=lambda e: (KIND_PRIORITY[e["kind"]], e.get("priority", 0)))


def pick_event(events: list, state: GameState, locations: dict, location_id: str) -> dict | None:
    """Highest-priority eligible event: story/group > favor > bonus > hangout."""
    here = present(locations, location_id, state)
    candidates = [e for e in events if eligible(e, state, location_id, here)]
    if not candidates:
        return None
    return max(candidates, key=lambda e: (KIND_PRIORITY[e["kind"]], e.get("priority", 0)))


def mark_seen(state: GameState, event) -> GameState:
    """Record an event as seen (pass the event dict; a bare id also works)."""
    s = evolve(state)
    if isinstance(event, str):
        s.seen_events.add(event)
        return s
    s.seen_events.add(event["id"])
    if is_daily(event):
        s.seen_today.add(daily_key(event))
    return s


def validate_events(events: list, locations: dict, cast: dict) -> list:
    """Return a list of data problems (empty if valid)."""
    problems, ids = [], set()
    for e in events:
        eid = e.get("id", "?")
        if eid in ids:
            problems.append(f"duplicate event id {eid}")
        ids.add(eid)
        if e.get("kind") not in KIND_PRIORITY:
            problems.append(f"{eid}: unknown kind {e.get('kind')!r}")
        if not e.get("forced") and e.get("location") not in locations:
            problems.append(f"{eid}: unknown location {e.get('location')!r}")
        for cid in e.get("chars", ()):
            if cid not in cast:
                problems.append(f"{eid}: unknown character {cid!r}")
        for s in e.get("slots", ()):
            if s not in SLOTS:
                problems.append(f"{eid}: unknown slot {s!r}")
    return problems
