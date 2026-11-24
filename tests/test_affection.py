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


def test_everyone_starts_at_10(gs):
    assert {c.affection for c in gs.chars.values()} == {10}


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
    assert gs.chars["gemma"].affection == 10           # original untouched (rollback-safe)
    assert s.chars["gemma"].affection > 10
    assert s.day_log[-1][0] == "gemma"


def test_affection_clamps(gs):
    s = affection.add_affection(gs, "grace", 500)
    assert s.chars["grace"].affection == R.max_affection
    s = affection.add_affection(gs, "grace", -500)
    assert s.chars["grace"].affection == 0


def test_dealbreaker_drops_then_locks(gs, cast):
    s = affection.add_affection(gs, "gemma", 70)               # 80
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
    s = affection.add_affection(gs, "grace", 40)              # 50
    u = affection.unlocks(s, "grace")
    assert u == {"opens_up": True, "favor": True, "bonus_date": False, "confession": False}
    s = affection.add_affection(s, "grace", 40)               # 90
    assert all(affection.unlocks(s, "grace").values())


def test_hearts(gs):
    assert affection.hearts(gs, "grace") == 0
    s = affection.add_affection(gs, "grace", 90)
    assert affection.hearts(s, "grace") == 5
