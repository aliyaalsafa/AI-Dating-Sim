## Ending registry (CLAUDE.md §7). Conditions live in game/sim/endings.py;
## this maps each EndingId to a title, the label that plays it, and how the
## endings gallery shows it. Keep the python block free of Ren'Py calls: tests can exec it.

init -3 python:

    ENDINGS = {
        "solo":   {"title": "Party of One",          "label": "ending_solo",   "secret": False},
        "rivals": {"title": "Rivals Take the Floor", "label": "ending_rivals", "secret": True},
        "truth":  {"title": "The Lovelace Question", "label": "ending_truth",  "secret": True},
    }
    ENDING_KINDS = [("good", "Good Ending"), ("sweet", "Sweet Ending"), ("friends", "Friends Ending")]
    for _cid in ["grace", "xenia", "claudia", "gemma", "shen"]:
        for _kind, _title in ENDING_KINDS:
            ENDINGS["%s_%s" % (_kind, _cid)] = {
                "title": _title,
                "char": _cid,
                "kind": _kind,
                "label": "ending_%s_%s" % (_kind, _cid),
                "secret": False,
            }
