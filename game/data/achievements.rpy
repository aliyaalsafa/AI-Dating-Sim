## Achievements (CLAUDE.md §6.5). Persist across playthroughs.
## Keep the python block free of Ren'Py calls: tests can exec it.

init -3 python:

    ACHIEVEMENTS = {
        "first_day":   {"name": "Orientation",      "desc": "Survive your first day at the Academy."},
        "first_gift":  {"name": "Thoughtful",       "desc": "Give someone a gift."},
        "loved_gift":  {"name": "Nailed It",        "desc": "Give someone a gift she loves."},
        "first_favor": {"name": "Favor Granted",    "desc": "Finish someone's favor."},
        "all_met":     {"name": "Full Roster",      "desc": "Meet all five of them."},
    }

init python:
    for _aid in ACHIEVEMENTS:
        achievement.register(_aid)
