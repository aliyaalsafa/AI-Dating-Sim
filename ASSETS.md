# Adding art and audio

The game runs on placeholder art and no sound. Real assets are picked up by
**file name**: drop a file in the right folder and it replaces the placeholder
the next time the game starts. No code changes are needed. The matching rules
live in [game/sim/assets.py](game/sim/assets.py). Record every third-party
file and its license in [CREDITS.md](CREDITS.md).

File names are lowercase letters, digits and underscores. If the same name exists
in several formats, the first one in each list below wins.

## Backgrounds

`game/images/bg/<name>.webp|png|jpg` becomes `bg <name>`. Size: 1920×1080.

| name | where |
| --- | --- |
| `quad`, `council_office`, `robotics_lab`, `library_3f`, `claudia_library`, `cafeteria`, `observatory_roof`, `campus_store` | Map locations (ids from `game/data/locations.rpy`) |
| `gates` | Prologue |
| `dorm` | Day 1 evening |
| `gala` | Founders' Gala and endings |

## Character sprites

`game/images/sprites/<char>_<expression>.webp|png` becomes `<char> <expression>`.
Characters are `grace`, `xenia`, `claudia`, `gemma` and `shen`.

Every scene currently uses the **`neutral`** expression, so `grace_neutral.png`
and so on are the first five files to add. Sprites are bottom-aligned; the
placeholders are 440×860, but real sprites can be any height up to 1080.
Add more expressions (`grace_happy.png`) and use them in scenes with
`show grace happy`.

## Music

`game/audio/music/<key>.ogg|opus|mp3` loops while that key is active. When a key
has no file, the music stops instead of carrying over the wrong track. All keys
and where they play are listed in [game/data/audio.rpy](game/data/audio.rpy):

- `title`: main menu
- `campus_day`, `campus_night`: map visits, by time of day
- `roof`, `shop`, `library`: location overrides (optional)
- `theme_<char>`: plays during that character's route scenes (optional)
- `dorm`, `gala`
- `ending_good`, `ending_sweet`, `ending_bittersweet`

For a map visit, the game uses the first key in this list that has a file: the character theme, then the location track, then the campus track.

## Sound effects

`game/audio/sfx/<key>.ogg|opus|mp3|wav`:
`affection_up`, `affection_down`, `achievement`, `phone`, `choice`, `click`, `new_day`.

## Web build notes

Use `.ogg` or `.opus` for audio. They play in every current browser, and the web
build streams them. `.mp3` also works. Keep images as `.webp` where possible to
keep the web download small.
