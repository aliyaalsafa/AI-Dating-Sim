from sim import affection, calendar, events
from sim.rules import DEFAULT_RULES as R
from sim.state import set_flag


def next_day(s):
    for _ in range(len(calendar.SLOTS)):
        s = calendar.advance(s)
    return s


def test_slots_cycle_and_day_advances(gs):
    s = gs
    assert calendar.slot_name(s) == "morning"
    s = calendar.advance(s)
    assert calendar.slot_name(s) == "afternoon"
    s = calendar.advance(s)
    assert calendar.is_evening(s)
    s = calendar.advance(s)
    assert calendar.is_night(s) and calendar.is_last_slot(s)
    s = affection.add_affection(s, "grace", 5)
    s = calendar.advance(s)
    assert (s.day, s.slot) == (2, 0)
    assert s.day_log == []          # recap cleared for the new day


def test_gala_is_the_last_evening(gs):
    s = gs
    s.day = R.semester_days
    s.slot = 1
    assert not calendar.is_gala_day(s)          # last day's afternoon is still playable
    s = calendar.advance(s)
    assert calendar.is_gala_day(s)              # its evening is the gala


def test_semester_slot_count():
    """14 days: 3 map slots + a date night each; the gala takes day 14's evening."""
    assert R.semester_days == 14
    assert calendar.playable_slots() == {"day": 41, "night": 13}


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
            assert slot in ("morning", "afternoon", "evening"), lid   # nights are dates only
            for cid in who:
                assert cid in data["CAST"], (lid, cid)


def test_every_character_has_a_hangout_somewhere(data):
    hangout_chars = {c for e in data["EVENTS"] if e["kind"] == "hangout" for c in e["chars"]}
    assert hangout_chars == set(data["CAST"])


# --- M2: daily limits, forced events, favor steps -------------------------

def test_hangouts_once_per_day_per_character(gs):
    s = gs
    ev = events.pick_event(EVENTS, s, LOCS, "lab")
    assert ev["id"] == "hang_gemma"
    s = events.mark_seen(s, ev)
    assert events.pick_event(EVENTS, s, LOCS, "lab") is None      # same day: no repeat
    s = next_day(s)   # next morning
    assert events.pick_event(EVENTS, s, LOCS, "lab")["id"] == "story_lab"


def test_daily_key_shared_across_locations(gs):
    evs = [
        {"id": "h1", "label": "x", "kind": "hangout", "location": "lab", "chars": ["gemma"]},
        {"id": "h2", "label": "x", "kind": "hangout", "location": "roof", "chars": ["gemma"]},
    ]
    locs = {"lab": {"schedule": {"morning": ["gemma"]}}, "roof": {"schedule": {"morning": ["gemma"]}}}
    s = events.mark_seen(gs, evs[0])
    assert events.pick_event(evs, s, locs, "roof") is None


FORCED = [
    {"id": "prologue", "label": "x", "kind": "story", "forced": True, "day_max": 1, "slots": ["morning"]},
    {"id": "lunch", "label": "x", "kind": "group", "forced": True, "day_max": 1, "slots": ["afternoon"]},
    {"id": "loc_event", "label": "x", "kind": "story", "location": "lab", "chars": ["gemma"]},
]


def test_forced_events_play_by_schedule(gs):
    assert events.pick_forced(FORCED, gs)["id"] == "prologue"
    s = events.mark_seen(gs, events.pick_forced(FORCED, gs))
    assert events.pick_forced(FORCED, s) is None                  # once
    s = calendar.advance(s)
    assert events.pick_forced(FORCED, s)["id"] == "lunch"
    s.day = 2
    assert events.pick_forced(FORCED, s) is None


def test_forced_events_never_picked_from_map(gs):
    assert events.pick_event(FORCED, gs, LOCS, "lab")["id"] == "loc_event"


def test_favor_step_requirement(gs):
    from sim import favors
    evs = [
        {"id": "step0", "label": "x", "kind": "favor", "location": "lab", "chars": ["gemma"],
         "favor_step": {"gemma": 0}, "once": False},
        {"id": "step1", "label": "x", "kind": "favor", "location": "lab", "chars": ["gemma"],
         "favor_step": {"gemma": 1}, "once": False},
    ]
    assert events.pick_event(evs, gs, LOCS, "lab") is None         # favor not active
    s = favors.offer(gs, "gemma")
    assert events.pick_event(evs, s, LOCS, "lab")["id"] == "step0"
    s = favors.advance_step(s, "gemma", 2)
    assert events.pick_event(evs, s, LOCS, "lab")["id"] == "step1"
    s = favors.advance_step(s, "gemma", 2)
    assert events.pick_event(evs, s, LOCS, "lab") is None         # done


def test_counters(gs):
    from sim.state import count, incr
    s = incr(incr(gs, "grace.hangouts"), "grace.hangouts")
    assert count(s, "grace.hangouts") == 2 and count(gs, "grace.hangouts") == 0


def test_days_1_to_3_introduce_everyone(data):
    """Forced scenes on days 1-3 must meet all five characters (M2 requirement)."""
    met = set()
    for e in data["EVENTS"]:
        if e.get("forced") and e.get("day_max", 99) <= 3:
            met |= set(e.get("introduces", ()))
    assert met == set(data["CAST"])


MEET = {
    "lab": {"schedule": {"afternoon": ["gemma"]},
            "meetups": [{"chars": ["gemma", "kimi"], "slot": "afternoon", "days": [3]}]},
    "hall": {"schedule": {"afternoon": ["kimi"]}},
}


def test_meetups_pull_both_girls_together(gs):
    s = calendar.advance(gs)                       # day 1 afternoon: no meetup
    assert events.present(MEET, "lab", s) == ["gemma"]
    assert events.present(MEET, "hall", s) == ["kimi"]
    s.day = 3
    assert events.present(MEET, "lab", s) == ["gemma", "kimi"]
    assert events.present(MEET, "hall", s) == []
    assert events.meetup_here(MEET, "lab", s) == ["gemma", "kimi"]


def test_focus_limits_the_pick(gs):
    evs = [
        {"id": "h_gemma", "label": "x", "kind": "hangout", "location": "lab", "chars": ["gemma"]},
        {"id": "h_kimi", "label": "x", "kind": "hangout", "location": "lab", "chars": ["kimi"]},
    ]
    s = calendar.advance(gs)
    s.day = 3
    assert events.pick_event(evs, s, MEET, "lab", focus="kimi")["id"] == "h_kimi"
    assert events.pick_event(evs, s, MEET, "lab", focus="gemma")["id"] == "h_gemma"


def test_schedule_validation_catches_double_booking(cast):
    locs = {"a": {"schedule": {"morning": ["grace"]}}, "b": {"schedule": {"morning": ["grace"]}}}
    assert events.validate_schedule(locs, cast)
