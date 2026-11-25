## Achievements (CLAUDE.md §6.4). Persist across playthroughs.
## Conditions for most of these live in game/sim/achievements.py.
## Keep the python block free of Ren'Py calls: tests can exec it.
## Registration with Ren'Py's achievement system happens in sim_bridge.rpy.

init -3 python:

    # Order here is display order on the phone. "secret" hides the description until earned.
    ACHIEVEMENTS = {
        "first_day":         {"name": "Orientation",           "desc": "Survive your first day at the Academy."},
        "all_met":           {"name": "Full Roster",           "desc": "Meet all seven of them."},
        "first_gift":        {"name": "Thoughtful",            "desc": "Give someone a gift."},
        "loved_gift":        {"name": "Nailed It",             "desc": "Give someone a gift she loves."},
        "opened_up":         {"name": "Past the Small Talk",   "desc": "Get someone to open up to you."},
        "open_book":         {"name": "Open Book",             "desc": "Get all seven to open up in one semester."},
        "first_favor":       {"name": "Favor Granted",         "desc": "Finish someone's favor."},
        "all_favors":        {"name": "Campus Fixer",          "desc": "Finish all seven favors in one semester."},
        "first_girlfriend":  {"name": "It's Official",         "desc": "Pass a date and become someone's girlfriend."},
        "first_lover":       {"name": "Special Delivery",      "desc": "Give a girlfriend her special gift."},
        "hit_a_nerve":       {"name": "Hit a Nerve",           "desc": "Find someone's deal-breaker the hard way.", "secret": True},
        "friend_zoned":      {"name": "Strictly Platonic",     "desc": "Lock yourself out of a romance.", "secret": True},
        "first_clue":        {"name": "Case Opened",           "desc": "Overhear your first hint."},
        "prompt_engineer":   {"name": "Prompt Engineer",       "desc": "Get a major clue with a well-crafted question."},
        "jailbreak":         {"name": "Jailbreak",             "desc": "Force a major clue out of someone.", "secret": True},
        "truth_known":       {"name": "Whole Life a Lie",      "desc": "Find out what you really are.", "secret": True},
        "first_ending":      {"name": "Gala Night",            "desc": "Reach any ending."},
        "unfinished_ending": {"name": "Keep Dancing",          "desc": "Reach the gala without knowing the truth."},
        "complete_ending":   {"name": "Heartthrob",            "desc": "Tell the truth with all seven as your lovers.", "secret": True},
        "exiled_ending":     {"name": "Expelled",              "desc": "Tell the truth with no one on your side.", "secret": True},
        "lie_ending":        {"name": "Passing",               "desc": "Know the truth and say nothing.", "secret": True},
        "all_mono":          {"name": "Every One of Them",     "desc": "See all seven Monogamous endings."},
        "completionist":     {"name": "Valedictorian",         "desc": "See every ending."},
    }
