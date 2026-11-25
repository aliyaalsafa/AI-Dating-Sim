## Campus map locations and who's where (CLAUDE.md §5).
## Keep this python block free of Ren'Py calls: tests/conftest.py execs it directly.
##
## "open":     slots the location can be visited (default: morning, afternoon, evening).
## "schedule": slot -> characters present. Same every day.
## "meetups":  pair scenes. On the listed days, in that slot, both characters
##             are here instead of where their schedule puts them. The pairs and
##             their hints are in data/mystery.rpy; the scenes in routes/common/pairs/.
## "kind":     "shop" opens the store instead of an event.
##
## Days 1 and 3 (morning) are scripted, so meetups start on day 2. Each pair
## meets on three days so a player who misses one can catch another.

init -3 python:

    LOCATIONS = {
        "council_office": {
            "name": "Student Council Office",
            "icon": "★",
            "color": "#d9f2e4",
            "schedule": {"morning": ["grace"], "afternoon": ["grace"], "evening": ["grace"]},
            "meetups": [
                {"chars": ["grace", "claudia"], "slot": "afternoon", "days": [2, 5, 9]},
            ],
        },
        "claudia_library": {
            "name": "Opus Suite Library",
            "icon": "❦",
            "color": "#f6e6d6",
            "schedule": {"morning": ["claudia"], "afternoon": ["claudia"], "evening": ["claudia"]},
            "meetups": [
                {"chars": ["claudia", "gemma"], "slot": "morning", "days": [4, 7, 11]},
            ],
        },
        "robotics_lab": {
            "name": "Robotics Lab",
            "icon": "⬢",
            "color": "#dde8fb",
            "schedule": {"morning": ["gemma"], "afternoon": ["gemma"], "evening": ["gemma"]},
            "meetups": [
                {"chars": ["gemma", "kimi"], "slot": "afternoon", "days": [3, 7, 11]},
            ],
        },
        "library_3f": {
            "name": "24-Hour Library, 3rd Floor",
            "icon": "✎",
            "color": "#d6deeb",
            "schedule": {"morning": ["shen"], "afternoon": ["shen"], "evening": ["shen"]},
            "meetups": [
                {"chars": ["grace", "shen"], "slot": "evening", "days": [3, 6, 10]},
            ],
        },
        "activities_hall": {
            "name": "Student Activities Hall",
            "icon": "❋",
            "color": "#ece4fb",
            "schedule": {"morning": ["kimi"], "afternoon": ["kimi"], "evening": ["kimi"]},
        },
        "quad": {
            "name": "Main Quad Fountain",
            "icon": "✿",
            "color": "#ffe3f0",
            "schedule": {"morning": ["lola"], "afternoon": ["lola"], "evening": ["lola"]},
            "meetups": [
                {"chars": ["lola", "shen"], "slot": "afternoon", "days": [4, 8, 13]},
            ],
        },
        "cafeteria": {
            "name": "Cafeteria",
            "icon": "❖",
            "color": "#fff1d6",
            "schedule": {"afternoon": ["xenia"]},
            "meetups": [
                {"chars": ["xenia", "lola"], "slot": "afternoon", "days": [5, 9, 12]},
            ],
        },
        "observatory_roof": {
            "name": "Observatory Roof",
            "icon": "✦",
            "color": "#1d2340",
            "text_color": "#cfe6ff",
            "open": ["evening"],
            "schedule": {"evening": ["xenia"]},
            "meetups": [
                {"chars": ["xenia", "kimi"], "slot": "evening", "days": [4, 8, 12]},
            ],
        },
        "campus_store": {
            "name": "Campus Store",
            "icon": "❥",
            "color": "#f3e8ff",
            "kind": "shop",
            "schedule": {},
        },
    }
