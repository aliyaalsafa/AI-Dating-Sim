"""State-derived achievements (CLAUDE.md §6.5).

`earned` looks at a game state plus the persistent set of endings seen and
returns every achievement id whose condition currently holds. The Ren'Py side
grants whatever is new. Achievements that depend on a single moment (giving a
gift) are still granted directly from the scene that causes them.
"""

from . import clues
from .endings import RIVALS, SOLO, TRUTH, all_ending_ids
from .state import GameState


def earned(state: GameState | None, cast_ids, endings_seen=()) -> set:
    cast_ids = list(cast_ids)
    seen = set(endings_seen)
    got = set()

    if state is not None:
        flags = state.flags
        chars = state.chars

        if cast_ids and all(f"met_{c}" in flags for c in cast_ids):
            got.add("all_met")
        if any(f"{c}.opened_up" in flags for c in cast_ids):
            got.add("opened_up")
        if cast_ids and all(f"{c}.opened_up" in flags for c in cast_ids):
            got.add("open_book")
        done = [c for c in cast_ids if chars[c].favor_status == "done"]
        if done:
            got.add("first_favor")
        if cast_ids and len(done) == len(cast_ids):
            got.add("all_favors")
        if any(f"{c}.bonus_date_done" in flags for c in cast_ids):
            got.add("first_date")
        if any(f"{c}.confessed" in flags for c in cast_ids):
            got.add("first_confession")
        if any(chars[c].dealbreaker_hits > 0 for c in cast_ids):
            got.add("hit_a_nerve")
        if any(chars[c].romance_locked for c in cast_ids):
            got.add("friend_zoned")
        if clues.known_minors(state) or clues.known_majors(state):
            got.add("first_clue")
        if any("mystery.%s.jailbreak" % c in flags for c in cast_ids):
            got.add("jailbreak")
        if any("mystery.%s.crafted" % c in flags for c in cast_ids):
            got.add("prompt_engineer")

    if seen:
        got.add("first_ending")
    if any(e.startswith("good_") for e in seen):
        got.add("good_ending")
    if RIVALS in seen:
        got.add("rivals_ending")
    if SOLO in seen:
        got.add("solo_ending")
    if TRUTH in seen:
        got.add("truth_ending")
    if cast_ids and all(f"good_{c}" in seen for c in cast_ids):
        got.add("all_good")
    if cast_ids and set(all_ending_ids(cast_ids)) <= seen:
        got.add("completionist")

    return got


def endings_progress(cast_ids, endings_seen) -> tuple:
    """(seen, total) for the endings gallery header."""
    ids = all_ending_ids(cast_ids)
    return sum(1 for e in ids if e in set(endings_seen)), len(ids)
