## Founders' Gala (full version with gallery in M4).
## Asks the player who to invite, evaluates the ending and plays it.

screen gala_choice():
    modal True
    add Solid("#2a1830")
    vbox:
        xalign 0.5
        yalign 0.45
        spacing 20
        text "Who will you ask to the [GALA_NAME]?" size 50 bold True color "#fff6fb" xalign 0.5
        for cid in CAST:
            if ("met_" + cid) in gs.flags:
                textbutton CAST_NAMES[cid]["name"]:
                    xalign 0.5
                    text_size 40
                    text_color SIGNATURE_COLORS[cid]["accent"]
                    text_hover_color "#ff5fa2"
                    action Return(cid)
        textbutton "Go alone":
            xalign 0.5
            text_size 34
            text_color "#c9bfd6"
            text_hover_color "#ff5fa2"
            action Return(None)


label gala:
    hide screen hud
    scene bg gala
    with fade
    # PLACEHOLDER: gala night lead-in (M4)
    "The night of the [GALA_NAME] has arrived."
    "Everyone is here. Everyone is dressed up. Everyone, it seems, is watching to see who you'll ask."
    call screen gala_choice
    $ ending = sim_end.evaluate_ending(gs, _return, RULES)
    $ persistent.endings_seen.add(ending)
    call expression ENDINGS[ending]["label"] pass (ending)
    return


label ending_card(ending):
    $ etitle = ENDINGS[ending]["title"]
    if "char" in ENDINGS[ending]:
        $ etitle = CAST_NAMES[ENDINGS[ending]["char"]]["name"] + " — " + etitle
    scene black
    with fade
    show text "{size=72}{color=#fff6fb}THE END{/color}{/size}\n\n{size=40}{color=#ff5fa2}[etitle]{/color}{/size}" at truecenter
    with dissolve
    pause
    return


label ending_placeholder(ending):
    # PLACEHOLDER: every ending gets its own scene in M3–M4.
    "(This route's endings are written in a later milestone.)"
    call ending_card(ending)
    return
