import pickle

from sim import affection, calendar
from sim.state import reveal, set_flag


def test_state_pickles(gs, cast):
    """Ren'Py saves by pickling the store; the state must round-trip."""
    s = affection.apply_choice(gs, cast, "grace", 3, "honest")
    s = calendar.advance(set_flag(s, "met_grace"))
    s2 = pickle.loads(pickle.dumps(s))
    assert s2 == s


def test_helpers_do_not_mutate(gs):
    s = reveal(set_flag(gs, "x"), "shen", "likes")
    assert "x" not in gs.flags and "likes" not in gs.chars["shen"].known
    assert "x" in s.flags and "likes" in s.chars["shen"].known
