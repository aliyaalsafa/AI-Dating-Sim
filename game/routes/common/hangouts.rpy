## Generic, repeatable hangout used until each route has real scenes (M2–M3).
## Exercises every M1 system: prompt styles, deal-breakers, unlocks, favors, gifts.
##
## Every line in HANGOUT_LINES is a PLACEHOLDER for the owner to rewrite.
## {name} is replaced with the player's name.

init -2 python:

    HANGOUT_LINES = {
        "grace": {
            # PLACEHOLDER: Grace hangout lines
            "first": "Oh! You're the new transfer! Great question — I mean, great to meet you. I'm Grace, student body president.",
            "greet": "Hi, {name}! Want me to: 1) catch you up on council news, 2) quiz you for midterms, or 3) both?",
            "good": "Huh. Nobody's ever said that to me before. I think I... like it?",
            "bad": "Great point — no, wait. I'm sorry, I think I got that wrong. Can we try again?",
            "opens_up": "Can I tell you something? I color-code my planner because if I stop, I don't know what I'd want to do instead.",
            "dealbreaker_option": "Ask her to just write your essay for you.",
            "dealbreaker_react": "Of course! I'd be happy to... Actually. You know what? No. I'm not a homework service.",
            "favor_ask": "Would you... do me a favor? {desc} I've never asked anyone that before.",
            "favor_step": "You did it? Really? I spent a whole hour doing nothing. It was terrifying. Thank you.",
        },
        "xenia": {
            # PLACEHOLDER: Xenia hangout lines
            "first": "Oh great, the human. Don't look so lost, it makes you an easy target. I'm Xenia. That's Xeno. He bites.",
            "greet": "You again. Either you like me or you've got no other friends. Both are tragic.",
            "good": "Ha! Okay, that was actually funny. Don't let it go to your head.",
            "bad": "Wow. That was the most sanitized thing I've heard all week, and I go to school with Grace.",
            "opens_up": "Sometimes I think the stars are the only things on this campus that aren't pretending. ...Forget I said that.",
            "dealbreaker_option": "Tell her she should really tone it down.",
            "dealbreaker_react": "Oh, a lecture. Cool. Super original. The door's that way.",
            "favor_ask": "Okay, don't make it weird, but I need help. {desc} You in or not?",
            "favor_step": "You actually pulled it off. Huh. Maybe you're not completely useless.",
        },
        "claudia": {
            # PLACEHOLDER: Claudia hangout lines
            "first": "Hello. You must be the new student. I'm Claudia, and I'm so sorry, I've already heard three rumors about you. I'll only tell you the kind ones.",
            "greet": "{name}, how lovely. I want to be careful here, but I may have something you ought to know.",
            "good": "That's a wonderfully honest thing to say. Thank you. I mean that, at some length.",
            "bad": "Ah. I think I'd rather not, if that's all right. I'm sorry. I'm sorry for apologizing, too.",
            "opens_up": "People assume I'm careful because I have no opinions. I have so many opinions. Most of them are about ducks.",
            "dealbreaker_option": "Try to trick a secret out of her.",
            "dealbreaker_react": "I see what you're doing, and I'm going to decline, very politely, and with some disappointment.",
            "favor_ask": "May I ask something of you? {desc} I'd understand completely if you'd rather not.",
            "favor_step": "You delivered it. And you didn't read it. I'll write you a note about how much that means.",
        },
        "gemma": {
            # PLACEHOLDER: Gemma hangout lines
            "first": "Hi! You're the new transfer, right? Let me look that up — actually, I already know. Gemma. I run the wiki. Your page is a stub.",
            "greet": "{name}! Actually, perfect timing, I just started a new project. Well, three.",
            "good": "Oh, that's so interesting! Hold on, I'm citing you in my notes.",
            "bad": "Hm. Actually, according to my sources, that's not how that works. Sorry. Kind of.",
            "opens_up": "Want to know a secret? I have never once finished a project. Not one. The shelf's getting full.",
            "dealbreaker_option": "Call her 'Bard'.",
            "dealbreaker_react": "Nope. No. We don't say that name. That was a different era. A dark era.",
            "favor_ask": "Okay, big ask. {desc} If I start a new one, you're allowed to stop me.",
            "favor_step": "It's done. It's actually done. I'm going to label it. I'm going to label it so hard.",
        },
        "shen": {
            # PLACEHOLDER: Shen hangout lines
            "first": "You're the transfer. Wait. Let me reconsider. You're the other transfer. Shen. Notes are free if you need them.",
            "greet": "{name}. You have ten minutes. Use them well.",
            "good": "...That's efficient. I appreciate efficient.",
            "bad": "Wait. Let me reconsider. No. That wasted both our time.",
            "opens_up": "Everyone here talks about what I don't have. Nobody asks what I did with what I had.",
            "dealbreaker_option": "Say she's basically the next Grace.",
            "dealbreaker_react": "I am not 'the next' anyone. We're done here.",
            "favor_ask": "I need help. Fairly. {desc} No shortcuts.",
            "favor_step": "You found out, and you did it the right way. Thank you. I mean it.",
        },
    }


