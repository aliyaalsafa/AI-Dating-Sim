## Evening recap on the phone (CLAUDE.md §5 step 5).

screen day_recap():
    modal True
    add Solid("#00000088")

    $ totals = recap_totals()

    frame:
        xalign 0.5
        yalign 0.5
        xsize 760
        padding (26, 26)
        background Solid(PHONE_BG)
        vbox:
            spacing 16
            text "Day [gs.day] recap" size 40 bold True color "#fff6fb" xalign 0.5
            frame:
                xfill True
                padding (24, 20)
                background Solid(PHONE_SCREEN)
                vbox:
                    spacing 10
                    if not totals:
                        text "A quiet day. Nobody's feelings changed." size 28 color PHONE_INK italic True
                    for cid, d in totals.items():
                        hbox:
                            xfill True
                            text cname(cid) size 30 bold True color SIGNATURE_COLORS[cid]["name"]
                            text ("+%d ♥" % d if d >= 0 else "%d ♥" % d) size 30 color ("#ff5fa2" if d >= 0 else "#8a7f88") xalign 1.0
                    if gs.feed and gs.feed[-1]["day"] == gs.day:
                        null height 10
                        text "@x_unfiltered just posted:" size 22 color "#0090ff" bold True
                        text gs.feed[-1]["text"] size 24 color PHONE_INK italic True
            textbutton "Go to sleep":
                xalign 0.5
                text_color "#fff6fb"
                text_hover_color "#ff5fa2"
                text_size 32
                action Return()
