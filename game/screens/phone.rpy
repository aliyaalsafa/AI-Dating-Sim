## Phone / profile screen (CLAUDE.md §6.5): Contacts, Feed, Achievements.
## Anything the player hasn't learned yet shows as ???.

define PHONE_BG = "#2a1830"
define PHONE_SCREEN = "#fff6fb"
define PHONE_INK = "#3a1640"

screen phone(tab="contacts"):
    modal True
    zorder 100
    default current = tab

    add Solid("#3a164099")
    key "game_menu" action Hide("phone")

    frame at notify_pop:
        xalign 0.5
        yalign 0.5
        xysize (860, 1040)
        padding (40, 36, 40, 36)
        background ui_panel("panel_dark")

        vbox:
            spacing 16

            hbox:
                spacing 8
                xalign 0.5
                for t, label_ in [("contacts", "Contacts"), ("feed", "Feed"), ("achievements", "Awards")]:
                    button:
                        background ui_pill("pink" if current == t else "plum")
                        hover_background ui_pill("violet")
                        padding (26, 8, 26, 12)
                        action SetScreenVariable("current", t)
                        text label_ size 26 color "#ffffff" outlines OUTLINE_SMALL

            frame:
                xfill True
                ysize 820
                padding (26, 24, 18, 24)
                background ui_panel("panel")

                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    vbox:
                        spacing 16
                        xfill True
                        if current == "contacts":
                            use phone_contacts
                        elif current == "feed":
                            use phone_feed
                        else:
                            use phone_achievements

            hbox:
                xalign 0.5
                use pill_button("Close", Hide("phone"), "white", 28)


screen phone_contacts():
    for cid in CAST:
        $ c = gs.chars[cid]
        $ met = ("met_" + cid) in gs.flags
        $ col = SIGNATURE_COLORS[cid]
        frame:
            xfill True
            padding (24, 18)
            background ui_card("card" if met else "card_off")
            vbox:
                spacing 6
                if not met:
                    text "???" size 32 bold True color PHONE_INK
                    text "You haven't met yet." size 24 color "#8a7f88" italic True
                else:
                    hbox:
                        spacing 14
                        use char_chip(cid, 28)
                        vbox:
                            yalign 0.5
                            text CAST_NAMES[cid]["full"] size 24 bold True color col["name"]
                            if SHOW_MODEL_SUBTITLES:
                                text CAST_NAMES[cid]["model"] size 20 color "#8a7f88"
                    $ h = sim_aff.hearts(gs, cid)
                    use hearts(h)
                    if c.romance_locked:
                        text "Just friends now." size 22 color "#8a7f88" italic True
                    text "Likes: " + (", ".join(CAST[cid]["favorites"]["likes"]) if "likes" in c.known else "???") size 24 color PHONE_INK
                    text "Dislikes: " + (", ".join(CAST[cid]["favorites"]["dislikes"]) if "dislikes" in c.known else "???") size 24 color PHONE_INK
                    $ fs = c.favor_status
                    if fs == "not_offered":
                        text "Favor: ???" size 24 color PHONE_INK
                    elif fs == "active":
                        text "Favor: " + CAST[cid]["favor"]["desc"] + " (%d days left)" % sim_fav.days_left(gs, cid) size 24 color "#b0306a"
                    else:
                        text "Favor: " + fs.capitalize() size 24 color PHONE_INK


screen phone_feed():
    text "@x_unfiltered" size 30 bold True color "#0090ff"
    if not gs.feed:
        text "No posts yet." size 24 color "#8a7f88" italic True
    for p in reversed(gs.feed):
        frame:
            xfill True
            padding (18, 14)
            background ui_card("card")
            vbox:
                spacing 4
                text "Day %d" % p["day"] size 20 color "#8a7f88"
                text p["text"] size 26 color PHONE_INK


screen phone_achievements():
    use achievement_rows
