## Playtest tools: a "Dev" button on the HUD for skipping ahead while testing.
##
## Release-safe by default. The button shows only when:
##   - running from the Ren'Py SDK (config.developer is True for unbuilt projects), or
##   - game/playtest_enabled.txt exists, which pages.yml creates just before the
##     GitHub Pages playtest build. It is gitignored and never committed, so
##     desktop and itch.io builds never include it (see RELEASE.md).

define PLAYTEST = config.developer or renpy.loadable("playtest_enabled.txt")

init python:

    def pt_affection(cid, delta):
        s = sim_state.evolve(store.gs)
        c = s.chars[cid]
        c.affection = max(0, min(sim_aff.cap_for(s, cid, RULES), c.affection + delta))
        store.gs = s

    def pt_skip_days(n):
        s = sim_state.evolve(store.gs)
        s.day = min(RULES.semester_days - 1, s.day + n)
        s.seen_today = set()
        store.gs = s

    def pt_to_gala_eve():
        s = sim_state.evolve(store.gs)
        s.day = RULES.semester_days - 1
        s.seen_today = set()
        store.gs = s

    def pt_all_clues():
        """Know every minor clue (to test crafted prompts)."""
        pairs = [(src, MYSTERY["minor"][src][w]["about"]) for src in MYSTERY["order"] for w in ("freebie", "earned")]
        store.gs = sim_clues.seed_minors(store.gs, pairs)
        renpy.notify("All minor clues known")

    def pt_money(n):
        s = sim_state.evolve(store.gs)
        s.money += n
        store.gs = s


screen playtest_tools():
    modal True
    zorder 120
    add Solid("#3a164099")

    frame:
        xalign 0.5
        yalign 0.5
        padding (54, 40, 54, 44)
        background ui_panel("panel")
        vbox:
            spacing 14
            text "Playtest tools" size 40 bold True color PHONE_INK
            text "Affection" size 26 color "#8a7f88"
            for cid in CAST:
                hbox:
                    spacing 16
                    text "%s: %d" % (cname(cid), gs.chars[cid].affection) min_width 260 size 30 color SIGNATURE_COLORS[cid]["name"]
                    textbutton "-10" action Function(pt_affection, cid, -10)
                    textbutton "+10" action Function(pt_affection, cid, 10)
                    textbutton "+25" action Function(pt_affection, cid, 25)
            null height 10
            hbox:
                spacing 24
                textbutton "Skip 2 days" action Function(pt_skip_days, 2)
                textbutton "Go to gala eve" action Function(pt_to_gala_eve)
                textbutton "+100 cash" action Function(pt_money, 100)
                textbutton "All clues" action Function(pt_all_clues)
            textbutton "Close" xalign 0.5 action Hide("playtest_tools")


screen playtest_button():
    if PLAYTEST:
        textbutton "Dev":
            padding (24, 8, 24, 12)
            background ui_pill("violet")
            hover_background ui_pill("pink")
            text_color "#ffffff"
            text_outlines OUTLINE_SMALL
            text_size 28
            action Show("playtest_tools")
