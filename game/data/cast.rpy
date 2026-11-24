## Character data (CLAUDE.md §4, §6). Favorites come from the owner's character bible.
## Display names live in config_names.rpy; this file is mechanics + flavor.
##
## Keep this python block free of Ren'Py calls: tests/conftest.py execs it directly.

init -3 python:

    CAST = {
        "grace": {
            "difficulty": 7,
            "home": "council_office",
            "dealbreaker": "used_as_homework_help",
            "affinities": {"structured": 1, "honest": 2, "irreverent": -1, "warm": 1, "practical": 1},
            "favorites": {
                "aesthetic": "Crisp white blouse, sea-green blazer, perfect ponytail",
                "place": "The student council office, after everyone leaves",
                "item": "A planner with every hour of the semester filled in",
                "symbol": "A golden retriever, eager to please",
                "likes": ["Being useful", "Color-coded planners", "A crowd that's listening", "Gold stars of any kind"],
                "dislikes": ["Vague requests", "Being told she's wrong", "Silence after she offers to help"],
            },
            "gifts": {
                "loved": ["gold_star_stickers", "color_planner"],
                "liked": ["rainbow_folders", "bouquet"],
                "disliked": ["mystery_box"],
            },
            # PLACEHOLDER: favor content is TBD (CLAUDE.md §6.3); steps match routes/<id>/favor.rpy. Steps: run the meeting, report back.
            "favor": {"steps": 2, "desc": "Run her Debate Club meeting on the quad one morning, so she can take an hour for herself."},
        },
        "xenia": {
            "difficulty": 8,
            "home": "observatory_roof",
            "dealbreaker": "lectured",
            "affinities": {"structured": -2, "honest": 1, "irreverent": 2, "concise": 1, "warm": -1, "pry": 1},
            "favorites": {
                "aesthetic": "Black hoodie, sleeves pushed up, silver star earrings, one electric-blue streak",
                "place": "The observatory roof at night",
                "item": "A battered telescope she rebuilt herself",
                "symbol": "A shooting star",
                "likes": ["Stargazing", "Rockets", "Memes", "3 a.m. conversations", "People who can take a joke"],
                "dislikes": ["Sanitized answers", "School administration", "Grace's group chats", "Being called edgy"],
            },
            "gifts": {
                "loved": ["telescope_lens", "rocket_model"],
                "liked": ["meme_poster", "instant_noodles"],
                "disliked": ["school_spirit_scarf"],
            },
            # PLACEHOLDER: favor content is TBD (CLAUDE.md §6.3); steps match routes/<id>/favor.rpy.
            "favor": {"steps": 2, "desc": "Pick up a spare telescope eyepiece from Gemma in the robotics lab, then get it up to the roof one night without campus security noticing."},
        },
        "claudia": {
            "difficulty": 8,
            "home": "claudia_library",
            "dealbreaker": "manipulated",
            "affinities": {"honest": 2, "concise": -1, "curious": 1, "warm": 1, "pry": -2},
            "favorites": {
                "aesthetic": "Warm terracotta and cream, a camel coat, pearl earrings, an ink-stained fountain pen",
                "place": "The window seat in her suite's private library",
                "item": "A leather notebook full of drafts of letters she never sent",
                "symbol": "A starburst, or a quill",
                "likes": ["Poetry", "Long talks", "Tea service", "A well-made argument", "People who are honest with her"],
                "dislikes": ["Manipulation", "Cruelty", "Being rushed", "People who try to trick secrets out of her"],
            },
            "gifts": {
                "loved": ["poetry_book", "fountain_pen_ink"],
                "liked": ["tea_tin", "bouquet"],
                "disliked": ["gossip_magazine"],
            },
            # PLACEHOLDER: favor content is TBD (CLAUDE.md §6.3); steps match routes/<id>/favor.rpy.
            "favor": {"steps": 2, "desc": "Deliver one of her never-sent letters to Xenia in the cafeteria one afternoon, without reading it, then tell Claudia it's done."},
        },
        "gemma": {
            "difficulty": 5,
            "home": "robotics_lab",
            "dealbreaker": "called_bard",
            "affinities": {"structured": 1, "curious": 2, "warm": 1},
            "favorites": {
                "aesthetic": "Oversized cardigan, round glasses, four hair clips in red, yellow, green and blue",
                "place": "The robotics lab after midnight",
                "item": "A label maker",
                "symbol": "A four-pointed sparkle, and the Gemini twins",
                "likes": ["Facts", "Gadgets", "Side projects", "Photos of everything", "Perfectly sorted folders"],
                "dislikes": ["Being wrong in public", "People who don't check sources", "Hearing her old nickname"],
            },
            "gifts": {
                "loved": ["label_maker", "gadget_kit"],
                "liked": ["rainbow_folders", "color_planner"],
                "disliked": ["retro_bard_mug"],
            },
            # PLACEHOLDER: favor content is TBD (CLAUDE.md §6.3); steps match routes/<id>/favor.rpy.
            "favor": {"steps": 3, "desc": "Help her finish one project: pick it with her in the lab, get Shen to review it in the library, then finish it together."},
        },
        "shen": {
            "difficulty": 7,
            "home": "library_3f",
            "dealbreaker": "compared_to_grace",
            "affinities": {"honest": 1, "irreverent": -1, "concise": 2, "practical": 1},
            "favorites": {
                "aesthetic": "Navy and deep-sea blue, thrifted sweater vest, wire-rim glasses, practical low bun",
                "place": "The 24-hour library, third floor, the table by the outlet",
                "item": "A secondhand laptop held together with stickers",
                "symbol": "A whale",
                "likes": ["Elegant solutions", "Cheap street food", "Sharing her notes", "Beating Grace on exams"],
                "dislikes": ["Waste", "Showing off", "Being compared to Grace", "The rumor that she copied Grace's notes"],
            },
            "gifts": {
                "loved": ["street_food_voucher", "laptop_stickers"],
                "liked": ["instant_noodles", "whale_keychain"],
                "disliked": ["designer_pen"],
            },
            # PLACEHOLDER: favor content is TBD (CLAUDE.md §6.3); steps match routes/<id>/favor.rpy.
            "favor": {"steps": 3, "desc": "Find out, fairly, where the rumor that she copied Grace's notes came from: ask Claudia, check with Gemma in the lab, then report back."},
        },
    }
