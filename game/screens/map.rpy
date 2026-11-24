## Campus map (CLAUDE.md §5). Returns the chosen location id.

screen campus_map():
    modal True

    add gui.game_menu_background

    vbox:
        xalign 0.5
        ypos 105
        use heading("Where to this %s?" % slot_label().lower(), 58)

    grid 4 2:
        xalign 0.5
        ypos 215
        spacing 26

        for lid, loc in LOCATIONS.items():
            $ is_open = sim_ev.is_open(LOCATIONS, lid, gs)
            $ here = sim_ev.present(LOCATIONS, lid, gs)

            button at pop_hover:
                xysize (420, 340)
                padding (30, 28)
                background ui_card("card" if is_open else "card_off")
                hover_background ui_card("card_hover")
                insensitive_background ui_card("card_off")
                sensitive is_open
                action Return(lid)

                # big location icon in the corner
                text loc.get("icon", "♥"):
                    size 120
                    xalign 1.0
                    yalign 1.0
                    color (THEME_PINK_LIGHT if is_open else "#e4dce2")
                    outlines [(4, "#ffffff", 0, 0)]

                vbox:
                    spacing 12
                    text loc["name"] size 34 bold True color (THEME_PLUM if is_open else "#9a8f98")

                    if not is_open:
                        text "Closed right now" size 26 color "#9a8f98" italic True
                    elif loc.get("kind") == "shop":
                        hbox:
                            spacing 8
                            add "gui/theme/heart_small.png" yalign 0.5
                            text "Gift shop" size 28 color THEME_VIOLET bold True
                    elif not here:
                        text "Nobody around" size 26 color THEME_MUTED italic True
                    else:
                        for cid in here:
                            use char_chip(cid)
