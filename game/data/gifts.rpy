## Campus store stock (CLAUDE.md §6.3). Who loves/hates what is in cast.rpy.
## "special": True marks a girl's special gift (cast.rpy "special_gift"); it turns a girlfriend into a lover.
## Keep this python block free of Ren'Py calls: tests/conftest.py execs it directly.

init -3 python:

    SHOP = {
        "gold_star_stickers":  {"name": "Gold star stickers",      "price": 5},
        "color_planner":       {"name": "Color-coded planner",     "price": 15},
        "rainbow_folders":     {"name": "Four-color folder set",   "price": 8},
        "telescope_lens":      {"name": "Telescope lens",          "price": 30},
        "rocket_model":        {"name": "Model rocket kit",        "price": 20},
        "meme_poster":         {"name": "Deep-fried meme poster",  "price": 6},
        "poetry_book":         {"name": "Slim book of poetry",     "price": 12},
        "fountain_pen_ink":    {"name": "Bottle of fountain-pen ink", "price": 10},
        "tea_tin":             {"name": "Tin of loose-leaf tea",   "price": 9},
        "label_maker":         {"name": "Label maker",             "price": 25},
        "gadget_kit":          {"name": "Pocket gadget kit",       "price": 18},
        "street_food_voucher": {"name": "Street-food voucher",     "price": 7},
        "laptop_stickers":     {"name": "Laptop sticker pack",     "price": 4},
        "whale_keychain":      {"name": "Whale keychain",          "price": 5},
        "instant_noodles":     {"name": "Instant noodles (6-pack)", "price": 4},
        "bouquet":             {"name": "Bouquet of flowers",      "price": 12},
        "chocolate_box":       {"name": "Box of chocolates",       "price": 10},
        "rubber_duck":         {"name": "Rubber duck",             "price": 3},
        "mystery_box":         {"name": "Mystery box",             "price": 10},
        "school_spirit_scarf": {"name": "School-spirit scarf",     "price": 10},
        "gossip_magazine":     {"name": "Gossip magazine",         "price": 3},
        "retro_bard_mug":      {"name": "Retro 'Bard' mug",        "price": 6},
        "designer_pen":        {"name": "Designer pen",            "price": 28},
        "clipboard_set":       {"name": "Set of twelve clipboards", "price": 9},
        "snack_box":           {"name": "Snack box for thirty",    "price": 15},
        "mini_ring_light":     {"name": "Mini ring light",         "price": 20},
        "glitter_phone_case":  {"name": "Glitter phone case",      "price": 12},

        # Special gifts (one per girl). PLACEHOLDER names and prices.
        "blank_planner":       {"name": "A planner with every page left blank", "price": 40, "special": True},
        "star_atlas":          {"name": "A hand-bound star atlas",  "price": 40, "special": True},
        "wax_seal_set":        {"name": "Wax seal and stationery set", "price": 40, "special": True},
        "display_case":        {"name": "Display case for one finished project", "price": 40, "special": True},
        "whale_pendant":       {"name": "Silver whale pendant",     "price": 40, "special": True},
        "first_place_ribbon":  {"name": "A blue ribbon that says 1st", "price": 40, "special": True},
        "instant_camera":      {"name": "Instant camera (no filters)", "price": 40, "special": True},
    }
