## Entry point and main loop (CLAUDE.md §5).

label start:

    $ gs = sim_state.new_game(CAST.keys(), RULES)

    scene bg quad
    with fade

    narrator "Welcome to [SCHOOL_NAME]."

    $ player_name = renpy.input("What's your name?", length=20).strip() or "You"

    # PLACEHOLDER: the real prologue is written in M2.
    narrator "You're the newest transfer student, and the only human on campus."
    narrator "One semester. [RULES.semester_days] days. Then the [GALA_NAME]."
    narrator "(Tip: choices show a prompt style. Each person responds to styles differently. You can hide the icons in Preferences.)"

    # PLACEHOLDER: @x_unfiltered's first post
    $ post("New transfer spotted on the quad. A HUMAN?? In this economy?")

    jump day_loop


label day_loop:
    show screen hud

    while not sim_cal.is_gala_day(gs, RULES):

        call screen campus_map
        $ loc = _return

        scene expression location_bg(loc)
        with dissolve

        if LOCATIONS[loc].get("kind") == "shop":
            call screen gift_shop
        else:
            $ ev = sim_ev.pick_event(EVENTS, gs, LOCATIONS, loc)
            if ev is None:
                "Nobody's around. You enjoy a quiet moment to yourself."
            else:
                $ gs = sim_ev.mark_seen(gs, ev["id"])
                call expression ev["label"] pass (*ev.get("args", []))

        if sim_cal.is_evening(gs):
            call screen day_recap
            if gs.day == 1:
                $ grant("first_day")

        $ gs = sim_cal.advance(gs, RULES)

    jump gala
