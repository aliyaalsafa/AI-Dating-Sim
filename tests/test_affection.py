import pytest

from sim import affection
from sim.affection import scale_gain
from sim.rules import DEFAULT_RULES as R


@pytest.mark.parametrize("gain,difficulty,expected", [
    (6, 5, 6),      # 6 * 6/6
    (6, 8, 3),      # 6 * 3/6
    (5, 7, 3),      # 5 * 4/6 = 3.33
    (3, 8, 2),      # 3 * 3/6 = 1.5 -> rounds half up
    (1, 10, 0),     # 1 * 1/6 = 0.17
    (-5, 8, -5),    # losses unscaled
    (0, 5, 0),
])
def test_scale_gain(gain, difficulty, expected):
    assert scale_gain(gain, difficulty) == expected


def test_everyone_starts_ready_to_open_up(gs):
    assert {c.affection for c in gs.chars.values()} == {R.start_affection}
    assert R.start_affection >= R.opens_up_at


def test_style_affinity_changes_outcome(gs, cast):
    # The same honest answer lands better with Claudia (+2) than Gemma (0).
    claudia = affection.choice_delta(cast, "claudia", 2, "honest")
    gemma = affection.choice_delta(cast, "gemma", 2, "honest")
    assert claudia > 0 and gemma > 0
    # Structured is +1 for Grace but -2 for Xenia.
    assert affection.choice_delta(cast, "grace", 2, "structured") > 0
    assert affection.choice_delta(cast, "xenia", 2, "structured") < 0


def test_apply_choice_returns_new_state(gs, cast):
    s = affection.apply_choice(gs, cast, "gemma", 4, "curious")
    assert gs.chars["gemma"].affection == R.start_affection     # original untouched (rollback-safe)
    assert s.chars["gemma"].affection > R.start_affection
    assert s.day_log[-1][0] == "gemma"


def test_affection_clamps(gs):
    s = affection.add_affection(gs, "grace", 500)
    assert s.chars["grace"].affection == R.max_affection
    s = affection.add_affection(gs, "grace", -500)
    assert s.chars["grace"].affection == 0


def test_dealbreaker_drops_then_locks(gs, cast):
    s = affection.add_affection(gs, "gemma", 80 - R.start_affection)   # 80
    s = affection.dealbreaker(s, cast, "gemma")
    assert s.chars["gemma"].affection == 80 - R.dealbreaker_drop
    assert not s.chars["gemma"].romance_locked
    assert "gemma.called_bard" in s.flags
    s = affection.dealbreaker(s, cast, "gemma")
    assert s.chars["gemma"].romance_locked
    assert s.chars["gemma"].affection <= R.romance_cap


def test_romance_lock_caps_gains(gs, cast):
    s = affection.dealbreaker(gs, cast, "shen")
    s = affection.dealbreaker(s, cast, "shen")
    s = affection.add_affection(s, "shen", 200)
    assert s.chars["shen"].affection == R.romance_cap


def test_unlock_thresholds(gs):
    u = affection.unlocks(gs, "grace")
    assert u == {"opens_up": True, "favor": True, "date": False}
    s = affection.add_affection(gs, "grace", R.date_at - R.start_affection)
    assert all(affection.unlocks(s, "grace").values())


def test_romance_cap_blocks_dates():
    assert R.romance_cap < R.date_at


def test_hearts(gs):
    assert affection.hearts(gs, "grace") == 0
    s = affection.add_affection(gs, "grace", 90)
    assert affection.hearts(s, "grace") == 5


def test_gain_multiplier_applies_to_gains_only(cast):
    from dataclasses import replace
    from sim.affection import choice_delta
    from sim.rules import DEFAULT_RULES
    double = replace(DEFAULT_RULES, gain_multiplier=2.0)
    one = replace(DEFAULT_RULES, gain_multiplier=1.0)
    assert choice_delta(cast, "gemma", 3, None, double) == 2 * choice_delta(cast, "gemma", 3, None, one)
    assert choice_delta(cast, "gemma", -4, None, double) == choice_delta(cast, "gemma", -4, None, one) == -4
