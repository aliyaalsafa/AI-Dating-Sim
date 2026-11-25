## Gift giving (CLAUDE.md §6.3). Giving a gift is a free action when you
## visit someone: it doesn't use up the time slot. Her special gift turns a
## girlfriend into a lover and plays <id>_lover.

label offer_gift(cid):
    $ _cn = cname(cid)
    menu:
        "Give [_cn] a gift first?"
        "Give her a gift":
            call give_gift_flow(cid)
        "Not now":
            pass
    return


label give_gift_flow(cid):
    $ cn = cname(cid)
    call screen gift_picker(cid)
    $ gid = _return
    if gid not in SHOP:
        return

    if gid == CAST[cid]["special_gift"]:
        if sim_rom.can_become_lover(gs, CAST, cid):
            $ gs = sim_rom.give_special(gs, CAST, cid)
            $ grant("first_lover")
            $ sfx("achievement")
            call expression cid + "_lover"
            "(You and [cn] are lovers now.)"
            return
        elif gs.chars[cid].stage == "lover":
            # PLACEHOLDER
            "[cn] already has one. She keeps it somewhere you can always see it."
            return
        else:
            # PLACEHOLDER
            "[cn] turns it over in her hands, smiles, and gives it back. \"Not yet. Ask me again when we're... you know. Official.\""
            return

    if not sim_gifts.can_give(gs, cid, gid):
        "You've already given [cn] something today."
        return
    $ kind = sim_gifts.reaction(CAST, cid, gid)
    $ before = gs.chars[cid].affection
    $ gs = sim_gifts.give(gs, CAST, cid, gid, RULES)
    $ last_delta = gs.chars[cid].affection - before
    $ notify_delta(cid, last_delta)
    $ grant("first_gift")
    # PLACEHOLDER: per-character gift reactions
    if kind == "loved":
        $ grant("loved_gift")
        "[cn]'s whole face lights up. She loves it."
    elif kind == "liked":
        "[cn] smiles. Good pick."
    elif kind == "disliked":
        "[cn] takes it politely, but... that one missed."
    else:
        "[cn] thanks you. It's a nice, if generic, gesture."
    return
