"""Art and audio swap points (game/sim/assets.py)."""

from sim.assets import find_audio, find_backgrounds, find_sprites, scene_music_key

FILES = [
    "images/bg/council_office.png",
    "images/bg/council_office.webp",       # preferred over png
    "images/bg/Gala.JPG",                  # case-insensitive match
    "images/bg/notes.txt",                 # ignored: not an image
    "images/sprites/grace_neutral.png",
    "images/sprites/grace_happy.png",
    "images/sprites/nobody_neutral.png",   # ignored: not in the cast
    "images/gui_thing.png",                # ignored: wrong folder
    "audio/music/campus_day.mp3",
    "audio/music/campus_day.ogg",          # preferred over mp3
    "audio/music/theme_grace.opus",
    "audio/sfx/achievement.wav",
    "audio\\sfx\\phone.ogg",               # Windows separators
]


def test_backgrounds():
    assert find_backgrounds(FILES) == {
        "council_office": "images/bg/council_office.webp",
        "gala": "images/bg/Gala.JPG",
    }


def test_sprites():
    assert find_sprites(FILES, ["grace", "shen"]) == {
        ("grace", "neutral"): "images/sprites/grace_neutral.png",
        ("grace", "happy"): "images/sprites/grace_happy.png",
    }


def test_audio():
    assert find_audio(FILES, "music") == {
        "campus_day": "audio/music/campus_day.ogg",
        "theme_grace": "audio/music/theme_grace.opus",
    }
    assert find_audio(FILES, "sfx") == {"achievement": "audio/sfx/achievement.wav", "phone": "audio/sfx/phone.ogg"}


def test_no_files_means_placeholders_and_silence():
    assert find_backgrounds([]) == {} and find_sprites([], ["grace"]) == {} and find_audio([], "music") == {}
    assert scene_music_key("quad", "morning", available=()) is None


def test_scene_music_preference_order():
    loc_music = {"observatory_roof": "roof"}
    ev = {"route": "xenia"}
    every = {"theme_xenia", "roof", "campus_day", "campus_night"}
    assert scene_music_key("observatory_roof", "evening", ev, loc_music, every) == "theme_xenia"
    assert scene_music_key("observatory_roof", "evening", ev, loc_music, every - {"theme_xenia"}) == "roof"
    assert scene_music_key("observatory_roof", "evening", ev, loc_music, {"campus_night"}) == "campus_night"
    assert scene_music_key("quad", "morning", None, loc_music, every) == "campus_day"
    assert scene_music_key(None, "afternoon", {"id": "day01_lunch"}, loc_music, every) == "campus_day"


def test_audio_data_is_consistent(data):
    music, sfx = data["MUSIC_KEYS"], data["SFX_KEYS"]
    assert set(data["LOCATION_MUSIC"].values()) <= set(music)
    assert set(data["LOCATION_MUSIC"]) <= set(data["LOCATIONS"])
    assert set(data["ENDING_MUSIC"].values()) <= set(music)
    for cid in data["CAST"]:
        assert "theme_" + cid in music
    assert {"campus_day", "campus_night", "title", "gala"} <= set(music)
    assert {"affection_up", "affection_down", "achievement"} <= set(sfx)


def test_every_requested_key_is_documented(data):
    """Keys passed to music()/sfx() in scripts must be listed in data/audio.rpy."""
    import pathlib
    import re
    game = pathlib.Path(__file__).parent.parent / "game"
    text = "\n".join(p.read_text(encoding="utf-8") for p in game.rglob("*.rpy"))
    for key in re.findall(r'\bmusic\("([a-z_]+)"\)', text):
        assert key in data["MUSIC_KEYS"], key
    for key in re.findall(r'\bsfx\(\s*"([a-z_]+)"', text) + re.findall(r'Function\(sfx, "([a-z_]+)"\)', text):
        assert key in data["SFX_KEYS"], key
