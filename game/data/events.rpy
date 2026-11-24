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
    # Grace's route (routes/grace/)
    # ---------------------------------------------------------------------
    EVENTS += [
        {"id": "grace_hangout", "label": "grace_hangout", "kind": "hangout", "route": "grace",
         "location": "council_office", "chars": ["grace"]},
        {"id": "grace_opens_up", "label": "grace_opens_up", "kind": "story", "route": "grace",
         "location": "council_office", "chars": ["grace"], "min_affection": {"grace": 25}},
        {"id": "grace_favor_offer", "label": "grace_favor_offer", "kind": "story", "route": "grace",
         "location": "council_office", "chars": ["grace"], "min_affection": {"grace": 50},
         "requires_flags": ["grace.opened_up"], "favor_status": {"grace": "not_offered"}},
        # Favor step 1: run her Debate Club meeting on the quad (any morning).
        {"id": "grace_favor_debate", "label": "grace_favor_debate", "kind": "favor", "route": "grace",
         "location": "quad", "chars": [], "slots": ["morning"], "favor_step": {"grace": 0}, "once": False},
        # Favor step 2: report back to her.
        {"id": "grace_favor_report", "label": "grace_favor_report", "kind": "favor", "route": "grace",
         "location": "council_office", "chars": ["grace"], "favor_step": {"grace": 1}, "once": False},
        {"id": "grace_bonus_date", "label": "grace_bonus_date", "kind": "bonus", "route": "grace",
         "location": "council_office", "chars": ["grace"], "slots": ["evening"],
         "min_affection": {"grace": 75}},
        {"id": "grace_confession", "label": "grace_confession", "kind": "story", "route": "grace",
         "location": "council_office", "chars": ["grace"], "slots": ["evening"],
         "min_affection": {"grace": 90}, "requires_flags": ["grace.bonus_date_done"]},
    ]

    # ---------------------------------------------------------------------
    # Other routes: generic placeholder hangouts until M3.
    # ---------------------------------------------------------------------
    for _cid, _locs in {
        "xenia":   ["cafeteria", "observatory_roof"],
        "claudia": ["quad", "claudia_library"],
        "gemma":   ["robotics_lab"],
        "shen":    ["library_3f", "robotics_lab"],
    }.items():
        for _loc in _locs:
            EVENTS.append({
                "id": "hangout_%s_%s" % (_cid, _loc),
                "label": "generic_hangout",
                "args": [_cid],
                "kind": "hangout",
                "location": _loc,
                "chars": [_cid],
            })

    for _cid, _loc in [("xenia", "observatory_roof"), ("claudia", "claudia_library"),
                       ("gemma", "robotics_lab"), ("shen", "library_3f")]:
        EVENTS.append({
            "id": "favor_%s" % _cid,
            "label": "generic_favor_step",
            "args": [_cid],
            "kind": "favor",
            "location": _loc,
            "chars": [_cid],
            "favor_status": {_cid: "active"},
            "once": False,
        })

    EVENTS.append({
        "id": "group_lab_partners",
        "label": "group_lab_partners",
        "args": [],
        "kind": "group",
        "location": "robotics_lab",
        "chars": ["gemma", "shen"],
        "slots": ["morning"],
        "day_min": 4,
    })
