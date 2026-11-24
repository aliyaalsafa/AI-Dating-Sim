## Gift shop and gift picker (CLAUDE.md §6.4).

screen gift_shop():
    modal True
    add Solid("#3a164077")

    frame:
        xalign 0.5
        yalign 0.56
        xysize (1160, 880)
        padding (54, 40, 54, 44)
        background ui_panel("panel")

        vbox:
            spacing 16
            hbox:
                xfill True
                text "Campus Store" size 56 color "#ffffff" outlines OUTLINE_MED
                frame:
                    xalign 1.0
                    yalign 0.5
                    background ui_pill("gold")
                    padding (26, 8, 30, 12)
                    text "$ [gs.money]" size 30 color "#ffffff" outlines [(3, "#b77900", 0, 0)]

            viewport:
                ysize 600
                scrollbars "vertical"
                mousewheel True
                draggable True
                vbox:
                    spacing 10
                    for gid, item in SHOP.items():
                        $ owned = gs.inventory.get(gid, 0)
                        frame:
                            xfill True
                            background ui_card("card")
                            padding (26, 12)
                            hbox:
                                xfill True
                                text item["name"] + ("  (own %d)" % owned if owned else "") size 28 color THEME_PLUM yalign 0.5
                                hbox:
                                    xalign 1.0
                                    use pill_button("Buy  $%d" % item["price"], Function(buy_gift, gid), "pink", 24, gs.money >= item["price"])

            hbox:
                xalign 0.5
                use pill_button("Leave", Return(), "white", 30)


screen gift_picker(cid):
    modal True
    add Solid("#3a164077")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        padding (54, 40, 54, 44)
        background ui_panel("panel")
        vbox:
            spacing 14
            xfill True
            use heading("Give %s a gift" % cname(cid), 48)
            if not gs.inventory:
                text "You don't have any gifts. The campus store sells them." size 26 color THEME_MUTED xalign 0.5
            for gid, n in gs.inventory.items():
                hbox:
                    xalign 0.5
                    use pill_button("%s  x%d" % (SHOP[gid]["name"], n), Return(gid), "pink", 28, True, 640)
            null height 4
            hbox:
                xalign 0.5
                use pill_button("Never mind", Return(None), "white", 28)
