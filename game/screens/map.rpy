## Campus map (CLAUDE.md §5). Returns the chosen location id.
## One portrait = time alone with her. Two portraits with a "Together" tag =
## a pair scene: you'll overhear them and get a hint about each.

screen campus_map():
    modal True

    add gui.game_menu_background

    vbox:
        xalign 0.5
        ypos 100
        $ _left = len(unmet())
        if _left and gs.day == 1:
            use heading("Meet everyone: %d left to find" % _left, 54)
        else:
            use heading("Where to this %s?" % slot_label().lower(), 54)

    grid 3 3:
        xalign 0.5
        ypos 190
        spacing 22

        for lid, loc in LOCATIONS.items():
            $ is_open = sim_ev.is_open(LOCATIONS, lid, gs)
            $ here = sim_ev.present(LOCATIONS, lid, gs)
            $ ev = sim_ev.pick_event(EVENTS, gs, LOCATIONS, lid) if is_open else None
            $ pair_scene = ev is not None and ev["kind"] == "pair"

            button at pop_hover:
                xysize (560, 268)
                padding (28, 22)
                background ui_card("card" if is_open else "card_off")
                hover_background ui_card("card_hover")
                insensitive_background ui_card("card_off")
                sensitive is_open
                action Return(lid)

                # big location icon in the corner
                text loc.get("icon", "♥"):
                    size 96
                    xalign 1.0
                    yalign 1.0
                    color (THEME_PINK_LIGHT if is_open else "#e4dce2")
                    outlines [(4, "#ffffff", 0, 0)]

                vbox:
                    spacing 10
                    text loc["name"] size 30 bold True color (THEME_PLUM if is_open else "#9a8f98")

                    if not is_open:
                        text "Closed right now" size 24 color "#9a8f98" italic True
                    elif loc.get("kind") == "shop":
                        hbox:
                            spacing 8
                            add "gui/theme/heart_small.png" yalign 0.5
                            text "Gift shop (takes no time)" size 24 color THEME_VIOLET bold True
                    elif not here:
                        text "Nobody around" size 24 color THEME_MUTED italic True
                    else:
                        hbox:
                            spacing 8
                            for cid in here:
                                use char_chip(cid, 24)
                        if pair_scene:
                            frame:
                                background ui_pill("gold")
                                padding (18, 4, 18, 8)
                                text "Together: overhear them" size 22 color "#ffffff" outlines [(2, "#b77900", 0, 0)]
