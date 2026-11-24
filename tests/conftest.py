import os
import re
import sys
import textwrap

import pytest

GAME_DIR = os.path.join(os.path.dirname(__file__), "..", "game")

# Make game/sim importable as `sim`, the same way Ren'Py imports it.
sys.path.insert(0, GAME_DIR)

from sim.rules import DEFAULT_RULES  # noqa: E402
from sim.state import new_game  # noqa: E402

DATA_FILES = ["data/cast.rpy", "data/locations.rpy", "data/events.rpy", "data/gifts.rpy", "data/endings.rpy"]


def load_rpy_python(*relpaths):
    """Exec the `init ... python:` blocks of data .rpy files and return their namespace.

    Data files keep these blocks free of Ren'Py calls precisely so tests can read them.
    """
    ns = {}
    for rel in relpaths:
        text = open(os.path.join(GAME_DIR, rel), encoding="utf-8").read()
        for m in re.finditer(r"^init[^\n]*python[^\n]*:\n((?:[ \t]+[^\n]*\n|\n)+)", text, re.M):
            exec(textwrap.dedent(m.group(1)), ns)
    return ns


@pytest.fixture(scope="session")
def data():
    return load_rpy_python(*DATA_FILES)


@pytest.fixture
def cast(data):
    return data["CAST"]


@pytest.fixture
def gs(cast):
    return new_game(cast.keys(), DEFAULT_RULES)
