## Founders' Gala (CLAUDE.md §5, §7). Day 30.
## Lead-in, a greeting from each character (routes/<cid>/gala_greeting.rpy),
## the invitation, then the ending. Endings seen persist across playthroughs.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

default gala_new_ending = False

screen gala_choice():
    modal True
    add Solid("#2a1830")
    vbox:
        xalign 0.5
        yalign 0.45
        spacing 20
        text "Who will you ask to the [GALA_NAME]?" size 50 bold True color "#fff6fb" xalign 0.5
        null height 10
        for cid in CAST:
            if ("met_" + cid) in gs.flags:
                $ h = sim_aff.hearts(gs, cid)
                button:
                    xalign 0.5
                    action Return(cid)
                    hbox:
                        spacing 24
                        text CAST_NAMES[cid]["name"]:
                            size 40
                            min_width 260
                            color SIGNATURE_COLORS[cid]["accent"]
                            hover_color "#ff5fa2"
                        text ("♥" * h + "♡" * (5 - h)) size 34 color "#ff5fa2" yalign 0.5
        null height 10
        textbutton "Go alone":
            xalign 0.5
            text_size 34
            text_color "#c9bfd6"
            text_hover_color "#ff5fa2"
            action Return(None)


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
        if gala_pick_tmp is None:
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
    $ enew = "{color=#ffd84d}New ending!{/color}  " if gala_new_ending and not _in_replay else ""
    scene black
    with fade
    show text "{size=72}{color=#fff6fb}THE END{/color}{/size}\n\n{size=40}{color=#ff5fa2}[etitle]{/color}{/size}\n\n\n{size=28}{color=#c9bfd6}[enew]Endings found: [eseen] / [etotal]{/color}{/size}" at truecenter
    with dissolve
    pause
    return


## Replays an ending from the endings gallery (Ren'Py Replay, scope sets `replay_ending_id`).
label replay_ending:
    $ gala_new_ending = False
    $ gs = sim_state.new_game(CAST.keys(), RULES)
    $ ending_music(replay_ending_id)
    call expression ENDINGS[replay_ending_id]["label"] pass (replay_ending_id)
    $ renpy.end_replay()
    return
