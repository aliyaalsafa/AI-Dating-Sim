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

image bg quad = placeholder_bg("Main Quad", "#ffe3f0")

image grace placeholder = placeholder_sprite("grace")
image xenia placeholder = placeholder_sprite("xenia")
image claudia placeholder = placeholder_sprite("claudia")
image gemma placeholder = placeholder_sprite("gemma")
image shen placeholder = placeholder_sprite("shen")
