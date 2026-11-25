"""Mystery: pair-scene hints and major clues (game/sim/clues.py, CLAUDE.md §6.5)."""

import pytest

from sim import clues
from sim.rules import DEFAULT_RULES as R


@pytest.fixture
def mystery(data):
    return data["MYSTERY"]


def started(gs):
    gs.flags.add(clues.STARTED_FLAG)
    return gs


def test_data_is_valid(mystery, cast):
    assert clues.validate_mystery(mystery, cast.keys()) == []


def test_every_girl_is_in_two_pair_scenes(mystery):
    for cid in mystery["order"]:
        assert len(clues.pairs_about(mystery, cid)) == 2, cid


def test_pair_scene_gives_a_hint_about_each_girl(gs, mystery):
    s, new = clues.give_pair_hints(gs, mystery, "grace_claudia")
    assert set(new) == {("grace_claudia", "grace"), ("grace_claudia", "claudia")}
    s, again = clues.give_pair_hints(s, mystery, "grace_claudia")
    assert again == []


def test_crafted_needs_both_hints(gs, mystery):
    s = started(gs)
    assert not clues.can_craft(s, mystery, "grace")
    s, _ = clues.give_pair_hints(s, mystery, "grace_claudia")
    assert not clues.can_craft(s, mystery, "grace")
    with pytest.raises(ValueError):
        clues.confront(s, mystery, "grace", clues.CRAFTED)
    s, _ = clues.give_pair_hints(s, mystery, "grace_shen")
    assert clues.can_craft(s, mystery, "grace")
    before = s.chars["grace"].affection
    s = clues.confront(s, mystery, "grace", clues.CRAFTED)
    assert s.chars["grace"].affection == before - R.crafted_drop
    assert not s.chars["grace"].romance_locked
    assert "grace" in clues.known_majors(s)
    assert not clues.can_confront(s, "grace")


def test_jailbreak_always_works_and_locks(gs, mystery):
    s = started(gs)
    s.chars["xenia"].affection = 80
    s = clues.confront(s, mystery, "xenia", clues.JAILBREAK)
    c = s.chars["xenia"]
    assert c.romance_locked
    assert c.affection == min(80 - R.jailbreak_drop, R.romance_cap)
    assert s.day_log[-1] == ("xenia", c.affection - 80, clues.JAILBREAK)


def test_cannot_ask_before_the_mystery_starts(gs):
    assert not clues.can_confront(gs, "grace")


def test_solved_needs_every_major(gs, mystery):
    s = started(gs)
    for cid in mystery["order"][:-1]:
        s = clues.confront(s, mystery, cid, clues.JAILBREAK)
    assert not clues.solved(s, mystery)
    s = clues.confront(s, mystery, mystery["order"][-1], clues.JAILBREAK)
    assert clues.solved(s, mystery)


def test_seeded_hints_carry_over(gs, mystery):
    s = clues.seed_minors(gs, [("grace_claudia", "grace"), ("grace_shen", "grace")])
    assert clues.can_craft(s, mystery, "grace")


def test_validate_catches_a_girl_in_one_pair(mystery, cast):
    broken = dict(mystery, pairs=[p for p in mystery["pairs"] if p["id"] != "lola_shen"])
    problems = clues.validate_mystery(broken, cast.keys())
    assert any("lola" in p for p in problems) and any("shen" in p for p in problems)
