"""Gift shop and gift reactions (CLAUDE.md §6.4)."""

from .affection import add_affection, scale_gain
from .rules import DEFAULT_RULES, Rules
from .state import GameState, evolve


def reaction(cast: dict, char_id: str, gift_id: str) -> str:
    gifts = cast[char_id].get("gifts", {})
    for kind in ("loved", "liked", "disliked"):
        if gift_id in gifts.get(kind, ()):
            return kind
    return "neutral"


def reaction_delta(kind: str, difficulty: int, rules: Rules = DEFAULT_RULES) -> int:
    base = {
        "loved": rules.gift_loved,
        "liked": rules.gift_liked,
        "neutral": rules.gift_neutral,
        "disliked": rules.gift_disliked,
    }[kind]
    return scale_gain(base, difficulty)


def buy(state: GameState, shop: dict, gift_id: str) -> GameState:
    price = shop[gift_id]["price"]
    if state.money < price:
        raise ValueError("not enough money")
    s = evolve(state)
    s.money -= price
    s.inventory[gift_id] = s.inventory.get(gift_id, 0) + 1
    return s


def can_give(state: GameState, char_id: str, gift_id: str) -> bool:
    """One gift per character per day, and you must own it."""
    return state.inventory.get(gift_id, 0) > 0 and state.chars[char_id].last_gift_day != state.day


def give(state: GameState, cast: dict, char_id: str, gift_id: str,
         rules: Rules = DEFAULT_RULES) -> GameState:
    if not can_give(state, char_id, gift_id):
        raise ValueError(f"can't give {gift_id} to {char_id} now")
    kind = reaction(cast, char_id, gift_id)
    s = evolve(state)
    s.inventory[gift_id] -= 1
    if not s.inventory[gift_id]:
        del s.inventory[gift_id]
    c = s.chars[char_id]
    c.last_gift_day = s.day
    if kind in ("loved", "liked"):
        c.known.add("likes")
    elif kind == "disliked":
        c.known.add("dislikes")
    return add_affection(s, char_id, reaction_delta(kind, cast[char_id]["difficulty"], rules),
                         f"gift_{kind}", rules)
