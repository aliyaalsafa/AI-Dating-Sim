import pytest

from sim import affection, calendar, favors, gifts
from sim.rules import DEFAULT_RULES as R


def test_favor_offered_once_she_opens_up(gs):
    s = affection.add_affection(gs, "gemma", -10)
    assert not favors.can_offer(s, "gemma")
    assert favors.can_offer(gs, "gemma")          # start affection = opens-up threshold


def test_finished_favor_pays(gs):
    s = favors.offer(gs, "kimi")
    s = favors.advance_step(s, "kimi", 2)
    assert s.money == gs.money
    s = favors.advance_step(s, "kimi", 2)
    assert s.money == gs.money + R.favor_pay


def test_favor_lifecycle(gs):
    s = favors.offer(gs, "gemma")
    assert s.chars["gemma"].favor_status == "active"
    s = favors.advance_step(s, "gemma", total_steps=2)
    assert s.chars["gemma"].favor_status == "active"
    s = favors.advance_step(s, "gemma", total_steps=2)
    assert s.chars["gemma"].favor_status == "done"
    with pytest.raises(ValueError):
        favors.offer(s, "gemma")


def test_favor_fails_after_deadline(gs):
    s = affection.add_affection(gs, "shen", 40)
    s = favors.offer(s, "shen")
    before = s.chars["shen"].affection
    for _ in range(R.favor_deadline_days * 4):        # exactly the deadline: still active
        s = calendar.advance(s)
    assert s.chars["shen"].favor_status == "active"
    assert favors.days_left(s, "shen") == 0
    for _ in range(4):                                 # one more day: failed
        s = calendar.advance(s)
    assert s.chars["shen"].favor_status == "failed"
    assert s.chars["shen"].affection == before - R.favor_fail_penalty


def test_gift_reactions_use_favorites(cast):
    assert gifts.reaction(cast, "grace", "gold_star_stickers") == "loved"
    assert gifts.reaction(cast, "gemma", "label_maker") == "loved"
    assert gifts.reaction(cast, "shen", "designer_pen") == "disliked"
    assert gifts.reaction(cast, "claudia", "rubber_duck") == "neutral"


def test_right_gift_beats_generic(gs, cast, data):
    shop = data["SHOP"]
    gs.money = 100
    s = gifts.buy(gs, shop, "telescope_lens")
    s = gifts.buy(s, shop, "bouquet")
    loved = gifts.give(s, cast, "xenia", "telescope_lens").chars["xenia"].affection
    generic = gifts.give(s, cast, "xenia", "bouquet").chars["xenia"].affection
    assert loved > generic


def test_gift_rules(gs, data, cast):
    shop = data["SHOP"]
    s = gifts.buy(gs, shop, "tea_tin")
    assert s.money == gs.money - shop["tea_tin"]["price"]
    s = gifts.give(s, cast, "claudia", "tea_tin")
    assert "likes" in s.chars["claudia"].known
    assert "tea_tin" not in s.inventory
    s = gifts.buy(s, shop, "tea_tin")
    assert not gifts.can_give(s, "claudia", "tea_tin")    # one per day
    for _ in range(4):
        s = calendar.advance(s)
    assert gifts.can_give(s, "claudia", "tea_tin")


def test_cannot_overspend(gs, data):
    s = gs
    s.money = 0
    with pytest.raises(ValueError):
        gifts.buy(s, data["SHOP"], "tea_tin")


def test_every_gift_reference_exists(cast, data):
    shop = data["SHOP"]
    for cid, c in cast.items():
        for kind, ids in c["gifts"].items():
            for gid in ids:
                assert gid in shop, (cid, kind, gid)