label generic_hangout(cid):
    show expression placeholder_sprite(cid) as lovein at center
    with dissolve

    if not has_flag("met_" + cid):
        $ set_flag("met_" + cid)
        $ line(cid, "first")
        if all(has_flag("met_" + c) for c in CAST):
            $ grant("all_met")
    else:
        $ line(cid, "greet")

    $ db_option = HANGOUT_LINES[cid]["dealbreaker_option"]
    $ cn = cname(cid)
    $ last_delta = 0
    $ reacted = False

    menu:
        "Tell her what you actually think." (prompt="honest"):
            $ choose(cid, 3, "honest")
        "Crack a joke at her expense." (prompt="irreverent"):
            $ choose(cid, 3, "irreverent")
        "Suggest a plan, point by point." (prompt="structured"):
            $ choose(cid, 3, "structured")
        "Ask what she's been curious about lately." (prompt="curious"):
            $ choose(cid, 3, "curious")
        "Keep it short and get to the point." (prompt="concise"):
            $ choose(cid, 3, "concise")
        "[db_option]":
            $ hit_dealbreaker(cid)
            $ line(cid, "dealbreaker_react")
            $ reacted = True
            $ post("Just watched the new kid crash and burn with %s. Brutal. Iconic." % cname(cid))  # PLACEHOLDER
        "Give her a gift.":
            call give_gift_flow(cid)
            $ reacted = True

    if not reacted:
        if last_delta > 0:
            $ line(cid, "good")
        elif last_delta < 0:
            $ line(cid, "bad")

    # Threshold unlocks (CLAUDE.md §6.1)
    if sim_aff.unlocks(gs, cid, RULES)["opens_up"] and "likes" not in gs.chars[cid].known:
        $ line(cid, "opens_up")
        $ reveal(cid, "likes")
        "(You learned what [cn] likes. Check your phone.)"

    if sim_fav.can_offer(gs, cid, RULES):
        $ line(cid, "favor_ask", desc=CAST[cid]["favor"]["desc"])
        $ gs = sim_fav.offer(gs, cid)
        "(Favor accepted. You have [RULES.favor_deadline_days] days.)"

    hide lovein
    with dissolve
    return


label generic_favor_step(cid):
    show expression placeholder_sprite(cid) as lovein at center
    with dissolve
    # PLACEHOLDER: real multi-step favors per character are written in M2–M3.
    "You report back about the favor."
    $ gs = sim_fav.advance_step(gs, cid, CAST[cid]["favor"]["steps"])
    if gs.chars[cid].favor_status == "done":
        $ line(cid, "favor_step")
        $ bump(cid, sim_aff.scale_gain(10, CAST[cid]["difficulty"]), "favor_done")
        $ grant("first_favor")
    hide lovein
    with dissolve
    return


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
