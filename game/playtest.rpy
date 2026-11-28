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
        s.slot = 0
        s.seen_today = set()
        store.gs = s

    def pt_skip_day1():
        """Skip day 1: everyone met, the mystery started, day 2 morning."""
        s = sim_state.evolve(store.gs)
        s.flags |= {"met_" + c for c in CAST} | {sim_clues.STARTED_FLAG}
        for e in EVENTS:
            if e.get("day_max") == 1:
                s.seen_events.add(e["id"])
        s.day, s.slot, s.seen_today = 2, 0, set()
        store.gs = s

    def pt_to_gala_eve():
        s = sim_state.evolve(store.gs)
        s.day = RULES.semester_days - 1
        s.slot = 0
        s.seen_today = set()
        store.gs = s

    def pt_all_clues():
        """Know every pair-scene hint (to test well-crafted asks)."""
        hints = [(p["id"], c) for p in MYSTERY["pairs"] for c in p["chars"]]
        store.gs = sim_clues.seed_minors(store.gs, hints)
        renpy.notify("All hints known")

    def pt_stage(cid, stage):
        s = sim_state.evolve(store.gs)
        s.chars[cid].stage = stage
        s.chars[cid].affection = max(s.chars[cid].affection, RULES.date_at)
        s.flags.add("met_" + cid)
        store.gs = s

    def pt_truth():
        """Find every major clue and know the truth (to test the gala choice)."""
        s = sim_state.evolve(store.gs)
        s.layers.setdefault("clues", {"minor": set(), "major": set()})["major"] |= set(MYSTERY["order"])
        s.flags |= {sim_clues.STARTED_FLAG, sim_clues.TRUTH_FLAG}
        store.gs = s
        renpy.notify("You know the truth")

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
                    spacing 14
                    text "%s: %d %s" % (cname(cid), gs.chars[cid].affection, STAGE_LABELS[gs.chars[cid].stage]) min_width 330 size 28 color SIGNATURE_COLORS[cid]["name"]
                    textbutton "-10" action Function(pt_affection, cid, -10)
                    textbutton "+10" action Function(pt_affection, cid, 10)
                    textbutton "+25" action Function(pt_affection, cid, 25)
                    textbutton "GF" action Function(pt_stage, cid, "girlfriend")
                    textbutton "Lover" action Function(pt_stage, cid, "lover")
            null height 10
            hbox:
                spacing 24
                if gs.day == 1:
                    textbutton "Skip to day 2" action [Function(pt_skip_day1), Hide("playtest_tools"), Jump("day_loop")]
                textbutton "Skip 2 days" action Function(pt_skip_days, 2)
                textbutton "Go to gala eve" action Function(pt_to_gala_eve)
                textbutton "+100 cash" action Function(pt_money, 100)
                textbutton "All hints" action Function(pt_all_clues)
                textbutton "Know truth" action Function(pt_truth)
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
