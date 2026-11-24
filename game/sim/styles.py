"""Prompt styles: the signature mechanic (CLAUDE.md §6.2)."""

STYLES = ("structured", "honest", "irreverent", "concise", "curious", "warm", "practical", "pry")


def affinity(cast: dict, char_id: str, style: str | None) -> int:
    """A character's affinity (-2..+2) for a style. Untagged choices are 0."""
    if style is None:
        return 0
    if style not in STYLES:
        raise ValueError(f"unknown prompt style: {style!r}")
    return cast[char_id].get("affinities", {}).get(style, 0)


def validate_cast_affinities(cast: dict) -> list:
    """Return a list of problems (empty if the data is valid)."""
    problems = []
    for cid, data in cast.items():
        for style, value in data.get("affinities", {}).items():
            if style not in STYLES:
                problems.append(f"{cid}: unknown style {style!r}")
            elif not -2 <= value <= 2:
                problems.append(f"{cid}: affinity {style}={value} outside -2..2")
    return problems
