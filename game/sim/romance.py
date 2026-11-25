"""Romance stages: date -> girlfriend -> lover (CLAUDE.md §6.1).

- Affection reaches `date_at`: you can ask her on a night date.
- On the date she quizzes you about herself. Pass and she's your girlfriend.
- Give your girlfriend her special gift (from the store) and she's your lover.

Facts the quiz asks about are learned by spending time with her (one per
hangout), from gifts, and when she opens up. They show on the phone.
"""

import random

from .affection import add_affection, scale_gain
from .rules import DEFAULT_RULES, Rules
from .state import GameState, evolve

# Order in which hangouts reveal facts. "likes"/"dislikes" are also revealed
# by opening up and by gifts.
FACT_KEYS = ("likes", "place", "item", "dislikes", "symbol")

QUESTION_TEXT = {
    "likes": "Which of these does {name} like?",
    "dislikes": "Which of these does {name} dislike?",
    "place": "Where is {name}'s favorite place?",
    "item": "What is {name}'s favorite thing?",
    "symbol": "Which symbol is most like {name}?",
}


def met(state: GameState, cid: str) -> bool:
    return f"met_{cid}" in state.flags


def can_date(state: GameState, cid: str, rules: Rules = DEFAULT_RULES) -> bool:
    c = state.chars[cid]
    return (met(state, cid) and c.stage == "none" and not c.romance_locked
            and c.affection >= rules.date_at)


def date_candidates(state: GameState, cast_ids, rules: Rules = DEFAULT_RULES) -> list:
    return [c for c in cast_ids if can_date(state, c, rules)]


def next_fact(state: GameState, cid: str):
    known = state.chars[cid].known
    return next((k for k in FACT_KEYS if k not in known), None)


def learn_fact(state: GameState, cid: str):
    """Reveal the next unknown fact about her. Returns (state, key or None)."""
    key = next_fact(state, cid)
    if key is None:
        return state, None
    s = evolve(state)
    s.chars[cid].known.add(key)
    return s, key


def _fact_values(cast: dict, cid: str, key: str) -> list:
    v = cast[cid]["favorites"][key]
    return list(v) if isinstance(v, (list, tuple)) else [v]


def build_quiz(cast: dict, cid: str, name: str, known=(), seed: int = 0,
               rules: Rules = DEFAULT_RULES) -> list:
    """Questions about her, facts the player has learned first.

    Each question is {"key", "prompt", "options", "answer"}; distractors come
    from the other characters, so a guess is a real guess.
    """
    rng = random.Random(seed)
    learned = [k for k in FACT_KEYS if k in known]
    unknown = [k for k in FACT_KEYS if k not in known]
    rng.shuffle(learned)
    rng.shuffle(unknown)
    keys = (learned + unknown)[:rules.quiz_len]
    quiz = []
    for key in keys:
        answer = rng.choice(_fact_values(cast, cid, key))
        mine = set(_fact_values(cast, cid, key))
        pool = sorted({v for other in cast if other != cid
                       for v in _fact_values(cast, other, key) if v not in mine})
        options = rng.sample(pool, min(2, len(pool))) + [answer]
        rng.shuffle(options)
        quiz.append({"key": key, "prompt": QUESTION_TEXT[key].format(name=name),
                     "options": options, "answer": answer})
    return quiz


def resolve_date(state: GameState, cast: dict, cid: str, correct: int,
                 rules: Rules = DEFAULT_RULES):
    """Apply the quiz result. Returns (state, passed)."""
    s = evolve(state)
    s.chars[cid].dates += 1
    passed = correct >= rules.quiz_pass
    if passed:
        s.chars[cid].stage = "girlfriend"
        s.flags.add(f"{cid}.girlfriend")
        s = add_affection(s, cid, scale_gain(rules.quiz_pass_bonus, cast[cid]["difficulty"]),
                          "date_passed", rules)
    else:
        s = add_affection(s, cid, -rules.quiz_fail_drop, "date_failed", rules)
    return s, passed


def special_gift(cast: dict, cid: str) -> str:
    return cast[cid]["special_gift"]


def can_become_lover(state: GameState, cast: dict, cid: str) -> bool:
    c = state.chars[cid]
    return (c.stage == "girlfriend" and not c.romance_locked
            and state.inventory.get(special_gift(cast, cid), 0) > 0)


def give_special(state: GameState, cast: dict, cid: str) -> GameState:
    if not can_become_lover(state, cast, cid):
        raise ValueError(f"{cid} can't become a lover now")
    s = evolve(state)
    gid = special_gift(cast, cid)
    s.inventory[gid] -= 1
    if not s.inventory[gid]:
        del s.inventory[gid]
    s.chars[cid].stage = "lover"
    s.chars[cid].last_gift_day = s.day
    s.flags.add(f"{cid}.lover")
    s.day_log.append((cid, 0, "lover"))
    return s


def lovers(state: GameState, cast_ids) -> list:
    return [c for c in cast_ids if c in state.chars and state.chars[c].stage == "lover"]


def girlfriends(state: GameState, cast_ids) -> list:
    return [c for c in cast_ids if c in state.chars and state.chars[c].stage == "girlfriend"]
