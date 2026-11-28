## Event registry (CLAUDE.md §5). Schema: see game/sim/events.py.
## Keep this python block free of Ren'Py calls: tests/conftest.py execs it directly.
##
## "args" are passed to the label: `call expression ev["label"] pass (*ev["args"])`.
## Extra keys the engine ignores but tests check:
##   "introduces": characters this scene introduces (days 1-3 must cover everyone)
##   "route":      which route the event belongs to
##
## Night dates are not map events: the night menu (routes/common/night.rpy)
## offers them, then plays <id>_bonus_date, the quiz, and <id>_confession.

init -3 python:

    EVENTS = []

    # ---------------------------------------------------------------------
    # Common route: prologue and days 1-3 (routes/common/)
    # ---------------------------------------------------------------------
    EVENTS += [
        {"id": "day01_prologue", "label": "day01_prologue", "kind": "story", "forced": True,
         "day_max": 1, "slots": ["morning"], "introduces": ["grace"]},
        # Explore campus: meet everyone else (takes no time; ends when all are met).
        {"id": "day01_explore", "label": "day01_explore", "kind": "story", "forced": True,
         "day_max": 1, "slots": ["afternoon"],
         "introduces": ["claudia", "gemma", "xenia", "lola", "kimi", "shen"]},
        {"id": "day01_dorm", "label": "day01_dorm", "kind": "story", "forced": True,
         "day_max": 1, "slots": ["evening"]},
        {"id": "day03_leaderboard", "label": "day03_leaderboard", "kind": "group", "forced": True,
         "day_min": 3, "day_max": 3, "slots": ["morning"]},
    ]

    # ---------------------------------------------------------------------
    # Character routes (routes/<id>/). Every route has the same beats:
    #   hangout (daily; each one teaches you a fact about her) -> opens up
    #   (she asks her favor at the end of that scene: script.rpy calls
    #   <id>_favor_offer) -> two favor steps, the last with her (pays money)
    #   -> night date + quiz (routes/common/night.rpy) -> special gift
    #   (routes/common/gifts.rpy).
    # ---------------------------------------------------------------------
    ROUTES = {
        "grace": {
            "hangouts": ["council_office"],
            "home": "council_office",
            # Favor steps, in order: (event suffix, location, characters who must be there, slots)
            "favor_steps": [
                ("debate", "quad", [], ["morning"]),
                ("report", "council_office", ["grace"], None),
            ],
        },
        "xenia": {
            "hangouts": ["cafeteria", "observatory_roof"],
            "home": "observatory_roof",
            "favor_steps": [
                ("pickup", "robotics_lab", ["gemma"], None),
                ("deliver", "observatory_roof", ["xenia"], None),
            ],
        },
        "claudia": {
            "hangouts": ["claudia_library"],
            "home": "claudia_library",
            "favor_steps": [
                ("deliver", "cafeteria", ["xenia"], None),
                ("report", "claudia_library", ["claudia"], None),
            ],
        },
        "gemma": {
            "hangouts": ["robotics_lab"],
            "home": "robotics_lab",
            "favor_steps": [
                ("review", "library_3f", ["shen"], None),
                ("finish", "robotics_lab", ["gemma"], None),
            ],
        },
        "shen": {
            "hangouts": ["library_3f"],
            "home": "library_3f",
            "favor_steps": [
                ("wiki", "robotics_lab", ["gemma"], None),
                ("report", "library_3f", ["shen"], None),
            ],
        },
        "kimi": {
            "hangouts": ["activities_hall"],
            "home": "activities_hall",
            "favor_steps": [
                ("swap", "council_office", ["grace"], None),
                ("report", "activities_hall", ["kimi"], None),
            ],
        },
        "lola": {
            "hangouts": ["quad"],
            "home": "quad",
            "favor_steps": [
                ("camera", "robotics_lab", ["gemma"], None),
                ("photo", "quad", ["lola"], None),
            ],
        },
    }

    # Affection threshold for opening up. Keep in step with game/sim/rules.py.
    OPENS_UP_AT = 15

    for _cid, _r in ROUTES.items():
        for _loc in _r["hangouts"]:
            EVENTS.append({"id": "%s_hangout_%s" % (_cid, _loc), "label": "%s_hangout" % _cid,
                           "kind": "hangout", "route": _cid, "location": _loc, "chars": [_cid]})
        _home = _r["home"]
        EVENTS += [
            {"id": "%s_opens_up" % _cid, "label": "%s_opens_up" % _cid, "kind": "story", "route": _cid,
             "location": _home, "chars": [_cid], "min_affection": {_cid: OPENS_UP_AT}},
        ]
        for _i, (_suffix, _loc, _chars, _slots) in enumerate(_r["favor_steps"]):
            _ev = {"id": "%s_favor_%s" % (_cid, _suffix), "label": "%s_favor_%s" % (_cid, _suffix),
                   "kind": "favor", "route": _cid, "location": _loc, "chars": list(_chars),
                   "favor_step": {_cid: _i}, "once": False}
            if _slots:
                _ev["slots"] = _slots
            EVENTS.append(_ev)

    # ---------------------------------------------------------------------
    # Pair scenes (routes/common/pairs/). Each plays once, when both girls
    # are at the location (see "meetups" in data/locations.rpy). Ids match
    # MYSTERY["pairs"] in data/mystery.rpy.
    # ---------------------------------------------------------------------
    PAIR_SCENES = [
        ("grace_claudia", "council_office", ["grace", "claudia"]),
        ("grace_shen", "library_3f", ["grace", "shen"]),
        ("claudia_gemma", "claudia_library", ["claudia", "gemma"]),
        ("gemma_kimi", "robotics_lab", ["gemma", "kimi"]),
        ("xenia_kimi", "observatory_roof", ["xenia", "kimi"]),
        ("xenia_lola", "cafeteria", ["xenia", "lola"]),
        ("lola_shen", "quad", ["lola", "shen"]),
    ]
    # No pair scenes until you've met everyone (all are met on day 1).
    for _pid, _loc, _chars in PAIR_SCENES:
        EVENTS.append({"id": "pair_" + _pid, "label": "pair_" + _pid, "kind": "pair",
                       "location": _loc, "chars": list(_chars), "pair": _pid,
                       "requires_flags": ["met_" + c for c in ROUTES]})
