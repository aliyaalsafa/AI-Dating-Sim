"""Days and time slots (CLAUDE.md §5)."""

from .favors import expire_overdue
from .rules import DEFAULT_RULES, SLOTS, Rules
from .state import GameState, evolve


def slot_name(state: GameState) -> str:
    return SLOTS[state.slot]


def is_evening(state: GameState) -> bool:
    return state.slot == len(SLOTS) - 1


def is_gala_day(state: GameState, rules: Rules = DEFAULT_RULES) -> bool:
    return state.day >= rules.semester_days


def advance(state: GameState, rules: Rules = DEFAULT_RULES) -> GameState:
    """Move to the next slot; after evening, start the next day.

    Starting a new day clears the recap log and expires overdue favors.
    """
    s = evolve(state)
    if s.slot < len(SLOTS) - 1:
        s.slot += 1
        return s
    s.day += 1
    s.slot = 0
    s.day_log = []
    return expire_overdue(s, rules)
