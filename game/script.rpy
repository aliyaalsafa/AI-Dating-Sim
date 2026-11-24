## Entry point and main loop (CLAUDE.md §5).
##
## Each slot: a scripted ("forced") scene if one is due, otherwise the campus
## map. Evenings end with the phone recap. The last day's evening is the gala.

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

        else:
            call screen campus_map
            $ loc = _return

            scene expression "bg " + loc
            with dissolve

            if LOCATIONS[loc].get("kind") == "shop":
                $ scene_music(loc)
                call screen gift_shop
            else:
                call mystery_offer(loc)
                $ mtarget = _return
                $ ev = None if mtarget else sim_ev.pick_event(EVENTS, gs, LOCATIONS, loc)
                $ scene_music(loc, ev)
                if mtarget:
                    call mystery_confront(mtarget)
                elif ev is not None:
                    $ gs = sim_ev.mark_seen(gs, ev)
                    call expression ev["label"] pass (*ev.get("args", []))
                elif sim_ev.present(LOCATIONS, loc, gs):
                    $ busy = ", ".join(cname(c) for c in sim_ev.present(LOCATIONS, loc, gs))
                    "[busy] waves, but you've already spent time together today. Maybe tomorrow."
                else:
                    "Nobody's around. You enjoy a quiet moment to yourself."

        $ check_achievements()

        if sim_cal.is_evening(gs):
            call screen day_recap
            if gs.day == 1:
                $ grant("first_day")

        $ gs = sim_cal.advance(gs, RULES)
        if gs.slot == 0:
            $ sfx("new_day")

    jump gala
