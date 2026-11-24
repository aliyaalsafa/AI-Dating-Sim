import os
import sys

# Make game/sim importable as `sim`, the same way Ren'Py imports it.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "game"))
