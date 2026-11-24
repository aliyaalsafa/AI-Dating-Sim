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
                "label": "ending_placeholder",   # real per-character labels arrive in M2–M4
            }
