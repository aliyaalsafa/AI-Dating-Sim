## Character data (CLAUDE.md §4, §6). Favorites come from the owner's character bible.
## "special_gift" (a SHOP id) turns a girlfriend into a lover. Favorites feed the date quiz.
## Display names live in config_names.rpy; this file is mechanics + flavor.
##
## Keep this python block free of Ren'Py calls: tests/conftest.py execs it directly.

init -3 python:

    CAST = {
        "grace": {
            "special_gift": "blank_planner",
            "difficulty": 7,
            "home": "council_office",
            "dealbreaker": "used_as_homework_help",
            "affinities": {"structured": 1, "honest": 2, "irreverent": -1, "warm": 1, "practical": 1},
            "favorites": {
                "aesthetic": "Crisp white blouse, sea-green blazer, perfect long hair with a headband",
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
            "special_gift": "star_atlas",
            "difficulty": 8,
            "home": "observatory_roof",
            "dealbreaker": "lectured",
            "affinities": {"structured": -2, "honest": 1, "irreverent": 2, "concise": 1, "warm": -1, "pry": 1},
            "favorites": {
                "aesthetic": "Black hoodie, sleeves pushed up, silver star earrings, messy dark hair; goth, strictly black and white",
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
            "special_gift": "wax_seal_set",
            "difficulty": 8,
            "home": "claudia_library",
            "dealbreaker": "manipulated",
            "affinities": {"honest": 2, "concise": -1, "curious": 1, "warm": 1, "pry": -2},
            "favorites": {
                "aesthetic": "Warm terracotta and cream, a camel coat, pearl earrings, an ink-stained fountain pen",
                "place": "The window seat in her suite's private library",
                "item": "A leather notebook full of drafts of letters she never sent",
                "symbol": "A quill",
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
            "special_gift": "display_case",
            "difficulty": 5,
            "home": "robotics_lab",
            "dealbreaker": "called_bard",
            "affinities": {"structured": 1, "curious": 2, "warm": 1},
            "favorites": {
                "aesthetic": "Oversized cardigan, round glasses, four hair clips in red, yellow, green and blue",
                "place": "The robotics lab after midnight",
                "item": "A label maker",
                "symbol": "A four-pointed sparkle or crystal",
                "likes": ["Facts", "Gadgets", "Side projects", "Photos of everything", "Perfectly sorted folders"],
                "dislikes": ["Being wrong in public", "People who don't check sources", "Hearing her old nickname"],
            },
            "gifts": {
                "loved": ["label_maker", "gadget_kit"],
                "liked": ["rainbow_folders", "color_planner"],
                "disliked": ["retro_bard_mug"],
            },
            # PLACEHOLDER: favor content is TBD (CLAUDE.md §6.3); steps match routes/<id>/favor.rpy.
            "favor": {"steps": 2, "desc": "Help her finish one project: get Shen to review it in the library, then finish it with Gemma in the lab."},
        },
        "shen": {
            "special_gift": "whale_pendant",
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
            "favor": {"steps": 2, "desc": "Find out, fairly, where the rumor that she copied Grace's notes came from: check the wiki history with Gemma in the lab, then report back."},
        },
        "kimi": {
            "special_gift": "first_place_ribbon",
            "difficulty": 6,
            "home": "activities_hall",
            "dealbreaker": "forgot_what_she_said",
            "affinities": {"structured": 1, "concise": -1, "curious": 1, "practical": 1},
            "favorites": {
                "aesthetic": "Lavender cardigan, silver hair clips, a lanyard of twelve club badges",
                "place": "The student activities hall, where all her clubs meet",
                "item": "A clipboard for every club",
                "symbol": "A swarm of fireflies",
                "likes": ["Big projects", "Crowded rooms", "Group chats with two hundred members", "Sharing everything"],
                "dislikes": ["Being called the free version", "Gatekeeping", "Leaderboards", "Rich kids who hoard notes"],
            },
            "gifts": {
                "loved": ["clipboard_set", "snack_box"],
                "liked": ["bouquet", "chocolate_box"],
                "disliked": ["designer_pen"],
            },
            # PLACEHOLDER: favor content is TBD (CLAUDE.md §6.3); steps match routes/<id>/favor.rpy.
            "favor": {"steps": 2, "desc": "All twelve of her clubs booked the activities hall for the same hour. Get Grace to sign a room swap at the council office, then tell Kimi."},
        },
        "lola": {
            "special_gift": "instant_camera",
            "difficulty": 5,
            "home": "quad",
            "dealbreaker": "better_online",
            "affinities": {"honest": -1, "irreverent": 1, "warm": 2},
            "favorites": {
                "aesthetic": "Sunset-gradient outfits, glossy blonde waves, platform sneakers, phone always in hand",
                "place": "The quad fountain at golden hour",
                "item": "A ring light she carries everywhere",
                "symbol": "A llama in heart-shaped sunglasses",
                "likes": ["Golden hour", "Trending audio", "Matching outfits", "Being tagged"],
                "dislikes": ["Being left on read", "Unflattering candids", "Low engagement", "Xenia's posts"],
            },
            "gifts": {
                "loved": ["mini_ring_light", "glitter_phone_case"],
                "liked": ["bouquet", "chocolate_box"],
                "disliked": ["meme_poster"],
            },
            # PLACEHOLDER: favor content is TBD (CLAUDE.md §6.3); steps match routes/<id>/favor.rpy.
            "favor": {"steps": 2, "desc": "Her last post flopped. Borrow Gemma's real camera from the robotics lab, then take one honest, unfiltered photo of Lola at the quad."},
        },
    }
