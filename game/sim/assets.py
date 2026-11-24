"""Art and audio swap points (CLAUDE.md §8 M5).

Real assets are picked up by file name, so adding art or music means dropping
a file into the right folder, with no code changes:

    game/images/bg/<name>.(png|jpg|jpeg|webp)          -> image "bg <name>"
    game/images/sprites/<char>_<expression>.(png|webp) -> image "<char> <expression>"
    game/audio/music/<key>.(ogg|opus|mp3)              -> music track <key>
    game/audio/sfx/<key>.(ogg|opus|mp3|wav)            -> sound effect <key>

Anything missing falls back to placeholder art or silence. Paths are relative
to game/, the way Ren'Py's renpy.list_files() reports them.
"""

import re

IMAGE_EXTS = ("webp", "png", "jpg", "jpeg")   # earlier wins if several exist
AUDIO_EXTS = ("ogg", "opus", "mp3", "wav")

_BG_RE = re.compile(r"^images/bg/([a-z0-9_]+)\.([a-z0-9]+)$")
_SPRITE_RE = re.compile(r"^images/sprites/([a-z0-9]+)_([a-z0-9_]+)\.([a-z0-9]+)$")


def _audio_re(folder):
    return re.compile(r"^audio/%s/([a-z0-9_]+)\.([a-z0-9]+)$" % folder)


def _pick(found, key, ext, exts, path):
    """Keep the path with the most preferred extension for each key."""
    if ext not in exts:
        return
    old = found.get(key)
    if old is None or exts.index(ext) < exts.index(old[0]):
        found[key] = (ext, path)


def _norm(files):
    for f in files:
        yield f.replace("\\", "/"), f.replace("\\", "/").lower()


def find_backgrounds(files) -> dict:
    """{bg name: path} for every real background file."""
    found = {}
    for path, low in _norm(files):
        m = _BG_RE.match(low)
        if m:
            _pick(found, m.group(1), m.group(2), IMAGE_EXTS, path)
    return {k: v[1] for k, v in found.items()}


def find_sprites(files, cast_ids) -> dict:
    """{(char_id, expression): path} for every real sprite of a known character."""
    cast_ids = set(cast_ids)
    found = {}
    for path, low in _norm(files):
        m = _SPRITE_RE.match(low)
        if m and m.group(1) in cast_ids:
            _pick(found, (m.group(1), m.group(2)), m.group(3), IMAGE_EXTS, path)
    return {k: v[1] for k, v in found.items()}


def find_audio(files, folder) -> dict:
    """{key: path} for audio/<folder>/<key>.<ext>."""
    rx = _audio_re(folder)
    found = {}
    for path, low in _norm(files):
        m = rx.match(low)
        if m:
            _pick(found, m.group(1), m.group(2), AUDIO_EXTS, path)
    return {k: v[1] for k, v in found.items()}


def scene_music_key(location_id, slot, event=None, location_music=None, available=()):
    """Which music key should play for a map visit, or None for silence.

    Preference order: the event's route theme ("theme_<char>"), the location's
    own track, then the generic campus track for the time of day.
    """
    available = set(available)
    candidates = []
    if event and event.get("route"):
        candidates.append("theme_" + event["route"])
    if location_music and location_id in location_music:
        candidates.append(location_music[location_id])
    candidates.append("campus_night" if slot == "evening" else "campus_day")
    for key in candidates:
        if key in available:
            return key
    return None
