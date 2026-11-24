"""Tunable numbers for every system, in one place.

Ren'Py code can build a custom Rules(...) and pass it through, so balancing
never means editing logic.
"""

from dataclasses import dataclass

SLOTS = ("morning", "afternoon", "evening")


@dataclass(frozen=True)
class Rules:
    semester_days: int = 7             # the gala is the evening of this day (owner: "about 7 days")
    gala_slot: int = 2                 # index into SLOTS; 2 = evening of the last day
    start_affection: int = 10
    max_affection: int = 100
    romance_cap: int = 60              # cap while romance_locked

    # Unlock thresholds
    opens_up_at: int = 25
    favor_at: int = 50
    bonus_date_at: int = 75
    confession_at: int = 90

    # Prompt styles: delta = base + affinity * affinity_weight (before scaling)
    affinity_weight: int = 2
    # Pacing for the short semester: dialogue-choice gains are multiplied by this
    # (after difficulty scaling). Gifts and fixed bumps are not. See DECISIONS.md.
    gain_multiplier: float = 1.5

    # Deal-breakers
    dealbreaker_drop: int = 15
    dealbreaker_lock_hits: int = 2     # nth offense sets romance_locked

    # Favors
    favor_deadline_days: int = 3
    favor_fail_penalty: int = 5

    # Gifts
    gift_loved: int = 8
    gift_liked: int = 4
    gift_neutral: int = 1
    gift_disliked: int = -4
    start_money: int = 100

    # Mystery clue layer (CLAUDE.md §6.7; owner switched it on)
    clue_layer: bool = True
    jailbreak_drop: int = 40           # hard confront: also locks romance
    crafted_drop: int = 5              # well-crafted prompt (needs both minor clues)
    minor_clues_persist: bool = True   # minor clues carry over between playthroughs

    # Endings
    good_min: int = 90
    sweet_min: int = 60
    solo_below: int = 25
    rivals_min: int = 75


DEFAULT_RULES = Rules()
