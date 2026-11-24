"""One test per row of the endings table (CLAUDE.md §7), plus boundaries."""

import pytest

from sim.endings import RIVALS, RIVALS_EVENT_FLAG, SOLO, all_ending_ids, evaluate_ending


def setup(gs, **affections):
    for cid, a in affections.items():
        gs.chars[cid].affection = a
    return gs


# Row: Good ending
def test_good(gs):
    s = setup(gs, grace=92)
    s.chars["grace"].favor_status = "done"
    assert evaluate_ending(s, "grace") == "good_grace"


def test_good_needs_favor_done(gs):
    s = setup(gs, grace=95)
    s.chars["grace"].favor_status = "failed"
    assert evaluate_ending(s, "grace") == "sweet_grace"


# Row: Sweet ending
@pytest.mark.parametrize("a", [60, 75, 89])
def test_sweet(gs, a):
    assert evaluate_ending(setup(gs, claudia=a), "claudia") == "sweet_claudia"


# Row: Friends ending
def test_friends_low_affection(gs):
    assert evaluate_ending(setup(gs, gemma=59), "gemma") == "friends_gemma"


def test_friends_when_locked(gs):
    s = setup(gs, gemma=60)
    s.chars["gemma"].romance_locked = True
    s.chars["gemma"].favor_status = "done"
    assert evaluate_ending(s, "gemma") == "friends_gemma"


# Row: Rivals (secret)
def test_rivals(gs):
    s = setup(gs, grace=75, shen=80)
    s.flags.add(RIVALS_EVENT_FLAG)
    assert evaluate_ending(s, "grace") == RIVALS
    assert evaluate_ending(s, "shen") == RIVALS


def test_rivals_needs_joint_event(gs):
    s = setup(gs, grace=80, shen=80)
    assert evaluate_ending(s, "shen") == "sweet_shen"


def test_rivals_needs_both_75(gs):
    s = setup(gs, grace=74, shen=95)
    s.flags.add(RIVALS_EVENT_FLAG)
    assert evaluate_ending(s, "shen") == "sweet_shen"


def test_rivals_only_when_asking_one_of_them(gs):
    s = setup(gs, grace=80, shen=80, xenia=70)
    s.flags.add(RIVALS_EVENT_FLAG)
    assert evaluate_ending(s, "xenia") == "sweet_xenia"


# Row: Solo
def test_solo_asked_no_one(gs):
    assert evaluate_ending(setup(gs, grace=95), None) == SOLO


def test_solo_everyone_below_25(gs):
    s = setup(gs, grace=24, xenia=24, claudia=24, gemma=24, shen=24)
    assert evaluate_ending(s, "grace") == SOLO


def test_not_solo_if_anyone_reaches_25(gs):
    s = setup(gs, grace=10, xenia=25, claudia=10, gemma=10, shen=10)
    assert evaluate_ending(s, "grace") == "friends_grace"


def test_all_ending_ids(cast):
    ids = all_ending_ids(cast)
    assert len(ids) == 3 + 3 * len(cast)          # solo, rivals, truth + 3 per character
    assert "good_shen" in ids and SOLO in ids and RIVALS in ids
