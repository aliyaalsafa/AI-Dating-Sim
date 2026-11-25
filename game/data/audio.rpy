## Audio swap points (CLAUDE.md §8 M5). The game ships silent; every key here
## starts playing as soon as a matching file exists:
##   game/audio/music/<key>.ogg   (or .opus / .mp3)
##   game/audio/sfx/<key>.ogg     (or .opus / .mp3 / .wav)
## See ASSETS.md. Keep the python block free of Ren'Py calls: tests can exec it.

init -3 python:

    # Music keys the game asks for, and where.
    MUSIC_KEYS = {
        "title":         "Main menu.",
        "campus_day":    "Map visits in the morning and afternoon (default).",
        "campus_night":  "Map visits in the evening (default).",
        "dorm":          "Day 1 dorm scene and quiet moments.",
        "gala":          "Founders' Gala lead-in and invitation.",
        "ending_good":   "Complete, Good Truth and True Final endings.",
        "ending_sweet":  "Monogamous and Unfinished endings.",
        "ending_bittersweet": "Bad Truth, Exiled, The Lie and Unfinished II.",
        "theme_grace":   "Plays during Grace's route scenes (optional).",
        "theme_xenia":   "Plays during Xenia's route scenes (optional).",
        "theme_claudia": "Plays during Claudia's route scenes (optional).",
        "theme_gemma":   "Plays during Gemma's route scenes (optional).",
        "theme_shen":    "Plays during Shen's route scenes (optional).",
        "theme_kimi":    "Plays during Kimi's route scenes (optional).",
        "theme_lola":    "Plays during Lola's route scenes (optional).",
    }

    # Per-location tracks; anything not listed uses campus_day / campus_night.
    LOCATION_MUSIC = {
        "observatory_roof": "roof",
        "campus_store": "shop",
        "library_3f": "library",
    }
    MUSIC_KEYS.update({
        "roof":    "Observatory roof (optional).",
        "shop":    "Campus store (optional).",
        "library": "24-hour library (optional).",
    })

    SFX_KEYS = {
        "affection_up":   "Affection goes up.",
        "affection_down": "Affection goes down.",
        "achievement":    "Achievement unlocked.",
        "phone":          "Phone opens.",
        "choice":         "A dialogue choice is picked.",
        "click":          "Menu and map buttons.",
        "new_day":        "A new day starts.",
    }

    # Which ending music key each ending kind uses.
    ENDING_MUSIC = {"complete": "ending_good", "true_final": "ending_good", "good_truth": "ending_good",
                    "mono": "ending_sweet", "bad_truth": "ending_bittersweet", "exiled": "ending_bittersweet",
                    "lie": "ending_bittersweet", "lie_ada": "ending_bittersweet",
                    "unfinished": "ending_sweet", "unfinished_two": "ending_bittersweet"}
