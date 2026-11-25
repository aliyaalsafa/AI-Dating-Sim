"""Tunable numbers for every system, in one place.

Ren'Py code can build a custom Rules(...) and pass it through, so balancing
never means editing logic. Values here were tuned with scripts/pacing_sim.py
(see DECISIONS.md).
"""

from dataclasses import dataclass

# Morning/afternoon/evening are for the campus map; night is for dates only.
SLOTS = ("morning", "afternoon", "evening", "night")
DAY_SLOTS = SLOTS[:3]
NIGHT = 3

STAGES = ("none", "girlfriend", "lover")


@dataclass(frozen=True)
class Rules:
    semester_days: int = 14            # the gala is the evening (and night) of this day
    gala_slot: int = 2                 # index into SLOTS; 2 = evening of the last day
    start_affection: int = 15           # = opens_up_at: your first real conversation is her opening up
    max_affection: int = 100
    romance_cap: int = 30              # cap while romance_locked (below date_at: no dates)

    # Unlock thresholds
    opens_up_at: int = 15              # she opens up, then asks her favor in the same scene
    date_at: int = 35                  # night dates become possible

    # Prompt styles: delta = base + affinity * affinity_weight (before scaling)
    affinity_weight: int = 2
    # Dialogue-choice gains are multiplied by this after difficulty scaling.
    # Gifts and fixed bumps are not. Tuned with scripts/pacing_sim.py.
    gain_multiplier: float = 1.5

    # Deal-breakers
    dealbreaker_drop: int = 15
    dealbreaker_lock_hits: int = 2     # nth offense sets romance_locked

    # Favors: the main source of money
    favor_deadline_days: int = 3
    favor_fail_penalty: int = 5
    favor_pay: int = 40
    favor_done_bonus: int = 10         # affection (scaled by difficulty) when a favor is finished

    # Gifts
    gift_loved: int = 8
    gift_liked: int = 4
    gift_neutral: int = 1
    gift_disliked: int = -4
    start_money: int = 20

    # Night dates: a short quiz about her
    quiz_len: int = 3
    quiz_pass: int = 2                 # correct answers needed to become her girlfriend
    quiz_pass_bonus: int = 5
    quiz_fail_drop: int = 3

    # Pair scenes (two girls at one location)
    pair_gain: int = 6                 # affection for each girl (scaled by difficulty)

    # Mystery
    clue_layer: bool = True
    jailbreak_drop: int = 40           # hard confront: also locks romance
    crafted_drop: int = 5              # well-crafted prompt (needs every hint about her)
    minor_clues_persist: bool = True   # hints carry over between playthroughs

    # Gala endings (lovers among the main cast, when you tell the truth)
    good_truth_min: int = 4
    bad_truth_min: int = 2


DEFAULT_RULES = Rules()
