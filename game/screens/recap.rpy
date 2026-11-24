## Evening recap on the phone (CLAUDE.md §5 step 5).

screen day_recap():
    modal True
    add Solid("#3a164099")

    $ totals = recap_totals()

    frame at notify_pop:
        xalign 0.5
        yalign 0.5
        xsize 820
        padding (50, 44, 50, 50)
        background ui_panel("panel")
        vbox:
            spacing 18
            xfill True
            use heading("Day %d recap" % gs.day, 52)
            if not totals:
                text "A quiet day. Nobody's feelings changed." size 28 color THEME_MUTED italic True xalign 0.5
            for cid, d in totals.items():
                frame:
                    xfill True
                    background ui_card("card")
                    padding (24, 14)
                    hbox:
                        xfill True
                        use char_chip(cid, 26)
                        hbox:
                            xalign 1.0
                            yalign 0.5
                            spacing 8
                            text ("+%d" % d if d >= 0 else "%d" % d) size 34 bold True color (THEME_HOT if d >= 0 else THEME_MUTED) yalign 0.5
                            add ("gui/theme/heart_small.png" if d >= 0 else "gui/theme/heart_empty.png") yalign 0.5
            if gs.feed and gs.feed[-1]["day"] == gs.day:
                frame:
                    xfill True
                    background ui_panel("panel_dark")
                    padding (30, 20)
                    vbox:
                        spacing 6
                        text "[XENIA_HANDLE] just posted:" size 22 color "#5fd7ff" bold True
                        text gs.feed[-1]["text"] size 24 color "#ffffff" italic True
            null height 4
            hbox:
                xalign 0.5
                use pill_button("Go to sleep", Return(), "pink", 32)
