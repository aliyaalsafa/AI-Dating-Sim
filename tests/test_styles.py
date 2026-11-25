import pytest

from sim.styles import STYLES, affinity, validate_cast_affinities

# The brief's default table (CLAUDE.md §6.2). Blank = 0.
BRIEF = {
    "structured": {"grace": 1, "xenia": -2, "gemma": 1, "kimi": 1},
    "honest":     {"grace": 2, "xenia": 1, "claudia": 2, "shen": 1, "lola": -1},
    "irreverent": {"grace": -1, "xenia": 2, "shen": -1, "lola": 1},
    "concise":    {"xenia": 1, "claudia": -1, "shen": 2, "kimi": -1},
    "curious":    {"claudia": 1, "gemma": 2, "kimi": 1},
    "warm":       {"grace": 1, "xenia": -1, "claudia": 1, "gemma": 1, "lola": 2},
    "practical":  {"grace": 1, "shen": 1, "kimi": 1},
    "pry":        {"xenia": 1, "claudia": -2},
}


def test_cast_matches_brief_table(cast):
    for style in STYLES:
        for cid in cast:
            assert affinity(cast, cid, style) == BRIEF[style].get(cid, 0), (style, cid)


def test_cast_affinities_valid(cast):
    assert validate_cast_affinities(cast) == []


def test_untagged_choice_is_neutral(cast):
    assert affinity(cast, "grace", None) == 0


def test_unknown_style_rejected(cast):
    with pytest.raises(ValueError):
        affinity(cast, "grace", "flattery")
