## Playtest tools: a "Dev" button on the HUD for skipping ahead while testing.
## Turn PLAYTEST off before any public release (see DECISIONS.md).

define PLAYTEST = True

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

    def pt_money(n):
        s = sim_state.evolve(store.gs)
        s.money += n
        store.gs = s


screen playtest_tools():
    modal True
    zorder 120
    add Solid("#00000099")

    frame:
        xalign 0.5
        yalign 0.5
        padding (36, 30)
        background Solid("#fff6fb")
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
                textbutton "Skip 5 days" action Function(pt_skip_days, 5)
                textbutton "Go to gala eve" action Function(pt_to_gala_eve)
                textbutton "+100 cash" action Function(pt_money, 100)
            textbutton "Close" xalign 0.5 action Hide("playtest_tools")


screen playtest_button():
    zorder 51
    if PLAYTEST:
        textbutton "Dev":
            xalign 1.0
            xoffset -180
            ypos 20
            padding (20, 12)
            background Solid("#7b4dff")
            hover_background Solid("#ff5fa2")
            text_color "#ffffff"
            text_size 30
            action Show("playtest_tools")
