## Plays music and sound effects if the files exist (see data/audio.rpy,
## game/sim/assets.py and ASSETS.md). With no audio files the game is silent
## and every call here is a no-op.

init 1 python:
    from sim import assets as sim_assets

    _audio_files = renpy.list_files()
    REAL_MUSIC = sim_assets.find_audio(_audio_files, "music")
    REAL_SFX = sim_assets.find_audio(_audio_files, "sfx")

    if "title" in REAL_MUSIC:
        config.main_menu_music = REAL_MUSIC["title"]
    if "click" in REAL_SFX:
        style.button.activate_sound = REAL_SFX["click"]
    if "choice" in REAL_SFX:
        style.choice_button.activate_sound = REAL_SFX["choice"]

    def music(key, fadein=1.0):
        """Switch to a music key; stops the music if that key has no file."""
        path = REAL_MUSIC.get(key) if key else None
        if path is None:
            renpy.music.stop(channel="music", fadeout=1.0)
        elif renpy.music.get_playing("music") != path:
            renpy.music.play(path, channel="music", loop=True, fadein=fadein, fadeout=1.0)

    def sfx(key):
        path = REAL_SFX.get(key)
        if path is not None:
            renpy.sound.play(path)

    def scene_music(location_id, event=None):
        music(sim_assets.scene_music_key(location_id, SLOTS[store.gs.slot], event,
                                         LOCATION_MUSIC, REAL_MUSIC))

    def ending_music(ending):
        kind = ending if ending in ENDING_MUSIC else ENDINGS[ending].get("kind")
        music(ENDING_MUSIC.get(kind))
