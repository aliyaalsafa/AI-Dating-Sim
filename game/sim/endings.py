"""Ending evaluation at the Founders' Gala (CLAUDE.md §7)."""

from . import clues
from .rules import DEFAULT_RULES, Rules
from .state import GameState

RIVALS_PAIR = ("grace", "shen")
RIVALS_EVENT_FLAG = "rivals_joint_event_done"

SOLO = "solo"
RIVALS = "rivals"
TRUTH = "truth"                 # secret mystery ending
TRUTH_CHOICE = "__truth__"      # gala choice offered only once the mystery is solved


def ending_id(kind: str, char_id: str) -> str:
    return f"{kind}_{char_id}"   # e.g. "good_grace"


def evaluate_ending(state: GameState, gala_choice: str | None, rules: Rules = DEFAULT_RULES) -> str:
    """Return the EndingId for the player's gala choice (None = asked no one).

    Order matters:
      0. Truth (secret): chose to reveal the mystery, and every major clue is found.
      1. Solo: asked no one, or everyone is below `solo_below`.
      2. Rivals (secret): asked Grace or Shen, both >= `rivals_min`, joint event done.
      3. Good: >= `good_min`, not locked, favor done.
      4. Sweet: >= `sweet_min`, not locked.
      5. Friends: anything else.
    """
    chars = state.chars
    if gala_choice == TRUTH_CHOICE:
        order = list(chars)
        if rules.clue_layer and clues.solved(state, order):
            return TRUTH
        gala_choice = None      # not solved: treated as asking no one
    if gala_choice is None or all(c.affection < rules.solo_below for c in chars.values()):
        return SOLO

    if (
        gala_choice in RIVALS_PAIR
        and all(chars[c].affection >= rules.rivals_min for c in RIVALS_PAIR if c in chars)
        and all(c in chars for c in RIVALS_PAIR)
        and RIVALS_EVENT_FLAG in state.flags
    ):
        return RIVALS

    c = chars[gala_choice]
    if not c.romance_locked and c.affection >= rules.good_min and c.favor_status == "done":
        return ending_id("good", gala_choice)
    if not c.romance_locked and c.affection >= rules.sweet_min:
        return ending_id("sweet", gala_choice)
    return ending_id("friends", gala_choice)


def all_ending_ids(cast_ids, rules: Rules = DEFAULT_RULES) -> list:
    ids = [SOLO, RIVALS] + ([TRUTH] if rules.clue_layer else [])
    for cid in cast_ids:
        ids += [ending_id(k, cid) for k in ("good", "sweet", "friends")]
    return ids
