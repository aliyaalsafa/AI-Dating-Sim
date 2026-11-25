"""Days and time slots (CLAUDE.md §5).

Morning, afternoon and evening are spent on the campus map. Night is for
dates only. The day's recap shows after the night.
"""

from .favors import expire_overdue
from .rules import DEFAULT_RULES, NIGHT, SLOTS, Rules
from .state import GameState, evolve


def slot_name(state: GameState) -> str:
    return SLOTS[state.slot]


def is_night(state: GameState) -> bool:
    return state.slot == NIGHT


def is_evening(state: GameState) -> bool:
    return state.slot == NIGHT - 1


def is_last_slot(state: GameState) -> bool:
    """The slot after which the day ends (and the recap shows)."""
    return state.slot == len(SLOTS) - 1


def is_gala_day(state: GameState, rules: Rules = DEFAULT_RULES) -> bool:
    """True once the gala slot (evening of the last day, by default) arrives."""
    return state.day > rules.semester_days or (
        state.day == rules.semester_days and state.slot >= rules.gala_slot)


def advance(state: GameState, rules: Rules = DEFAULT_RULES) -> GameState:
    """Move to the next slot; after night, start the next day.

    Starting a new day clears the recap log and daily event limits, and
    expires overdue favors.
    """
    s = evolve(state)
    if s.slot < len(SLOTS) - 1:
        s.slot += 1
        return s
    s.day += 1
    s.slot = 0
    s.day_log = []
    s.seen_today = set()
    return expire_overdue(s, rules)


def playable_slots(rules: Rules = DEFAULT_RULES) -> dict:
    """How many day slots and nights a semester has before the gala."""
    days = (rules.semester_days - 1) * (len(SLOTS) - 1) + rules.gala_slot
    nights = rules.semester_days - 1
    return {"day": days, "night": nights}
