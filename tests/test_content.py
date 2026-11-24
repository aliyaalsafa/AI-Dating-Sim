"""Checks that the data files and the scene files agree with each other."""

import pathlib
import re

from sim.endings import RIVALS_EVENT_FLAG

GAME = pathlib.Path(__file__).parent.parent / "game"


def defined_labels():
    labels = set()
    for path in GAME.rglob("*.rpy"):
        for m in re.finditer(r"^\s*label\s+([A-Za-z_][A-Za-z0-9_]*)", path.read_text(encoding="utf-8"), re.M):
            labels.add(m.group(1))
    return labels


def test_every_event_label_exists(data):
    labels = defined_labels()
    missing = sorted({e["label"] for e in data["EVENTS"]} - labels)
    assert not missing, missing


def test_every_ending_label_exists(data):
    labels = defined_labels()
    missing = sorted({e["label"] for e in data["ENDINGS"].values()} - labels)
    assert not missing, missing


def test_no_placeholder_endings_left(data):
    assert all(e["label"] != "ending_placeholder" for e in data["ENDINGS"].values())


def test_every_character_has_a_route(data):
    assert set(data["ROUTES"]) == set(data["CAST"])


def test_favor_steps_match_cast(data):
    for cid, route in data["ROUTES"].items():
        assert len(route["favor_steps"]) == data["CAST"][cid]["favor"]["steps"], cid


def test_every_route_has_every_beat(data):
    for cid in data["CAST"]:
        kinds = {e["kind"] for e in data["EVENTS"] if e.get("route") == cid}
        assert {"hangout", "story", "favor", "bonus"} <= kinds, cid
        ids = {e["id"] for e in data["EVENTS"] if e.get("route") == cid}
        for beat in ("opens_up", "favor_offer", "bonus_date", "confession"):
            assert "%s_%s" % (cid, beat) in ids, (cid, beat)


def test_route_flags_are_set_somewhere(data):
    """Events gate on flags like grace.opened_up; some scene must set each one."""
    text = "\n".join(p.read_text(encoding="utf-8") for p in GAME.rglob("*.rpy"))
    needed = {f for e in data["EVENTS"] for f in e.get("requires_flags", ())}
    missing = sorted(f for f in needed if 'set_flag("%s")' % f not in text)
    assert not missing, missing


def test_rivals_scene_sets_the_flag_endings_check():
    text = (GAME / "routes" / "common" / "rivals_study_night.rpy").read_text(encoding="utf-8")
    assert 'set_flag("%s")' % RIVALS_EVENT_FLAG in text


def test_every_route_has_a_dealbreaker_choice(data):
    for cid in data["CAST"]:
        text = "\n".join(p.read_text(encoding="utf-8") for p in (GAME / "routes" / cid).glob("*.rpy"))
        assert 'hit_dealbreaker("%s")' % cid in text, cid


def test_no_model_names_in_dialogue(data):
    """Model names are meta text only (CLAUDE.md §2)."""
    models = ["ChatGPT", "Grok", "Gemini", "DeepSeek", "Claude Sonnet", "Claude Haiku"]
    for path in (GAME / "routes").rglob("*.rpy"):
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith("#"):
                continue
            for m in models:
                assert m not in line, f"{path.name}:{n} mentions {m}"
