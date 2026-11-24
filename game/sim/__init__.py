"""Pure-Python game logic for the dating sim.

Nothing in this package may import ``renpy``. The .rpy files call into it, and
pytest exercises it directly (see tests/). Systems land in M1:
state, affection, styles, calendar, events, endings.
"""

SIM_VERSION = "0.0.1"
