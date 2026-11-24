import ast
import pathlib

import sim

SIM_DIR = pathlib.Path(__file__).parent.parent / "game" / "sim"


def test_sim_imports():
    assert sim.SIM_VERSION


def test_sim_never_imports_renpy():
    for path in SIM_DIR.rglob("*.py"):
        tree = ast.parse(path.read_text(), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names = [a.name for a in node.names]
            elif isinstance(node, ast.ImportFrom):
                names = [node.module or ""]
            else:
                continue
            assert not any(n == "renpy" or n.startswith("renpy.") for n in names), path
