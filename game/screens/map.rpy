## Campus map (CLAUDE.md §5). Returns the chosen location id.

screen campus_map():
    modal True

    add Solid("#ffd6e8")

    text "Where to this %s?" % slot_label().lower():
        xalign 0.5
        ypos 110
        size 54
        bold True
        color "#3a1640"

    grid 4 2:
        xalign 0.5
        ypos 220
        spacing 28

        for lid, loc in LOCATIONS.items():
            $ is_open = sim_ev.is_open(LOCATIONS, lid, gs)
            $ here = sim_ev.present(LOCATIONS, lid, gs)
            $ tc = loc.get("text_color", "#3a1640")

            button:
                xysize (420, 330)
                padding (22, 20)
                background Solid(loc["color"] if is_open else "#d8cfd6")
                hover_background Frame(Solid("#ffffff"), 0, 0)
                insensitive_background Solid("#d8cfd6")
                sensitive is_open
                action Return(lid)

                vbox:
                    spacing 14
                    text loc["name"] size 34 bold True color (tc if is_open else "#8a7f88")

                    if not is_open:
                        text "Closed right now" size 26 color "#8a7f88" italic True
                    elif loc.get("kind") == "shop":
                        text "Gift shop" size 26 color "#7b4dff"
                    elif not here:
                        text "Nobody around" size 26 color tc italic True
                    else:
                        for cid in here:
                            frame:
                                padding (14, 4)
                                background Solid(SIGNATURE_COLORS[cid]["fill"])
                                text cname(cid) size 26 color SIGNATURE_COLORS[cid]["accent"] bold True
