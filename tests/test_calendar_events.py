from sim import affection, calendar, events
from sim.rules import DEFAULT_RULES as R
from sim.state import set_flag


def test_slots_cycle_and_day_advances(gs):
    s = gs
    assert calendar.slot_name(s) == "morning"
    s = calendar.advance(s)
    assert calendar.slot_name(s) == "afternoon"
    s = calendar.advance(s)
    assert calendar.is_evening(s)
    s = affection.add_affection(s, "grace", 5)
    s = calendar.advance(s)
    assert (s.day, s.slot) == (2, 0)
    assert s.day_log == []          # recap cleared for the new day


def test_gala_day(gs):
    s = gs
    s.day = R.semester_days
    assert calendar.is_gala_day(s)


LOCS = {
    "lab": {"schedule": {"morning": ["gemma", "shen"], "afternoon": ["gemma"]}},
    "roof": {"schedule": {"evening": ["xenia"]}, "open": ["evening"]},
}

EVENTS = [
    {"id": "hang_gemma", "label": "x", "kind": "hangout", "location": "lab", "chars": ["gemma"]},
    {"id": "bonus_gemma", "label": "x", "kind": "bonus", "location": "lab", "chars": ["gemma"],
     "min_affection": {"gemma": 75}},
    {"id": "favor_gemma", "label": "x", "kind": "favor", "location": "lab", "chars": ["gemma"],
     "favor_status": {"gemma": "active"}},
    {"id": "story_lab", "label": "x", "kind": "group", "location": "lab", "chars": ["gemma", "shen"],
     "day_min": 2},
    {"id": "flagged", "label": "x", "kind": "story", "location": "lab", "chars": ["gemma"],
     "requires_flags": ["met_gemma"], "forbids_flags": ["called_bard"], "priority": -1},
]


def test_presence_by_slot(gs):
    assert events.present(LOCS, "lab", gs) == ["gemma", "shen"]
    assert events.present(LOCS, "roof", gs) == []
    assert not events.is_open(LOCS, "roof", gs)


def test_priority_order(gs):
    # Day 1: only the hangout is eligible.
    assert events.pick_event(EVENTS, gs, LOCS, "lab")["id"] == "hang_gemma"
    s = affection.add_affection(gs, "gemma", 70)
    assert events.pick_event(EVENTS, s, LOCS, "lab")["id"] == "bonus_gemma"
    s.chars["gemma"].favor_status = "active"
    assert events.pick_event(EVENTS, s, LOCS, "lab")["id"] == "favor_gemma"
    s.day = 2
    assert events.pick_event(EVENTS, s, LOCS, "lab")["id"] == "story_lab"


def test_group_needs_everyone_present(gs):
    s = calendar.advance(gs)          # afternoon: shen gone
    s.day = 2
    assert events.pick_event(EVENTS, s, LOCS, "lab")["id"] == "hang_gemma"


def test_once_events_and_repeatable_hangouts(gs):
    s = gs
    s.day = 2
    s = events.mark_seen(s, "story_lab")
    assert events.pick_event(EVENTS, s, LOCS, "lab")["id"] == "hang_gemma"
    s = events.mark_seen(s, "hang_gemma")
    assert events.pick_event(EVENTS, s, LOCS, "lab")["id"] == "hang_gemma"


def test_flag_requirements(gs):
    s = set_flag(gs, "met_gemma")
    assert events.pick_event(EVENTS, s, LOCS, "lab")["id"] == "flagged"
    s = set_flag(s, "called_bard")
    assert events.pick_event(EVENTS, s, LOCS, "lab")["id"] == "hang_gemma"


def test_nothing_here(gs):
    assert events.pick_event(EVENTS, gs, LOCS, "roof") is None


def test_real_data_is_valid(data):
    assert events.validate_events(data["EVENTS"], data["LOCATIONS"], data["CAST"]) == []
    for lid, loc in data["LOCATIONS"].items():
        for slot, who in loc.get("schedule", {}).items():
            assert slot in ("morning", "afternoon", "evening"), lid
            for cid in who:
                assert cid in data["CAST"], (lid, cid)


def test_every_character_has_a_hangout_somewhere(data):
    hangout_chars = {c for e in data["EVENTS"] if e["kind"] == "hangout" for c in e["chars"]}
    assert hangout_chars == set(data["CAST"])
