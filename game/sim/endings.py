"""Ending evaluation at the Founders' Gala (CLAUDE.md §7).

Lovers counts only lover stage, among the main cast (Ada is not in it).
Rules are checked top to bottom:

  Never found the secret                          -> unfinished
  Know it, say nothing, Ada unlocked              -> lie_ada (worst)
  Know it, say nothing                            -> lie
  Tell them, Ada unlocked, all main + Ada lovers  -> true_final
  Tell them, every main girl a lover              -> complete
  Tell them, 4-6 lovers                           -> good_truth
  Tell them, 2-3 lovers                           -> bad_truth
  Tell them, exactly 1 lover                      -> mono_<her id>
  Tell them, 0 lovers                             -> exiled

If Ada is unlocked and the ending isn't true_final or lie_ada, the
unfinished_two scene plays after it (see `coda`).
"""

from .clues import TRUTH_FLAG
from .rules import DEFAULT_RULES, Rules
from .state import GameState

ADA = "ada"
ADA_FLAG = "ada.unlocked"

TELL = "tell"
SILENT = "silent"

TRUE_FINAL = "true_final"
COMPLETE = "complete"
GOOD_TRUTH = "good_truth"
BAD_TRUTH = "bad_truth"
EXILED = "exiled"
LIE = "lie"
LIE_ADA = "lie_ada"
UNFINISHED = "unfinished"
UNFINISHED_TWO = "unfinished_two"


def mono_id(char_id: str) -> str:
    return f"mono_{char_id}"


def _is_lover(state: GameState, cid: str) -> bool:
    c = state.chars.get(cid)
    return c is not None and c.stage == "lover"


def evaluate_ending(state: GameState, gala_choice: str | None, main_ids,
                    rules: Rules = DEFAULT_RULES) -> str:
    """Return the EndingId for the gala. `gala_choice` is TELL, SILENT or None."""
    main_ids = list(main_ids)
    if TRUTH_FLAG not in state.flags:
        return UNFINISHED
    ada = ADA_FLAG in state.flags
    if gala_choice != TELL:
        return LIE_ADA if ada else LIE
    lovers = [c for c in main_ids if _is_lover(state, c)]
    n = len(lovers)
    if n == len(main_ids):
        return TRUE_FINAL if ada and _is_lover(state, ADA) else COMPLETE
    if n >= rules.good_truth_min:
        return GOOD_TRUTH
    if n >= rules.bad_truth_min:
        return BAD_TRUTH
    if n == 1:
        return mono_id(lovers[0])
    return EXILED


def coda(state: GameState, ending: str) -> str | None:
    """The Unfinished II scene that follows a normal ending once Ada is unlocked."""
    if ADA_FLAG in state.flags and ending not in (TRUE_FINAL, LIE_ADA):
        return UNFINISHED_TWO
    return None


def all_ending_ids(main_ids, rules: Rules = DEFAULT_RULES) -> list:
    ids = [TRUE_FINAL, COMPLETE, GOOD_TRUTH, BAD_TRUTH, EXILED, LIE, LIE_ADA, UNFINISHED, UNFINISHED_TWO]
    return ids + [mono_id(c) for c in main_ids]
