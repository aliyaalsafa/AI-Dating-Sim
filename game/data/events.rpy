## Event registry (CLAUDE.md §5). Schema: see game/sim/events.py.
## Keep this python block free of Ren'Py calls: tests/conftest.py execs it directly.
##
## "args" are passed to the label: `call expression ev["label"] pass (*ev["args"])`.

init -3 python:

    EVENTS = []

    # Repeatable hangouts: one per character per place she can be found.
    for _cid, _locs in {
        "grace":   ["council_office"],
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

    # Favor follow-up: completes an active favor at her home location.
    for _cid in ["grace", "xenia", "claudia", "gemma", "shen"]:
        EVENTS.append({
            "id": "favor_%s" % _cid,
            "label": "generic_favor_step",
            "args": [_cid],
            "kind": "favor",
            "location": {"grace": "council_office", "xenia": "observatory_roof",
                         "claudia": "claudia_library", "gemma": "robotics_lab",
                         "shen": "library_3f"}[_cid],
            "chars": [_cid],
            "favor_status": {_cid: "active"},
            "once": False,
        })

    # M1 sample group scene (replaced by real content in M2).
    EVENTS.append({
        "id": "group_lab_partners",
        "label": "group_lab_partners",
        "args": [],
        "kind": "group",
        "location": "robotics_lab",
        "chars": ["gemma", "shen"],
        "slots": ["morning"],
        "day_min": 2,
    })
