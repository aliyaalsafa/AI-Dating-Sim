"""Mystery clue layer (game/sim/clues.py, CLAUDE.md §6.7)."""

import pytest

from sim import clues
from sim.endings import SOLO, TRUTH, TRUTH_CHOICE, all_ending_ids, evaluate_ending
from sim.rules import DEFAULT_RULES as R
from sim.state import evolve

ORDER = ["grace", "xenia", "claudia", "gemma", "shen"]


def test_minor_rule_i_plus_1_and_3():
    subs = clues.minor_subjects(ORDER)
    assert subs["grace"] == {"freebie": "xenia", "earned": "gemma"}
    assert subs["shen"] == {"freebie": "grace", "earned": "claudia"}
    # everyone is the subject of exactly two minor clues, from two different sources
    for cid in ORDER:
        srcs = clues.sources_about(ORDER, cid)
        assert len(srcs) == 2 and cid not in srcs


def started(gs):
    s = evolve(gs)
    s.flags.add(clues.STARTED_FLAG)
    return s


def test_crafted_needs_both_minors(gs):
    s = started(gs)
    assert not clues.can_craft(s, ORDER, "grace")
    with pytest.raises(ValueError):
        clues.confront(s, ORDER, "grace", clues.CRAFTED)
    s, pair = clues.give_minor(s, ORDER, "shen", clues.FREEBIE)      # shen's freebie is about grace
    assert pair == ("shen", "grace") and not clues.can_craft(s, ORDER, "grace")
    s, _ = clues.give_minor(s, ORDER, "claudia", clues.EARNED)       # claudia's earned is about grace
    assert clues.can_craft(s, ORDER, "grace")
    before = s.chars["grace"].affection
    s = clues.confront(s, ORDER, "grace", clues.CRAFTED)
    assert "grace" in clues.known_majors(s)
    assert s.chars["grace"].affection == max(0, before - R.crafted_drop)
    assert not s.chars["grace"].romance_locked
    assert not clues.can_confront(s, "grace")


def test_jailbreak_always_works_but_locks(gs):
    s = started(gs)
    s.chars["xenia"].affection = 80
    s = clues.confront(s, ORDER, "xenia", clues.JAILBREAK)
    assert "xenia" in clues.known_majors(s)
    assert s.chars["xenia"].romance_locked
    assert s.chars["xenia"].affection == 40


def test_confront_requires_started(gs):
    assert not clues.can_confront(gs, "grace")
    assert clues.can_confront(started(gs), "grace")


def test_seeded_minors_from_earlier_runs(gs):
    s = clues.seed_minors(gs, [("shen", "grace"), ("claudia", "grace")])
    assert clues.can_craft(s, ORDER, "grace")
    assert clues.known_minors(gs) == set()          # original untouched


def test_truth_ending_needs_every_major(gs):
    s = started(gs)
    for cid in ORDER[:-1]:
        s = clues.confront(s, ORDER, cid, clues.JAILBREAK)
    assert evaluate_ending(s, TRUTH_CHOICE) == SOLO          # one missing: treated as asking no one
    s = clues.confront(s, ORDER, "shen", clues.JAILBREAK)
    assert clues.solved(s, ORDER)
    assert evaluate_ending(s, TRUTH_CHOICE) == TRUTH


def test_truth_is_a_listed_ending():
    assert TRUTH in all_ending_ids(ORDER)
    assert len(all_ending_ids(ORDER)) == 18


def test_mystery_data_is_valid(data, cast):
    assert clues.validate_mystery(data["MYSTERY"], cast.keys()) == []


def test_recap_logs_the_actual_change(gs):
    s = started(gs)
    s.chars["xenia"].affection = 16
    s = clues.confront(s, ORDER, "xenia", clues.JAILBREAK)
    assert s.day_log[-1] == ("xenia", -16, "jailbreak")
