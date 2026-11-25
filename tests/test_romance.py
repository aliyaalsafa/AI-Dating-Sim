"""Romance stages: date -> girlfriend -> lover (game/sim/romance.py, CLAUDE.md §6.1)."""

import pytest

from sim import affection, romance
from sim.rules import DEFAULT_RULES as R


def ready(gs, cid):
    gs.flags.add("met_" + cid)
    return affection.add_affection(gs, cid, R.date_at - gs.chars[cid].affection)


def test_dates_need_affection_and_meeting(gs):
    assert not romance.can_date(gs, "grace")
    s = ready(gs, "grace")
    assert romance.can_date(s, "grace")
    s.flags.discard("met_grace")
    assert not romance.can_date(s, "grace")


def test_locked_or_dating_girls_cant_be_asked(gs):
    s = ready(gs, "shen")
    s.chars["shen"].romance_locked = True
    assert not romance.can_date(s, "shen")
    s = ready(gs, "shen")
    s.chars["shen"].stage = "girlfriend"
    assert romance.date_candidates(s, ["shen"]) == []


def test_facts_are_learned_in_order(gs):
    s, key = romance.learn_fact(gs, "gemma")
    assert key == romance.FACT_KEYS[0]
    for _ in romance.FACT_KEYS[1:]:
        s, _ = romance.learn_fact(s, "gemma")
    s, key = romance.learn_fact(s, "gemma")
    assert key is None and s.chars["gemma"].known == set(romance.FACT_KEYS)


def test_quiz_asks_known_facts_first(cast):
    quiz = romance.build_quiz(cast, "kimi", "Kimi", known={"place", "item"}, seed=3)
    assert len(quiz) == R.quiz_len
    assert {q["key"] for q in quiz[:2]} == {"place", "item"}
    for q in quiz:
        assert q["answer"] in q["options"]
        assert len(set(q["options"])) == len(q["options"]) == 3


def test_quiz_is_deterministic_per_seed(cast):
    a = romance.build_quiz(cast, "lola", "Lola", known=set(), seed=7)
    b = romance.build_quiz(cast, "lola", "Lola", known=set(), seed=7)
    assert a == b


@pytest.mark.parametrize("correct,passed", [(R.quiz_pass, True), (R.quiz_pass - 1, False)])
def test_date_result(gs, cast, correct, passed):
    s = ready(gs, "claudia")
    before = s.chars["claudia"].affection
    s, ok = romance.resolve_date(s, cast, "claudia", correct)
    assert ok is passed
    assert s.chars["claudia"].dates == 1
    assert (s.chars["claudia"].stage == "girlfriend") is passed
    assert (s.chars["claudia"].affection > before) is passed


def test_special_gift_makes_a_lover(gs, cast, data):
    gid = romance.special_gift(cast, "xenia")
    s = ready(gs, "xenia")
    s.inventory[gid] = 1
    assert not romance.can_become_lover(s, cast, "xenia")        # not her girlfriend yet
    s.chars["xenia"].stage = "girlfriend"
    assert romance.can_become_lover(s, cast, "xenia")
    s = romance.give_special(s, cast, "xenia")
    assert s.chars["xenia"].stage == "lover"
    assert gid not in s.inventory
    assert romance.lovers(s, cast.keys()) == ["xenia"]
    with pytest.raises(ValueError):
        romance.give_special(s, cast, "xenia")


def test_one_favor_pays_for_one_special_gift(cast, data):
    for cid in cast:
        assert data["SHOP"][romance.special_gift(cast, cid)]["price"] <= R.favor_pay
