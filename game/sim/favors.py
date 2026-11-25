"""Favors: short multi-step quests, the main source of money (CLAUDE.md §6.3)."""

from .affection import add_affection
from .rules import DEFAULT_RULES, Rules
from .state import GameState, evolve


def can_offer(state: GameState, char_id: str, rules: Rules = DEFAULT_RULES) -> bool:
    c = state.chars[char_id]
    return c.favor_status == "not_offered" and c.affection >= rules.opens_up_at


def offer(state: GameState, char_id: str) -> GameState:
    s = evolve(state)
    c = s.chars[char_id]
    if c.favor_status != "not_offered":
        raise ValueError(f"{char_id}'s favor is already {c.favor_status}")
    c.favor_status = "active"
    c.favor_started_day = s.day
    c.favor_step = 0
    return s


def advance_step(state: GameState, char_id: str, total_steps: int,
                 rules: Rules = DEFAULT_RULES) -> GameState:
    """Complete one step. Finishing the last step marks the favor done and pays out."""
    s = evolve(state)
    c = s.chars[char_id]
    if c.favor_status != "active":
        raise ValueError(f"{char_id}'s favor is not active")
    c.favor_step += 1
    if c.favor_step >= total_steps:
        c.favor_status = "done"
        s.money += rules.favor_pay
    return s


def expire_overdue(state: GameState, rules: Rules = DEFAULT_RULES) -> GameState:
    """Fail every favor still active more than `favor_deadline_days` after it started."""
    s = state
    for cid, c in state.chars.items():
        if c.favor_status == "active" and s.day - c.favor_started_day > rules.favor_deadline_days:
            s = evolve(s)
            s.chars[cid].favor_status = "failed"
            s = add_affection(s, cid, -rules.favor_fail_penalty, "favor_failed", rules)
    return s


def days_left(state: GameState, char_id: str, rules: Rules = DEFAULT_RULES) -> int | None:
    c = state.chars[char_id]
    if c.favor_status != "active":
        return None
    return rules.favor_deadline_days - (state.day - c.favor_started_day)
