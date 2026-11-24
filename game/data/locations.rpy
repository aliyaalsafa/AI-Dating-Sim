## Campus map locations and who's where in each time slot (CLAUDE.md §5).
## Keep this python block free of Ren'Py calls: tests/conftest.py execs it directly.
##
## "open": slots the location can be visited (default: all three).
## "schedule": slot -> characters present. Same every day for now (see DECISIONS.md).
## "kind": "shop" makes the location open the gift shop instead of an event.

init -3 python:

    LOCATIONS = {
        "quad": {
            "name": "Main Quad",
            "icon": "✿",
            "color": "#ffe3f0",
            "schedule": {"morning": ["claudia"], "afternoon": [], "evening": []},
        },
        "council_office": {
            "name": "Student Council Office",
            "icon": "★",
            "color": "#d9f2e4",
            "schedule": {"morning": ["grace"], "afternoon": ["grace"], "evening": ["grace"]},
        },
        "robotics_lab": {
            "name": "Robotics Lab",
            "icon": "⬢",
            "color": "#dde8fb",
            "schedule": {"morning": ["gemma", "shen"], "afternoon": ["gemma"], "evening": ["gemma"]},
        },
        "library_3f": {
            "name": "24-Hour Library, 3rd Floor",
            "icon": "✎",
            "color": "#d6deeb",
            "schedule": {"morning": [], "afternoon": ["shen"], "evening": ["shen"]},
        },
        "claudia_library": {
            "name": "Opus Suite Library",
            "icon": "❦",
            "color": "#f6e6d6",
            "schedule": {"morning": [], "afternoon": ["claudia"], "evening": ["claudia"]},
        },
        "cafeteria": {
            "name": "Cafeteria",
            "icon": "❖",
            "color": "#fff1d6",
            "schedule": {"morning": [], "afternoon": ["xenia"], "evening": []},
        },
        "observatory_roof": {
            "name": "Observatory Roof",
            "icon": "✦",
            "color": "#1d2340",
            "text_color": "#cfe6ff",
            "open": ["evening"],
            "schedule": {"evening": ["xenia"]},
        },
        "campus_store": {
            "name": "Campus Store",
            "icon": "❥",
            "color": "#f3e8ff",
            "kind": "shop",
            "schedule": {},
        },
    }
