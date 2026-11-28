"""Checks that the data files and the scene files agree with each other."""

import pathlib
import re


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
    """Map events, plus the labels the engine calls by name (CLAUDE.md §6.1)."""
    labels = defined_labels()
    for cid in data["CAST"]:
        kinds = {e["kind"] for e in data["EVENTS"] if e.get("route") == cid}
        assert {"hangout", "story", "favor"} <= kinds, cid
        assert "%s_opens_up" % cid in {e["id"] for e in data["EVENTS"]}, cid
        for beat in ("favor_offer", "bonus_date", "confession", "lover"):
            assert "%s_%s" % (cid, beat) in labels, (cid, beat)


def test_favors_end_with_her(data):
    """The last favor step is spent with her, and every favor has two steps."""
    for cid, route in data["ROUTES"].items():
        assert len(route["favor_steps"]) == 2, cid
        assert cid in route["favor_steps"][-1][2], cid


def test_every_girl_has_a_special_gift(data):
    for cid, c in data["CAST"].items():
        assert data["SHOP"][c["special_gift"]].get("special"), cid
    specials = [g for g, item in data["SHOP"].items() if item.get("special")]
    assert sorted(specials) == sorted(c["special_gift"] for c in data["CAST"].values())


def test_schedule_is_consistent(data):
    from sim.events import validate_schedule
    assert validate_schedule(data["LOCATIONS"], data["CAST"]) == []


def test_every_pair_scene_meets_and_has_a_scene(data):
    """Each MYSTERY pair has a map event, a meetup at that location, and calls pair_done."""
    events = {e["pair"]: e for e in data["EVENTS"] if e["kind"] == "pair"}
    for p in data["MYSTERY"]["pairs"]:
        ev = events[p["id"]]
        assert sorted(ev["chars"]) == sorted(p["chars"]), p["id"]
        meetups = data["LOCATIONS"][ev["location"]].get("meetups", [])
        assert any(sorted(m["chars"]) == sorted(p["chars"]) for m in meetups), p["id"]
        text = (GAME / "routes" / "common" / "pairs" / ("pair_%s.rpy" % p["id"])).read_text(encoding="utf-8")
        assert 'call pair_done("%s")' % p["id"] in text, p["id"]


def test_mom_texts_cover_the_semester(data):
    from sim.rules import DEFAULT_RULES as R
    assert set(range(1, R.semester_days)) <= set(data["MOM_TEXTS"])


def test_route_flags_are_set_somewhere(data):
    """Events gate on flags like grace.opened_up; some scene must set each one."""
    text = "\n".join(p.read_text(encoding="utf-8") for p in GAME.rglob("*.rpy"))
    needed = {f for e in data["EVENTS"] for f in e.get("requires_flags", ())}
    missing = sorted(f for f in needed if 'set_flag("%s")' % f not in text)
    assert not missing, missing


def test_every_route_has_a_dealbreaker_choice(data):
    for cid in data["CAST"]:
        text = "\n".join(p.read_text(encoding="utf-8") for p in (GAME / "routes" / cid).glob("*.rpy"))
        assert 'hit_dealbreaker("%s")' % cid in text, cid


def test_no_model_names_in_dialogue(data):
    """Model names are meta text only (CLAUDE.md §2)."""
    models = ["ChatGPT", "Grok", "Gemini", "DeepSeek", "Claude Sonnet", "Claude Haiku", "Kimi K3", "Llama", "Moonshot"]
    for path in (GAME / "routes").rglob("*.rpy"):
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith("#"):
                continue
            for m in models:
                assert m not in line, f"{path.name}:{n} mentions {m}"


def test_every_character_has_a_gala_greeting(data):
    labels = defined_labels()
    for cid in data["CAST"]:
        assert "gala_greeting_" + cid in labels, cid


def test_every_achievement_can_be_granted(data):
    """Each achievement is either derived in sim/achievements.py or granted by a scene."""
    sim_src = (GAME / "sim" / "achievements.py").read_text(encoding="utf-8")
    rpy = "\n".join(p.read_text(encoding="utf-8") for p in GAME.rglob("*.rpy"))
    for aid in data["ACHIEVEMENTS"]:
        assert ('"%s"' % aid in sim_src) or ('grant("%s")' % aid in rpy), aid


def test_gallery_lists_every_ending(data):
    from sim.endings import all_ending_ids
    assert set(data["ENDINGS"]) == set(all_ending_ids(data["CAST"].keys()))
    labels = defined_labels()
    missing = sorted(e["label"] for e in data["ENDINGS"].values() if e["label"] not in labels)
    assert not missing, missing


def test_mystery_starts_on_day_one():
    dorm = (GAME / "routes" / "common" / "day01_dorm.rpy").read_text(encoding="utf-8")
    assert "call mystery_hook" in dorm


def test_every_girl_has_a_first_meeting(data):
    labels = defined_labels()
    for cid in data["CAST"]:
        if cid != "grace":                          # Grace meets you at the gates
            assert "meet_" + cid in labels, cid
