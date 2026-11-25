## Ending registry (CLAUDE.md §7). Conditions live in game/sim/endings.py;
## this maps each EndingId to a title, the label that plays it, and how the
## endings gallery shows it. Keep the python block free of Ren'Py calls: tests can exec it.

init -3 python:

    ENDINGS = {
        "complete":       {"title": "Complete",              "label": "ending_complete",       "secret": True},
        "good_truth":     {"title": "Good Truth",            "label": "ending_good_truth",     "secret": False},
        "bad_truth":      {"title": "Bad Truth",             "label": "ending_bad_truth",      "secret": False},
        "exiled":         {"title": "Exiled",                "label": "ending_exiled",         "secret": False},
        "lie":            {"title": "The Lie",               "label": "ending_lie",            "secret": True},
        "unfinished":     {"title": "Unfinished",            "label": "ending_unfinished",     "secret": False},
        # Layer 2 (Ada). Not reachable until she's built (CLAUDE.md §8 R5).
        "true_final":     {"title": "True Final Ending",     "label": "ending_true_final",     "secret": True},
        "lie_ada":        {"title": "The Lie, with Her",     "label": "ending_lie_ada",        "secret": True},
        "unfinished_two": {"title": "Unfinished II",         "label": "ending_unfinished_two", "secret": True},
    }
    # Gallery order for the non-character endings.
    MAIN_ENDINGS = ["complete", "good_truth", "bad_truth", "exiled", "lie", "unfinished", "true_final", "lie_ada", "unfinished_two"]

    for _cid in ["grace", "xenia", "claudia", "gemma", "shen", "kimi", "lola"]:
        ENDINGS["mono_" + _cid] = {
            "title": "Monogamous",
            "char": _cid,
            "kind": "mono",
            "label": "ending_mono_" + _cid,
            "secret": False,
        }
