## Shared gift-giving flow, used by every route hangout (CLAUDE.md §6.4).

label give_gift_flow(cid):
    call screen gift_picker(cid)
    $ gid = _return
    if gid is None:
        return
    if not sim_gifts.can_give(gs, cid, gid):
        "You've already given [cn] something today."
        return
    $ cn = cname(cid)
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
