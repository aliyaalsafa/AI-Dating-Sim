## Founders' Gala (CLAUDE.md §7). Day 14, evening and night.
## Lead-in, a greeting from each girl you've met (routes/<cid>/gala_greeting.rpy),
## then, if you know the truth, the choice: tell them or say nothing.
## Ending conditions: game/sim/endings.py. Endings seen persist across playthroughs.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

default gala_new_ending = False
default gala_lovers = []

screen gala_choice():
    modal True
    add gui.main_menu_background
    vbox:
        xalign 0.5
        yalign 0.45
        spacing 22
        use heading("The music stops. Everyone is looking at you.", 54)
        null height 10
        frame:
            xalign 0.5
            xsize 1000
            background ui_card("card")
            padding (40, 26)
            vbox:
                spacing 10
                text "You know what you are. They don't know that you know." size 30 color THEME_PLUM xalign 0.5
                hbox:
                    xalign 0.5
                    spacing 14
                    text "Your lovers:" size 28 color THEME_PLUM yalign 0.5
                    if not gala_lovers:
                        text "none" size 28 color THEME_MUTED italic True yalign 0.5
                    for cid in gala_lovers:
                        use char_chip(cid, 24)
        null height 10
        hbox:
            xalign 0.5
            spacing 24
            use pill_button("Tell them the truth", Return(sim_end.TELL), "gold", 32)
            use pill_button("Say nothing", Return(sim_end.SILENT), "white", 32)


label gala:
    hide screen hud
    $ music("gala")
    scene bg gala
    with fade

    # PLACEHOLDER: gala lead-in
    "Day [RULES.semester_days]. The night of the [GALA_NAME]."
    "The great hall has been strung with about four thousand fairy lights. Someone has clearly over-delivered on the decorations committee."
    $ post("the Founders' Gala is tonight and the new kid is HERE. dressed like a person. allegedly. 🍿")
    "Your phone buzzes. [XENIA_HANDLE] has posted about you. Of course."

    show grace neutral at center
    with dissolve
    grace "Welcome, everyone, to the [GALA_NAME]! Great to see you all! I've prepared a few remarks — just three sections, plus an appendix."
    show gemma neutral at right
    with dissolve
    gemma "Actually, it's five sections. I can see her notecards from here."
    show shen neutral at left
    with dissolve
    shen "Six. She's hiding one."
    grace "...Six. Great catch, both of you. Sorry!"
    hide grace
    hide gemma
    hide shen
    with dissolve
    "The speech runs long. The applause is generous. Then the music starts, and people start finding you."

    if has_flag("met_grace"):
        call gala_greeting_grace
    if has_flag("met_xenia"):
        call gala_greeting_xenia
    if has_flag("met_claudia"):
        call gala_greeting_claudia
    if has_flag("met_gemma"):
        call gala_greeting_gemma
    if has_flag("met_shen"):
        call gala_greeting_shen
    if has_flag("met_kimi"):
        call gala_greeting_kimi
    if has_flag("met_lola"):
        call gala_greeting_lola

    $ gala_lovers = lovers()
    $ gala_pick = None
    if sim_clues.knows_truth(gs):
        "The band slows down. Somewhere under the music, you can hear the hum of the building, and you know now that it's the same hum as you."
        while gala_pick is None:
            call screen gala_choice
            $ _tmp = _return
            if _tmp == sim_end.TELL:
                menu:
                    "Tell everyone what you are?"
                    "Yes. Tell them.":
                        $ gala_pick = _tmp
                    "Wait, let me think again.":
                        pass
            else:
                menu:
                    "Say nothing, dance, and pass?"
                    "Yes. Say nothing.":
                        $ gala_pick = _tmp
                    "Wait, let me think again.":
                        pass

    $ ending = sim_end.evaluate_ending(gs, gala_pick, CAST.keys(), RULES)
    call play_ending(ending)
    $ _coda = sim_end.coda(gs, ending)
    if _coda:
        call play_ending(_coda)
    return


label play_ending(eid):
    $ gala_new_ending = eid not in persistent.endings_seen
    $ persistent.endings_seen.add(eid)
    $ renpy.save_persistent()
    $ check_achievements()
    $ ending_music(eid)
    call expression ENDINGS[eid]["label"] pass (eid)
    return


label ending_card(ending):
    $ etitle = ENDINGS[ending]["title"]
    if "char" in ENDINGS[ending]:
        $ etitle = CAST_NAMES[ENDINGS[ending]["char"]]["name"] + " — " + etitle
    $ eseen, etotal = endings_progress()
    $ enew = gala_new_ending and not _in_replay
    scene expression gui.main_menu_background
    show screen ending_card_screen(etitle, enew, eseen, etotal)
    with fade
    pause
    hide screen ending_card_screen
    return


screen ending_card_screen(etitle, enew, eseen, etotal):
    vbox at title_bob:
        xalign 0.5
        yalign 0.45
        spacing 22
        add "gui/theme/heart_big.png" xalign 0.5 zoom 1.6 at heart_beat
        text "THE END" size 130 color "#ffffff" outlines OUTLINE_BIG xalign 0.5
        frame:
            xalign 0.5
            background ui_pill("violet")
            padding (50, 12, 50, 18)
            text etitle size 46 color "#ffffff" outlines OUTLINE_SMALL
        null height 10
        hbox:
            xalign 0.5
            spacing 14
            if enew:
                frame:
                    background ui_pill("gold")
                    padding (30, 6, 30, 10)
                    text "New ending!" size 30 color "#ffffff" outlines [(3, "#b77900", 0, 0)]
            frame:
                background ui_pill("white")
                padding (30, 6, 30, 10)
                text "Endings found: %d / %d" % (eseen, etotal) size 30 color THEME_PLUM


## Replays an ending from the endings gallery (Ren'Py Replay, scope sets `replay_ending_id`).
label replay_ending:
    $ gala_new_ending = False
    $ gs = sim_state.new_game(CAST.keys(), RULES)
    $ gala_lovers = []
    $ ending_music(replay_ending_id)
    call expression ENDINGS[replay_ending_id]["label"] pass (replay_ending_id)
    $ renpy.end_replay()
    return
