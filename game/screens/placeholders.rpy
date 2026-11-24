## Placeholder art so the game is fully playable before real art exists.
##   - Backgrounds: a solid color with the location name.
##   - Sprites: a signature-color silhouette card with the character's name.
##
## To swap in real art later, define an image with the same name
## (e.g. `image bg council_office = "bg/council_office.png"`) and delete the
## placeholder line.

init -1 python:

    def placeholder_bg(label, color="#ffd6e8", text_color="#3a164099"):
        return Fixed(
            Solid(color),
            Text(label, size=64, color=text_color, bold=True, xalign=0.5, yalign=0.12),
        )

    def placeholder_sprite(char_id):
        c = SIGNATURE_COLORS[char_id]
        return Fixed(
            Solid(c["fill"], xysize=(440, 860)),
            Solid(c["accent"], xysize=(440, 14), yalign=0.0),
            Text(CAST_NAMES[char_id]["name"], size=56, color=c["accent"], bold=True,
                 xalign=0.5, yalign=0.5),
            xysize=(440, 860),
        )



image grace placeholder = placeholder_sprite("grace")
image xenia placeholder = placeholder_sprite("xenia")
image claudia placeholder = placeholder_sprite("claudia")
image gemma placeholder = placeholder_sprite("gemma")
image shen placeholder = placeholder_sprite("shen")

## One placeholder background per map location ("bg <location_id>"), plus
## a few story-only places. Replace any of them with real art by defining the
## same image name in a file that loads later.
init 1 python:
    for _lid in LOCATIONS:
        renpy.image(("bg", _lid), location_bg(_lid))

image bg gates = placeholder_bg("Academy Gates", "#e9e1f7")
image bg dorm = placeholder_bg("Your Dorm Room", "#f7efe4")
image bg gala = placeholder_bg("The Founders' Gala", "#2a1830", "#fff6fb99")
