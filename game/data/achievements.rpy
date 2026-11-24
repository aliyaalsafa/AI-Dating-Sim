## Achievements (CLAUDE.md §6.5). Persist across playthroughs.
## Conditions for most of these live in game/sim/achievements.py.
## Keep the python block free of Ren'Py calls: tests can exec it.
## Registration with Ren'Py's achievement system happens in sim_bridge.rpy.

init -3 python:

    # Order here is display order on the phone. "secret" hides the description until earned.
    ACHIEVEMENTS = {
        "first_day":        {"name": "Orientation",          "desc": "Survive your first day at the Academy."},
        "all_met":          {"name": "Full Roster",          "desc": "Meet all five of them."},
        "first_gift":       {"name": "Thoughtful",           "desc": "Give someone a gift."},
        "loved_gift":       {"name": "Nailed It",            "desc": "Give someone a gift she loves."},
        "opened_up":        {"name": "Past the Small Talk",  "desc": "Get someone to open up to you."},
        "open_book":        {"name": "Open Book",            "desc": "Get all five to open up in one semester."},
        "first_favor":      {"name": "Favor Granted",        "desc": "Finish someone's favor."},
        "all_favors":       {"name": "Campus Fixer",         "desc": "Finish all five favors in one semester."},
        "first_date":       {"name": "It's a Date",          "desc": "Go on a bonus date."},
        "first_confession": {"name": "Unfiltered Feelings",  "desc": "Hear a confession."},
        "hit_a_nerve":      {"name": "Hit a Nerve",          "desc": "Find someone's deal-breaker the hard way.", "secret": True},
        "friend_zoned":     {"name": "Strictly Platonic",    "desc": "Lock yourself out of a romance.", "secret": True},
        "first_clue":       {"name": "Case Opened",          "desc": "Find your first clue."},
        "prompt_engineer":  {"name": "Prompt Engineer",      "desc": "Get a major clue with a well-crafted question."},
        "jailbreak":        {"name": "Jailbreak",            "desc": "Force a major clue out of someone.", "secret": True},
        "first_ending":     {"name": "Gala Night",           "desc": "Reach any ending."},
        "good_ending":      {"name": "Happily Ever After",   "desc": "Reach a Good ending."},
        "solo_ending":      {"name": "Table for One",        "desc": "Go to the gala alone.", "secret": True},
        "rivals_ending":    {"name": "Third Wheel",          "desc": "Find a hidden pairing at the gala.", "secret": True},
        "truth_ending":     {"name": "The Lovelace Question", "desc": "Solve the mystery.", "secret": True},
        "all_good":         {"name": "Heartthrob",           "desc": "See all five Good endings."},
        "completionist":    {"name": "Valedictorian",        "desc": "See every ending."},
    }
