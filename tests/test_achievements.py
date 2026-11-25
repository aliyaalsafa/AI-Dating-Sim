"""State-derived achievements (game/sim/achievements.py)."""

from sim.achievements import earned, endings_progress
from sim.endings import all_ending_ids
from sim.state import evolve


def test_fresh_game_earns_nothing(gs, cast):
    assert earned(gs, cast.keys()) == set()


def test_no_state_still_counts_endings(cast):
    assert earned(None, cast.keys(), {"unfinished"}) == {"first_ending", "unfinished_ending"}


def test_all_met_needs_everyone(gs, cast):
    s = evolve(gs)
    s.flags |= {"met_" + c for c in list(cast)[:-1]}
    assert "all_met" not in earned(s, cast.keys())
    s.flags.add("met_" + list(cast)[-1])
    assert "all_met" in earned(s, cast.keys())


def test_opened_up_and_open_book(gs, cast):
    s = evolve(gs)
    s.flags.add("grace.opened_up")
    got = earned(s, cast.keys())
    assert "opened_up" in got and "open_book" not in got
    s.flags |= {c + ".opened_up" for c in cast}
    assert "open_book" in earned(s, cast.keys())


def test_favors(gs, cast):
    s = evolve(gs)
    s.chars["gemma"].favor_status = "done"
    got = earned(s, cast.keys())
    assert "first_favor" in got and "all_favors" not in got
    for c in s.chars.values():
        c.favor_status = "done"
    assert "all_favors" in earned(s, cast.keys())


def test_stages_truth_and_bad_news(gs, cast):
    s = evolve(gs)
    s.chars["shen"].stage = "girlfriend"
    got = earned(s, cast.keys())
    assert "first_girlfriend" in got and "first_lover" not in got
    s.chars["xenia"].stage = "lover"
    s.chars["claudia"].dealbreaker_hits = 1
    s.chars["gemma"].romance_locked = True
    s.flags.add("truth.known")
    assert {"first_girlfriend", "first_lover", "hit_a_nerve", "friend_zoned", "truth_known"} <= earned(s, cast.keys())


def test_ending_achievements(cast):
    got = earned(None, cast.keys(), {"mono_grace", "lie"})
    assert {"first_ending", "lie_ending"} <= got
    assert "all_mono" not in got and "completionist" not in got
    assert "all_mono" in earned(None, cast.keys(), {"mono_" + c for c in cast})
    assert "complete_ending" in earned(None, cast.keys(), {"complete"})
    assert "exiled_ending" in earned(None, cast.keys(), {"exiled"})
    assert "completionist" in earned(None, cast.keys(), set(all_ending_ids(cast.keys())))


def test_endings_progress_ignores_unknown_ids(cast):
    seen, total = endings_progress(cast.keys(), {"unfinished", "mono_grace", "not_an_ending"})
    assert (seen, total) == (2, 16)


def test_every_earnable_id_is_registered(data, gs, cast):
    s = evolve(gs)
    for c in cast:
        s.flags |= {"met_" + c, c + ".opened_up"}
        s.chars[c].favor_status = "done"
        s.chars[c].stage = "lover"
        s.chars[c].dealbreaker_hits = 2
        s.chars[c].romance_locked = True
        s.flags |= {"mystery.%s.jailbreak" % c, "mystery.%s.crafted" % c}
    s.layers["clues"] = {"minor": {("grace_shen", "grace")}, "major": set(cast)}
    s.flags.add("truth.known")
    ids = earned(s, cast.keys(), set(all_ending_ids(cast.keys())))
    assert ids <= set(data["ACHIEVEMENTS"])
    assert len(ids) == len(data["ACHIEVEMENTS"]) - 3   # first_day, first_gift, loved_gift are granted by scenes
