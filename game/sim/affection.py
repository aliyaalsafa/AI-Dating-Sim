"""Affection, difficulty scaling, deal-breakers and unlock thresholds (CLAUDE.md §6.1–6.2)."""

import math

from .rules import DEFAULT_RULES, Rules
from .state import GameState, evolve
from .styles import affinity


def round_half_up(x: float) -> int:
    return int(math.floor(x + 0.5)) if x >= 0 else -int(math.floor(-x + 0.5))


def scale_gain(gain: int, difficulty: int) -> int:
    """Gains are scaled by (11 - difficulty) / 6. Losses are not scaled."""
    if gain <= 0:
        return gain
    return round_half_up(gain * (11 - difficulty) / 6)


def cap_for(state: GameState, char_id: str, rules: Rules = DEFAULT_RULES) -> int:
    return rules.romance_cap if state.chars[char_id].romance_locked else rules.max_affection


def choice_delta(cast: dict, char_id: str, base: int, style: str | None = None,
                 rules: Rules = DEFAULT_RULES) -> int:
    """The affection change a choice would cause, before clamping."""
    raw = base + affinity(cast, char_id, style) * rules.affinity_weight
    gain = scale_gain(raw, cast[char_id]["difficulty"])
    return round_half_up(gain * rules.gain_multiplier) if gain > 0 else gain


def add_affection(state: GameState, char_id: str, delta: int, reason: str = "",
                  rules: Rules = DEFAULT_RULES) -> GameState:
    """Apply an already-computed delta, clamped to 0..cap, and log it."""
    s = evolve(state)
    c = s.chars[char_id]
    before = c.affection
    c.affection = max(0, min(cap_for(s, char_id, rules), before + delta))
    actual = c.affection - before
    if actual or delta:
        s.day_log.append((char_id, actual, reason))
    return s


def apply_choice(state: GameState, cast: dict, char_id: str, base: int,
                 style: str | None = None, rules: Rules = DEFAULT_RULES) -> GameState:
    """A dialogue choice: base change, modified by style affinity, scaled by difficulty."""
    delta = choice_delta(cast, char_id, base, style, rules)
    return add_affection(state, char_id, delta, style or "choice", rules)


def dealbreaker(state: GameState, cast: dict, char_id: str, rules: Rules = DEFAULT_RULES) -> GameState:
    """Player hit this character's deal-breaker. Repeat offenses lock romance."""
    flag = cast[char_id]["dealbreaker"]
    s = evolve(state)
    c = s.chars[char_id]
    c.dealbreaker_hits += 1
    s.flags.add(f"{char_id}.{flag}")
    if c.dealbreaker_hits >= rules.dealbreaker_lock_hits:
        c.romance_locked = True
        s.flags.add(f"{char_id}.romance_locked")
    s = add_affection(s, char_id, -rules.dealbreaker_drop, flag, rules)
    # Re-clamp in case the lock lowered the cap below current affection.
    c = s.chars[char_id]
    c.affection = min(c.affection, cap_for(s, char_id, rules))
    return s


def unlocks(state: GameState, char_id: str, rules: Rules = DEFAULT_RULES) -> dict:
    a = state.chars[char_id].affection
    return {
        "opens_up": a >= rules.opens_up_at,
        "favor": a >= rules.favor_at,
        "bonus_date": a >= rules.bonus_date_at,
        "confession": a >= rules.confession_at,
    }


def hearts(state: GameState, char_id: str, total: int = 5, rules: Rules = DEFAULT_RULES) -> int:
    """Whole hearts to display (0..total)."""
    return min(total, state.chars[char_id].affection * total // rules.max_affection)
