## Ending registry (CLAUDE.md §7). Conditions live in game/sim/endings.py;
## this maps each EndingId to a title and the label that plays it.
## Keep the python block free of Ren'Py calls: tests can exec it.

init -3 python:

    ENDINGS = {
        "solo":   {"title": "Party of One",          "label": "ending_placeholder"},
        "rivals": {"title": "Rivals Take the Floor", "label": "ending_placeholder"},
    }
    for _cid in ["grace", "xenia", "claudia", "gemma", "shen"]:
        for _kind, _title in [("good", "Good Ending"), ("sweet", "Sweet Ending"), ("friends", "Friends Ending")]:
            ENDINGS["%s_%s" % (_kind, _cid)] = {
                "title": _title,
                "char": _cid,
                "label": "ending_placeholder",   # replaced per route below as routes land
            }

    # Routes with written endings (M2: Grace).
    for _cid in ["grace"]:
        for _kind in ["good", "sweet", "friends"]:
            ENDINGS["%s_%s" % (_kind, _cid)]["label"] = "ending_%s_%s" % (_kind, _cid)
