"""One test per row of the endings table (CLAUDE.md §7), plus boundaries."""

import pytest

from sim.clues import TRUTH_FLAG
from sim.endings import (ADA_FLAG, BAD_TRUTH, COMPLETE, EXILED, GOOD_TRUTH, LIE, LIE_ADA, SILENT, TELL,
                         TRUE_FINAL, UNFINISHED, UNFINISHED_TWO, all_ending_ids, coda, evaluate_ending,
                         mono_id)
from sim.state import CharState

MAIN = ["grace", "xenia", "claudia", "gemma", "shen", "kimi", "lola"]


def setup(gs, n_lovers=0, truth=True, ada=False, ada_lover=False):
    for cid in MAIN[:n_lovers]:
        gs.chars[cid].stage = "lover"
    if truth:
        gs.flags.add(TRUTH_FLAG)
    if ada:
        gs.flags.add(ADA_FLAG)
        gs.chars["ada"] = CharState(stage="lover" if ada_lover else "none")
    return gs


# Row: Unfinished (never found the secret), whatever else is true
@pytest.mark.parametrize("choice", [TELL, SILENT, None])
def test_unfinished(gs, choice):
    assert evaluate_ending(setup(gs, 7, truth=False), choice, MAIN) == UNFINISHED


# Rows: The Lie, and The Lie with her
def test_lie(gs):
    assert evaluate_ending(setup(gs, 7), SILENT, MAIN) == LIE


def test_lie_ada(gs):
    assert evaluate_ending(setup(gs, 7, ada=True, ada_lover=True), SILENT, MAIN) == LIE_ADA


# Row: True Final
def test_true_final(gs):
    assert evaluate_ending(setup(gs, 7, ada=True, ada_lover=True), TELL, MAIN) == TRUE_FINAL


def test_true_final_needs_ada_as_lover(gs):
    assert evaluate_ending(setup(gs, 7, ada=True), TELL, MAIN) == COMPLETE


# Row: Complete
def test_complete(gs):
    assert evaluate_ending(setup(gs, 7), TELL, MAIN) == COMPLETE


# Rows: Good / Bad Truth, Monogamous, Exiled
@pytest.mark.parametrize("n", [4, 5, 6])
def test_good_truth(gs, n):
    assert evaluate_ending(setup(gs, n), TELL, MAIN) == GOOD_TRUTH


@pytest.mark.parametrize("n", [2, 3])
def test_bad_truth(gs, n):
    assert evaluate_ending(setup(gs, n), TELL, MAIN) == BAD_TRUTH


def test_monogamous_names_the_girl(gs):
    s = setup(gs, 0)
    s.chars["kimi"].stage = "lover"
    assert evaluate_ending(s, TELL, MAIN) == mono_id("kimi")


def test_exiled(gs):
    assert evaluate_ending(setup(gs, 0), TELL, MAIN) == EXILED


def test_girlfriends_dont_count(gs):
    s = setup(gs, 1)
    for cid in MAIN[1:]:
        s.chars[cid].stage = "girlfriend"
    assert evaluate_ending(s, TELL, MAIN) == mono_id("grace")


# Unfinished II follows a normal ending once Ada is unlocked
def test_coda(gs):
    s = setup(gs, 5, ada=True)
    assert coda(s, GOOD_TRUTH) == UNFINISHED_TWO
    assert coda(s, UNFINISHED) == UNFINISHED_TWO
    assert coda(s, TRUE_FINAL) is None
    assert coda(s, LIE_ADA) is None
    s.flags.discard(ADA_FLAG)
    assert coda(s, GOOD_TRUTH) is None


def test_all_ending_ids():
    ids = all_ending_ids(MAIN)
    assert len(ids) == len(set(ids)) == 9 + 7
    assert mono_id("lola") in ids
