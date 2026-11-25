## Night: dates only (CLAUDE.md §5, §6.1).
## Once her affection reaches RULES.date_at you can ask her out. The date
## plays <id>_bonus_date (first time), then a short quiz about her. Pass and
## <id>_confession plays: she's your girlfriend.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label night_phase:
    $ _cands = sim_rom.date_candidates(gs, CAST.keys(), RULES)
    if not _cands:
        scene bg dorm
        with dissolve
        # PLACEHOLDER
        "Night falls. Nobody's waiting on a date tonight, so you turn in early."
        return
    call screen night_choice(_cands)
    $ _who = _return
    if _who not in CAST:
        scene bg dorm
        with dissolve
        "You stay in tonight."
        return
    call night_date(_who)
    return


label night_date(cid):
    $ _cn = cname(cid)
    $ _home = CAST[cid]["home"]
    $ scene_music(_home)
    scene expression "bg " + _home
    with fade
    if gs.chars[cid].dates == 0:
        call expression cid + "_bonus_date"
    else:
        $ renpy.show((cid, "neutral"), at_list=[center])
        with dissolve
        # PLACEHOLDER
        "[_cn] agreed to a second try. She's pretending she isn't nervous. So are you."
    call date_quiz(cid)
    if _return:
        $ grant("first_girlfriend")
        call expression cid + "_confession"
        $ _cn = cname(cid)
        "(You and [_cn] are together now. Her special gift is on your phone, and the campus store sells it.)"
    else:
        $ renpy.show((cid, "neutral"), at_list=[center])
        # PLACEHOLDER
        "[_cn] laughs it off, but you can tell she hoped you'd know her better by now."
        "(Spend more time with her to learn about her, then ask again another night.)"
    $ renpy.hide(cid)
    with dissolve
    return


## Returns True if she passes you.
label date_quiz(cid):
    $ _cn = cname(cid)
    $ _quiz = sim_rom.build_quiz(CAST, cid, _cn, gs.chars[cid].known, seed=gs.day * 31 + len(cid), rules=RULES)
    $ _correct = 0
    $ _qi = 0
    $ renpy.show((cid, "neutral"), at_list=[center])
    # PLACEHOLDER
    $ renpy.say(CHAR[cid], "Okay. Pop quiz. How well do you actually know me?")
    while _qi < len(_quiz):
        $ _q = _quiz[_qi]
        $ narrator(_q["prompt"], interact=False)
        $ _pick = renpy.display_menu([(o, o) for o in _q["options"]])
        if _pick == _q["answer"]:
            $ _correct += 1
            "She grins. Right."
        else:
            $ _ans = _q["answer"]
            "She winces. It's \"[_ans]\"."
        $ _qi += 1
    $ _before = gs.chars[cid].affection
    $ gs, _passed = sim_rom.resolve_date(gs, CAST, cid, _correct, RULES)
    $ notify_delta(cid, gs.chars[cid].affection - _before)
    "([_correct] of [RULES.quiz_len] right.)"
    return _passed


screen night_choice(cands):
    modal True
    add gui.game_menu_background
    vbox:
        xalign 0.5
        yalign 0.45
        spacing 18
        use heading("Night. Ask someone on a date?", 58)
        text "Dates happen at her favorite place. She'll test how well you know her." size 28 color THEME_PLUM xalign 0.5
        null height 10
        for cid in cands:
            $ h = sim_aff.hearts(gs, cid)
            button at pop_hover:
                xalign 0.5
                xsize 760
                background ui_card("card")
                hover_background ui_card("card_hover")
                padding (34, 16)
                action Return(cid)
                hbox:
                    xfill True
                    use char_chip(cid, 32)
                    hbox:
                        xalign 1.0
                        yalign 0.5
                        use hearts(h, 5, 1.2)
        null height 10
        hbox:
            xalign 0.5
            use pill_button("Stay in tonight", Return("stay"), "white", 30)
