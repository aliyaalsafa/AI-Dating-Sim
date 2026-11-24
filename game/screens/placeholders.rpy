## Art: real files where they exist, placeholders everywhere else (CLAUDE.md §2, §8 M5).
##
## Swap in real art by dropping files into game/images/ (see game/sim/assets.py
## and ASSETS.md). No code changes needed:
##   images/bg/<name>.png                  -> "bg <name>"  (e.g. bg/council_office.png)
##   images/sprites/<char>_<expression>.png -> "<char> <expression>"  (e.g. sprites/grace_neutral.png)
##
## Every scene shows "<char> neutral", so a `<char>_neutral` file is the first
## sprite to add for each character. Other expressions are optional.

init -1 python:

    def placeholder_bg(label, color="#ffd6e8", text_color="#3a164099"):
        """Location color + soft light/hearts overlay + the place name on a pill."""
        return Fixed(
            Solid(color),
            "gui/theme/bg_overlay.png",
            Window(
                Text(label, size=52, color="#ffffff", outlines=OUTLINE_MED, xalign=0.5),
                background=ui_pill("plum"), padding=(48, 10, 48, 16),
                xalign=0.5, yalign=0.11, style="empty",
            ),
        )

    def placeholder_sprite(char_id):
        """Silhouette tinted in the character's color, with her name chip."""
        c = SIGNATURE_COLORS[char_id]
        return Fixed(
            Transform("gui/theme/silhouette.png", matrixcolor=TintMatrix(c["fill"])),
            Transform("gui/theme/silhouette.png", matrixcolor=TintMatrix(c["accent"]) * OpacityMatrix(0.18),
                      crop=(0, 0, 440, 330)),
            Window(
                Text(CAST_NAMES[char_id]["name"], size=40, color="#ffffff", outlines=OUTLINE_SMALL),
                background=namebox_bg(char_id), padding=(30, 6, 30, 10),
                xalign=0.5, yalign=0.62, style="empty",
            ),
            xysize=(440, 860),
        )

    # Story-only backgrounds (map locations come from LOCATIONS).
    STORY_BGS = {
        "gates": ("Academy Gates", "#e9e1f7", "#3a164099"),
        "dorm":  ("Your Dorm Room", "#f7efe4", "#3a164099"),
        "gala":  ("The Founders' Gala", "#2a1830", "#fff6fb99"),
    }


init 1 python:
    from sim import assets as sim_assets

    _files = renpy.list_files()
    REAL_BGS = sim_assets.find_backgrounds(_files)
    REAL_SPRITES = sim_assets.find_sprites(_files, CAST.keys())

    def _bg_placeholder(name):
        if name in LOCATIONS:
            return location_bg(name)
        label_, color, ink = STORY_BGS[name]
        return placeholder_bg(label_, color, ink)

    for _name in list(LOCATIONS) + list(STORY_BGS):
        renpy.image(("bg", _name), REAL_BGS.get(_name) or _bg_placeholder(_name))
    for _name, _path in REAL_BGS.items():          # extra backgrounds with no placeholder
        if _name not in LOCATIONS and _name not in STORY_BGS:
            renpy.image(("bg", _name), _path)

    for _cid in CAST:
        renpy.image((_cid, "neutral"), REAL_SPRITES.get((_cid, "neutral")) or placeholder_sprite(_cid))
    for (_cid, _expr), _path in REAL_SPRITES.items():
        if _expr != "neutral":
            renpy.image((_cid, _expr), _path)
