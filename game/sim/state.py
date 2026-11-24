"""Game state.

State objects are treated as immutable by callers: every function in this
package that "changes" state returns a new copy (see `evolve`). Ren'Py only
tracks rollback for store variables, so `$ gs = sim.affection.apply_choice(gs, ...)`
keeps rollback and saves correct.
"""

import copy
from dataclasses import dataclass, field

from .rules import DEFAULT_RULES, Rules

FAVOR_STATUSES = ("not_offered", "active", "done", "failed")


@dataclass
class CharState:
    affection: int = 10
    romance_locked: bool = False
    dealbreaker_hits: int = 0
    favor_status: str = "not_offered"
    favor_started_day: int | None = None
    favor_step: int = 0
    known: set = field(default_factory=set)          # info revealed on the phone, e.g. {"likes"}
    last_gift_day: int | None = None


@dataclass
class GameState:
    chars: dict = field(default_factory=dict)        # char_id -> CharState
    day: int = 1
    slot: int = 0                                    # index into rules.SLOTS
    money: int = 100
    flags: set = field(default_factory=set)
    seen_events: set = field(default_factory=set)
    feed: list = field(default_factory=list)         # @x_unfiltered posts, newest last
    day_log: list = field(default_factory=list)      # (char_id, delta, reason) for the evening recap
    inventory: dict = field(default_factory=dict)    # gift_id -> count
    # Extension point for optional layers (e.g. the clue layer, CLAUDE.md §6.7).
    layers: dict = field(default_factory=dict)


def new_game(cast_ids, rules: Rules = DEFAULT_RULES) -> GameState:
    return GameState(
        chars={cid: CharState(affection=rules.start_affection) for cid in cast_ids},
        money=rules.start_money,
    )


def evolve(state: GameState) -> GameState:
    """Return a deep copy to mutate and hand back."""
    return copy.deepcopy(state)


def has_flag(state: GameState, flag: str) -> bool:
    return flag in state.flags


def set_flag(state: GameState, flag: str) -> GameState:
    s = evolve(state)
    s.flags.add(flag)
    return s


def reveal(state: GameState, char_id: str, info_key: str) -> GameState:
    s = evolve(state)
    s.chars[char_id].known.add(info_key)
    return s
