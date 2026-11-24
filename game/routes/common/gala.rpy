## Founders' Gala placeholder (full version in M4).
## Asks the player who to invite, evaluates the ending, records it in the gallery.

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
    scene expression placeholder_bg(GALA_NAME, "#2a1830", "#fff6fb99")
    with fade
    # PLACEHOLDER: gala night scenes (M4)
    "The night of the [GALA_NAME] has arrived."
    call screen gala_choice
    $ ending = sim_end.evaluate_ending(gs, _return, RULES)
    $ persistent.endings_seen.add(ending)
    call expression ENDINGS[ending]["label"] pass (ending)
    return


label ending_placeholder(ending):
    # PLACEHOLDER: every ending gets its own scene in M2–M4.
    $ etitle = ENDINGS[ending]["title"]
    "Ending reached: [etitle] ([ending])."
    return
