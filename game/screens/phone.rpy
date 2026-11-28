## Phone / profile screen (CLAUDE.md §6.5): Contacts, Feed, Achievements.
## Anything the player hasn't learned yet shows as ???.

define PHONE_BG = "#2a1830"
define PHONE_SCREEN = "#fff6fb"
define PHONE_INK = "#3a1640"

screen phone(tab="contacts", called=False):
    modal True
    zorder 100
    default current = tab

    add Solid("#3a164099")
    $ _close = Return() if called else Hide("phone")
    key "game_menu" action _close
    on "show" action If(tab == "case", SetVariable("case_new", False))

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
                $ tabs = [("contacts", "Contacts"), ("feed", "Feed")]
                if mystery_on() and has_flag(sim_clues.STARTED_FLAG):
                    $ tabs.append(("case", "Case •" if case_new else "Case"))
                $ tabs.append(("achievements", "Awards"))
                for t, label_ in tabs:
                    button:
                        background ui_pill("pink" if current == t else "plum")
                        hover_background ui_pill("violet")
                        padding (26, 8, 26, 12)
                        action [SetScreenVariable("current", t),
                                If(t == "case", SetVariable("case_new", False))]
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
                        elif current == "case":
                            use phone_case
                        else:
                            use phone_achievements

            hbox:
                xalign 0.5
                use pill_button("Close", _close, "white", 28)


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
                        if c.stage != "none":
                            frame:
                                yalign 0.5
                                background ui_pill("gold" if c.stage == "lover" else "pink")
                                padding (18, 4, 18, 8)
                                text STAGE_LABELS[c.stage] size 22 color "#ffffff" outlines OUTLINE_SMALL
                    $ h = sim_aff.hearts(gs, cid)
                    use hearts(h)
                    if c.romance_locked:
                        text "Just friends now." size 22 color "#8a7f88" italic True
                    elif c.stage == "none" and sim_rom.can_date(gs, cid, RULES):
                        text "She'd say yes to a date. Ask her tonight." size 22 color THEME_HOT italic True
                    for key in sim_rom.FACT_KEYS:
                        $ v = CAST[cid]["favorites"][key]
                        $ v = ", ".join(v) if isinstance(v, list) else v
                        text "%s: %s" % (FACT_LABELS[key], v if key in c.known else "???") size 22 color PHONE_INK
                    $ fs = c.favor_status
                    if fs == "not_offered":
                        text "Favor: ???" size 22 color PHONE_INK
                    elif fs == "active":
                        text "Favor: " + CAST[cid]["favor"]["desc"] + " (%d days left)" % sim_fav.days_left(gs, cid) size 22 color "#b0306a"
                    else:
                        text "Favor: " + fs.capitalize() size 22 color PHONE_INK
                    if c.stage == "girlfriend":
                        text "Her special gift: %s (campus store)" % SHOP[CAST[cid]["special_gift"]]["name"] size 22 color THEME_HOT bold True


screen phone_feed():
    text "@x_unfiltered" size 30 bold True color PHONE_INK
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


## Mystery board: the premise, then per girl her major clue and the hints
## about her (which pair scene gives each).
screen phone_case():
    $ found, total = mystery_progress()
    $ minors = sim_clues.known_minors(gs)
    $ majors = sim_clues.known_majors(gs)
    text MYSTERY["title"] size 32 bold True color PHONE_INK
    text MYSTERY["premise"] size 24 color THEME_MUTED italic True
    text "Pieces found: %d / %d" % (found, total) size 26 bold True color THEME_HOT
    if sim_clues.knows_truth(gs):
        frame:
            xfill True
            background ui_panel("panel_dark")
            padding (26, 18)
            text MYSTERY["solution"] size 24 color "#ffffff"
    for cid in MYSTERY["order"]:
        $ major = MYSTERY["major"][cid]
        frame:
            xfill True
            padding (24, 16)
            background ui_card("card_hover" if cid in majors else "card")
            vbox:
                spacing 6
                hbox:
                    spacing 12
                    use char_chip(cid, 24)
                    text (major["name"] if cid in majors else "Major clue: ???") size 24 bold True color PHONE_INK yalign 0.5
                if cid in majors:
                    text major["text"] size 22 color PHONE_INK italic True
                for pid in sim_clues.pairs_about(MYSTERY, cid):
                    $ p = sim_clues.pair_by_id(MYSTERY, pid)
                    $ other = [x for x in p["chars"] if x != cid][0]
                    if (pid, cid) in minors:
                        text "• " + p["hints"][cid] size 22 color PHONE_INK
                    else:
                        text "• ??? (overhear %s with %s)" % (cname(cid), cname(other)) size 22 color "#9a8f98"
                if cid not in majors:
                    $ ready = sim_clues.can_craft(gs, MYSTERY, cid)
                    text ("You know enough to ask her the right way." if ready else "Overhear both hints to ask her the right way, or force it out of her.") size 20 color (THEME_HOT if ready else "#9a8f98") italic True
