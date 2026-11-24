## Founders' Gala (CLAUDE.md §5, §7). Day 30.
## Lead-in, a greeting from each character (routes/<cid>/gala_greeting.rpy),
## the invitation, then the ending. Endings seen persist across playthroughs.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

default gala_new_ending = False

screen gala_choice():
    modal True
    add gui.main_menu_background
    vbox:
        xalign 0.5
        yalign 0.45
        spacing 18
        use heading("Who will you ask to the %s?" % GALA_NAME, 60)
        null height 14
        for cid in CAST:
            if ("met_" + cid) in gs.flags:
                $ h = sim_aff.hearts(gs, cid)
                button at pop_hover:
                    xalign 0.5
                    xsize 760
                    background ui_card("card")
                    hover_background ui_card("card_hover")
                    padding (34, 16)
                    action Return(cid)
                    hbox:
                        xfill True
                        use char_chip(cid, 32)
                        hbox:
                            xalign 1.0
                            yalign 0.5
                            use hearts(h, 5, 1.2)
        null height 14
        hbox:
            xalign 0.5
            spacing 20
            use pill_button("Go alone", Return(None), "white", 30)
            if mystery_on() and sim_clues.solved(gs, MYSTERY["order"]):
                use pill_button("Tell everyone what you found", Return(sim_end.TRUTH_CHOICE), "gold", 30)


label gala:
    hide screen hud
    $ music("gala")
    scene bg gala
    with fade

    # PLACEHOLDER: gala lead-in
    "Day [RULES.semester_days]. The night of the [GALA_NAME]."
    "The great hall has been strung with about four thousand fairy lights. Someone has clearly over-delivered on the decorations committee."
    $ post("BREAKING: the Founders' Gala is tonight and the new kid still hasn't asked anyone. the tension. the DRAMA. 🍿")
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

    "The band slows down. It's time to ask someone. Or not."

    $ gala_pick = "unset"
    while gala_pick == "unset":
        call screen gala_choice
        $ gala_pick_tmp = _return
        if gala_pick_tmp == sim_end.TRUTH_CHOICE:
            menu:
                "Skip the invitations and reveal the truth?"
                "Yes. Tell them.":
                    $ gala_pick = gala_pick_tmp
                "Wait, let me think again.":
                    pass
        elif gala_pick_tmp is None:
            menu:
                "Go to the gala alone?"
                "Yes, go alone.":
                    $ gala_pick = None
                "Wait, let me think again.":
                    pass
        else:
            $ gala_who = cname(gala_pick_tmp)
            menu:
                "Ask [gala_who] to the [GALA_NAME]?"
                "Ask her.":
                    $ gala_pick = gala_pick_tmp
                "Wait, let me think again.":
                    pass

    $ ending = sim_end.evaluate_ending(gs, gala_pick, RULES)
    $ gala_new_ending = ending not in persistent.endings_seen
    $ persistent.endings_seen.add(ending)
    $ renpy.save_persistent()
    $ check_achievements()
    $ ending_music(ending)
    call expression ENDINGS[ending]["label"] pass (ending)
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
    $ ending_music(replay_ending_id)
    call expression ENDINGS[replay_ending_id]["label"] pass (replay_ending_id)
    $ renpy.end_replay()
    return
