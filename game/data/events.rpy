## Event registry (CLAUDE.md §5). Schema: see game/sim/events.py.
## Keep this python block free of Ren'Py calls: tests/conftest.py execs it directly.
##
## "args" are passed to the label: `call expression ev["label"] pass (*ev["args"])`.
## Extra keys the engine ignores but tests check:
##   "introduces": characters this scene introduces (days 1-3 must cover everyone)
##   "route":      which route the event belongs to

init -3 python:

    EVENTS = []

    # ---------------------------------------------------------------------
    # Common route: prologue and days 1-3 (routes/common/)
    # ---------------------------------------------------------------------
    EVENTS += [
        {"id": "day01_prologue", "label": "day01_prologue", "kind": "story", "forced": True,
         "day_max": 1, "slots": ["morning"], "introduces": ["grace", "claudia"]},
        {"id": "day01_lunch", "label": "day01_lunch", "kind": "group", "forced": True,
         "day_max": 1, "slots": ["afternoon"], "introduces": ["xenia", "gemma"]},
        {"id": "day01_dorm", "label": "day01_dorm", "kind": "story", "forced": True,
         "day_max": 1, "slots": ["evening"]},
        # Meet Shen early if you go looking for her on day 2...
        {"id": "day02_meet_shen_library", "label": "day02_meet_shen", "kind": "story",
         "location": "library_3f", "chars": ["shen"], "day_max": 2, "forbids_flags": ["met_shen"]},
        {"id": "day02_meet_shen_lab", "label": "day02_meet_shen", "kind": "story",
         "location": "robotics_lab", "chars": ["shen"], "day_max": 2, "forbids_flags": ["met_shen"]},
        # ...and everyone meets her at the leaderboard on day 3 regardless.
        {"id": "day03_leaderboard", "label": "day03_leaderboard", "kind": "group", "forced": True,
         "day_min": 3, "day_max": 3, "slots": ["morning"], "introduces": ["shen"]},
    ]

    # ---------------------------------------------------------------------
    # Character routes (routes/<id>/). Every route has the same beats:
    #   hangout (daily) -> opens up at 25 -> favor offer at 50 -> favor steps
    #   -> bonus date at 75 -> confession at 90 (after the bonus date).
    # ---------------------------------------------------------------------
    ROUTES = {
        "grace": {
            "hangouts": ["council_office"],
            "home": "council_office",
            "date_slots": ["evening"],
            # Favor steps, in order: (event suffix, location, characters who must be there, slots)
            "favor_steps": [
                ("debate", "quad", [], ["morning"]),
                ("report", "council_office", ["grace"], None),
            ],
        },
        "xenia": {
            "hangouts": ["cafeteria", "observatory_roof"],
            "home": "observatory_roof",
            "date_slots": ["evening"],
            "favor_steps": [
                ("pickup", "robotics_lab", ["gemma"], None),
                ("deliver", "observatory_roof", ["xenia"], None),
            ],
        },
        "claudia": {
            "hangouts": ["quad", "claudia_library"],
            "home": "claudia_library",
            "date_slots": ["evening"],
            "favor_steps": [
                ("deliver", "cafeteria", ["xenia"], None),
                ("report", "claudia_library", ["claudia"], None),
            ],
        },
        "gemma": {
            "hangouts": ["robotics_lab"],
            "home": "robotics_lab",
            "date_slots": ["evening"],
            "favor_steps": [
                ("pick", "robotics_lab", ["gemma"], None),
                ("review", "library_3f", ["shen"], None),
                ("finish", "robotics_lab", ["gemma"], None),
            ],
        },
        "shen": {
            "hangouts": ["library_3f", "robotics_lab"],
            "home": "library_3f",
            "date_slots": ["evening"],
            "favor_steps": [
                ("claudia", "claudia_library", ["claudia"], None),
                ("wiki", "robotics_lab", ["gemma"], None),
                ("report", "library_3f", ["shen"], None),
            ],
        },
    }

    for _cid, _r in ROUTES.items():
        for _loc in _r["hangouts"]:
            EVENTS.append({"id": "%s_hangout_%s" % (_cid, _loc), "label": "%s_hangout" % _cid,
                           "kind": "hangout", "route": _cid, "location": _loc, "chars": [_cid]})
        _home = _r["home"]
        EVENTS += [
            {"id": "%s_opens_up" % _cid, "label": "%s_opens_up" % _cid, "kind": "story", "route": _cid,
             "location": _home, "chars": [_cid], "min_affection": {_cid: 25}},
            {"id": "%s_favor_offer" % _cid, "label": "%s_favor_offer" % _cid, "kind": "story", "route": _cid,
             "location": _home, "chars": [_cid], "min_affection": {_cid: 50},
             "requires_flags": ["%s.opened_up" % _cid], "favor_status": {_cid: "not_offered"}},
            {"id": "%s_bonus_date" % _cid, "label": "%s_bonus_date" % _cid, "kind": "bonus", "route": _cid,
             "location": _home, "chars": [_cid], "slots": _r["date_slots"], "min_affection": {_cid: 75}},
            {"id": "%s_confession" % _cid, "label": "%s_confession" % _cid, "kind": "story", "route": _cid,
             "location": _home, "chars": [_cid], "slots": _r["date_slots"], "min_affection": {_cid: 90},
             "requires_flags": ["%s.bonus_date_done" % _cid]},
        ]
        for _i, (_suffix, _loc, _chars, _slots) in enumerate(_r["favor_steps"]):
            _ev = {"id": "%s_favor_%s" % (_cid, _suffix), "label": "%s_favor_%s" % (_cid, _suffix),
                   "kind": "favor", "route": _cid, "location": _loc, "chars": list(_chars),
                   "favor_step": {_cid: _i}, "once": False}
            if _slots:
                _ev["slots"] = _slots
            EVENTS.append(_ev)

    # ---------------------------------------------------------------------
    # Group scenes
    # ---------------------------------------------------------------------
    EVENTS += [
        {"id": "group_lab_partners", "label": "group_lab_partners", "kind": "group",
         "location": "robotics_lab", "chars": ["gemma", "shen"], "slots": ["morning"], "day_min": 4},
        # Rivals (secret ending setup): Grace shows up at Shen's library table one evening.
        # Lower priority than Shen's own story beats so her route isn't blocked.
        {"id": "rivals_study_night", "label": "rivals_study_night", "kind": "group", "route": "rivals",
         "location": "library_3f", "chars": ["shen"], "slots": ["evening"], "priority": -1,
         "min_affection": {"grace": 60, "shen": 60},
         "requires_flags": ["grace.opened_up", "shen.opened_up"]},
    ]
