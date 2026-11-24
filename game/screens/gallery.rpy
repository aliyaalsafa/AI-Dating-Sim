## Endings gallery and achievements list (CLAUDE.md §6.6, §8 M4).
## Both read persistent data, so they survive across playthroughs and are
## reachable from the main menu. Seen endings can be replayed.

define GALLERY_INK = "#3a1640"
define GALLERY_MUTED = "#8a7f88"
define GALLERY_CARD = "#fff6fb"

screen endings_gallery():
    tag menu

    $ eprog = endings_progress()

    use game_menu(_("Endings"), scroll="viewport"):
        vbox:
            spacing 22
            xfill True

            text "Endings found: %d / %d" % eprog size 34 bold True color GALLERY_INK
            text "Seen endings can be replayed. They stay unlocked across playthroughs." size 24 color GALLERY_MUTED

            for cid in CAST:
                hbox:
                    spacing 16
                    text CAST_NAMES[cid]["name"]:
                        size 30
                        bold True
                        min_width 200
                        yalign 0.5
                        color SIGNATURE_COLORS[cid]["name"]
                    for kind, ktitle in ENDING_KINDS:
                        use gallery_card("%s_%s" % (kind, cid), ktitle)

            null height 6
            text "Other endings" size 30 bold True color GALLERY_INK
            hbox:
                spacing 16
                use gallery_card("solo", ENDINGS["solo"]["title"])
                use gallery_card("rivals", ENDINGS["rivals"]["title"])
                if RULES.clue_layer:
                    use gallery_card("truth", ENDINGS["truth"]["title"])


screen gallery_card(eid, label_text):
    $ seen = eid in persistent.endings_seen
    $ secret = ENDINGS[eid].get("secret", False)
    button at pop_hover:
        xysize (300, 100)
        padding (26, 12)
        background (ui_pill("pink") if seen else ui_card("card_off"))
        hover_background (ui_pill("violet") if seen else ui_card("card_off"))
        sensitive seen
        action Replay("replay_ending", scope={"replay_ending_id": eid}, locked=False)
        vbox:
            yalign 0.5
            text (label_text if seen else "???"):
                size 26
                bold True
                color ("#ffffff" if seen else GALLERY_INK)
                outlines (OUTLINE_SMALL if seen else [])
            text ("Replay ▸" if seen else ("Secret" if secret else "Not found yet")):
                size 20
                color ("#ffffffcc" if seen else GALLERY_MUTED)


screen achievements_gallery():
    tag menu

    use game_menu(_("Achievements"), scroll="viewport"):
        vbox:
            spacing 14
            xfill True
            $ agot = len(persistent.achievements & set(ACHIEVEMENTS))
            text "Unlocked: %d / %d" % (agot, len(ACHIEVEMENTS)) size 34 bold True color GALLERY_INK
            use achievement_rows


## Shared by the phone's Achievements tab and the menu screen above.
screen achievement_rows():
    for aid, a in ACHIEVEMENTS.items():
        $ got = aid in persistent.achievements
        $ hidden = a.get("secret", False) and not got
        frame:
            xfill True
            padding (24, 14)
            background ui_card("card_hover" if got else "card_off")
            hbox:
                spacing 16
                add ("gui/theme/heart_small.png" if got else "gui/theme/heart_empty.png") yalign 0.5
                vbox:
                    text (a["name"] if got else "???") size 28 bold True color GALLERY_INK
                    text ("Secret achievement" if hidden else (a["desc"] if got else "Locked: " + a["desc"])) size 22 color GALLERY_MUTED
