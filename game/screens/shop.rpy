## Gift shop and gift picker (CLAUDE.md §6.4).

screen gift_shop():
    modal True
    add Solid("#00000066")

    frame:
        xalign 0.5
        yalign 0.55
        xysize (1100, 860)
        padding (34, 28)
        background Solid("#f3e8ff")

        vbox:
            spacing 16
            hbox:
                xfill True
                text "Campus Store" size 44 bold True color PHONE_INK
                text "Cash: [gs.money]" size 32 color "#7b4dff" xalign 1.0 yalign 0.5

            viewport:
                ysize 620
                scrollbars "vertical"
                mousewheel True
                draggable True
                vbox:
                    spacing 8
                    for gid, item in SHOP.items():
                        $ owned = gs.inventory.get(gid, 0)
                        hbox:
                            xfill True
                            text item["name"] + (" (own %d)" % owned if owned else "") size 28 color PHONE_INK yalign 0.5
                            textbutton "Buy  %d" % item["price"]:
                                xalign 1.0
                                padding (20, 6)
                                background Solid("#7b4dff")
                                hover_background Solid("#ff5fa2")
                                insensitive_background Solid("#c9bfd6")
                                text_color "#ffffff"
                                text_size 26
                                sensitive gs.money >= item["price"]
                                action Function(buy_gift, gid)

            textbutton "Leave":
                xalign 0.5
                text_size 32
                action Return()


screen gift_picker(cid):
    modal True
    add Solid("#00000066")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        padding (34, 28)
        background Solid("#fff6fb")
        vbox:
            spacing 12
            text "Give %s..." % cname(cid) size 40 bold True color PHONE_INK
            if not gs.inventory:
                text "You don't have any gifts. The campus store sells them." size 26 color "#8a7f88"
            for gid, n in gs.inventory.items():
                textbutton "%s  x%d" % (SHOP[gid]["name"], n):
                    text_size 30
                    action Return(gid)
            textbutton "Never mind":
                text_size 28
                action Return(None)
