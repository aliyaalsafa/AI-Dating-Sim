## Phone / profile screen (CLAUDE.md §6.5): Contacts, Feed, Achievements.
## Anything the player hasn't learned yet shows as ???.

define PHONE_BG = "#2a1830"
define PHONE_SCREEN = "#fff6fb"
define PHONE_INK = "#3a1640"

screen phone(tab="contacts"):
    modal True
    zorder 100
    default current = tab

    add Solid("#00000088")
    key "game_menu" action Hide("phone")

    frame:
        xalign 0.5
        yalign 0.5
        xysize (820, 1000)
        padding (26, 26)
        background Solid(PHONE_BG)

        vbox:
            spacing 16

            hbox:
                spacing 10
                xalign 0.5
                for t, label_ in [("contacts", "Contacts"), ("feed", "Feed"), ("achievements", "Achievements")]:
                    textbutton label_:
                        padding (22, 10)
                        background Solid("#fff6fb33" if current != t else "#ff5fa2")
                        hover_background Solid("#ff5fa2aa")
                        text_color "#fff6fb"
                        text_size 28
                        action SetScreenVariable("current", t)

            frame:
                xfill True
                ysize 820
                padding (24, 20)
                background Solid(PHONE_SCREEN)

                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    vbox:
                        spacing 22
                        xfill True
                        if current == "contacts":
                            use phone_contacts
                        elif current == "feed":
                            use phone_feed
                        else:
                            use phone_achievements

            textbutton "Close":
                xalign 0.5
                text_color "#fff6fb"
                text_hover_color "#ff5fa2"
                text_size 30
                action Hide("phone")


screen phone_contacts():
    for cid in CAST:
        $ c = gs.chars[cid]
        $ met = ("met_" + cid) in gs.flags
        $ col = SIGNATURE_COLORS[cid]
        frame:
            xfill True
            padding (20, 16)
            background Solid(col["accent"] + "55")
            vbox:
                spacing 6
                if not met:
                    text "???" size 32 bold True color PHONE_INK
                    text "You haven't met yet." size 24 color "#8a7f88" italic True
                else:
                    hbox:
                        spacing 16
                        text CAST_NAMES[cid]["full"] size 32 bold True color col["name"]
                        text CAST_NAMES[cid]["model"] size 22 color "#8a7f88" yalign 0.5
                    $ h = sim_aff.hearts(gs, cid)
                    text ("♥" * h + "♡" * (5 - h)) size 34 color "#ff5fa2"
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
            background Solid("#11141812")
            vbox:
                spacing 4
                text "Day %d" % p["day"] size 20 color "#8a7f88"
                text p["text"] size 26 color PHONE_INK


screen phone_achievements():
    for aid, a in ACHIEVEMENTS.items():
        $ got = aid in persistent.achievements
        frame:
            xfill True
            padding (18, 14)
            background Solid("#ff5fa233" if got else "#00000010")
            vbox:
                text (a["name"] if got else "???") size 28 bold True color PHONE_INK
                text (a["desc"] if got else "Locked") size 22 color "#8a7f88"
