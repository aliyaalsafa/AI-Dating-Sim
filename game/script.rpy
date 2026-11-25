## Entry point and main loop (CLAUDE.md §5).
##
## Morning, afternoon, evening: a scripted ("forced") scene if one is due,
## otherwise the campus map. Night: dates only (routes/common/night.rpy).
## The day ends with the phone recap. Day 14's evening is the gala.

label start:
    $ gs = sim_state.new_game(CAST.keys(), RULES)
    $ mystery_seed_new_game()
    jump day_loop


label day_loop:
    show screen hud

    while not sim_cal.is_gala_day(gs, RULES):

        $ fev = sim_ev.pick_forced(EVENTS, gs)

        if fev is not None:
            $ gs = sim_ev.mark_seen(gs, fev)
            $ scene_music(fev.get("location"), fev)
            call expression fev["label"] pass (*fev.get("args", []))

        elif sim_cal.is_night(gs):
            call night_phase

        else:
            # The store takes no time: shop, then pick where to actually go.
            $ loc = None
            while loc is None:
                call screen campus_map
                $ loc = _return
                if LOCATIONS[loc].get("kind") == "shop":
                    $ scene_music(loc)
                    scene expression "bg " + loc
                    call screen gift_shop
                    $ loc = None

            scene expression "bg " + loc
            with dissolve
            call visit_location(loc)

        $ check_achievements()

        if sim_cal.is_last_slot(gs):
            call screen day_recap
            if gs.day == 1:
                $ grant("first_day")

        $ gs = sim_cal.advance(gs, RULES)
        if gs.slot == 0:
            $ sfx("new_day")

    jump gala


## One visit to a map location.
##   - A pair scene plays if both girls are here and it's unseen.
##   - Otherwise pick whom to talk to (if more than one), then optionally ask
##     her about the mystery, give her a gift (free), and play her event.
label visit_location(loc):
    $ ev = sim_ev.pick_event(EVENTS, gs, LOCATIONS, loc)
    if ev is not None and ev["kind"] == "pair":
        $ scene_music(loc, ev)
        call play_event(ev)
        return

    $ here = sim_ev.present(LOCATIONS, loc, gs)
    if not here:
        if ev is not None:
            $ scene_music(loc, ev)
            call play_event(ev)
        else:
            $ scene_music(loc)
            "Nobody's around. You enjoy a quiet moment to yourself."
        return

    $ who = here[0]
    if len(here) > 1:
        $ who = renpy.display_menu([("Talk to %s" % cname(c), c) for c in here])

    $ ev = sim_ev.pick_event(EVENTS, gs, LOCATIONS, loc, focus=who)
    $ scene_music(loc, ev)

    if mystery_can_ask(who):
        $ _act = renpy.display_menu([
            ("Spend time with %s" % cname(who), "talk"),
            ("Ask %s why you were admitted" % cname(who), "ask"),
        ])
        if _act == "ask":
            call mystery_confront(who)
            return

    if gs.inventory and has_flag("met_" + who) and gs.chars[who].last_gift_day != gs.day:
        call offer_gift(who)

    if ev is not None:
        call play_event(ev)
    else:
        $ _cn = cname(who)
        "[_cn] waves, but you've already spent time together today. Maybe tomorrow."
    return


## Plays an event, then the bookkeeping every event shares.
label play_event(ev):
    $ gs = sim_ev.mark_seen(gs, ev)
    $ _fav_before = {c: gs.chars[c].favor_status for c in CAST}
    call expression ev["label"] pass (*ev.get("args", []))

    if ev["kind"] == "hangout":
        $ learn_fact(ev["route"])

    # She asks her favor at the end of the scene where she opens up.
    if ev["id"].endswith("_opens_up") and gs.chars[ev["route"]].favor_status == "not_offered":
        call expression ev["route"] + "_favor_offer"

    $ _done = [c for c in CAST if _fav_before[c] != "done" and gs.chars[c].favor_status == "done"]
    if _done:
        $ _cn = cname(_done[0])
        $ sfx("achievement")
        "(Favor done. [_cn] paid you $[RULES.favor_pay]. That's enough for something special at the campus store.)"
        $ learn_fact(_done[0])
    return
