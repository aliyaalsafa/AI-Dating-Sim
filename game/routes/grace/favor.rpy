## Grace's favor (CLAUDE.md §6.3), offered at affection 50. Two steps:
##   0. Run her Debate Club meeting on the quad, any morning (and keep her secret).
##   1. Report back to her at the council office.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label grace_favor_offer:
    show grace neutral at center
    with dissolve

    # PLACEHOLDER
    grace "Can I ask you something? Not a 'want me to' thing. A me thing."
    grace "Debate Club meets on the quad in the mornings. Could you run it for me, just once? I want to take one hour. For myself. To do... I don't know yet."
    grace "And maybe don't tell anyone why I'm not there? People will think I'm sick. Or broken."

    menu:
        "\"Of course. Take the hour.\"" (prompt="warm"):
            $ choose("grace", 2, "warm")
            grace "Really? Thank you. I've never asked anyone for anything. That was terrifying. Great. Terrifying."
        "\"Only if you promise not to spend it on homework.\"" (prompt="irreverent"):
            $ choose("grace", 1, "irreverent")
            grace "Ha! I— okay. Okay. I promise. Probably."

    $ gs = sim_fav.offer(gs, "grace")
    "(Favor accepted: run Debate Club on the quad some morning, then tell Grace how it went. You have [RULES.favor_deadline_days] days.)"

    hide grace
    with dissolve
    return


label grace_favor_debate:
    scene bg quad
    "Debate Club is six students on a bench, waiting for Grace. You are not Grace."

    show gemma neutral at right
    with dissolve

    # PLACEHOLDER
    gemma "Oh! You're running it? Actually, that's great, I've been meaning to fact-check Grace's last three rulings."
    gemma "Today's resolution, according to the schedule, is: {i}This house believes rest is productive.{/i} Huh. She must have picked that one weeks ago."
    gemma "Wait. Where is Grace? She's never missed a meeting. I have a spreadsheet."

    menu:
        "\"Council business. Very urgent. Very boring.\"" (prompt="concise"):
            $ set_flag("grace.favor_kept_secret")
            gemma "Hm. Plausible. I'll mark it as 'citation needed.'"
        "\"She's taking an hour off. For herself.\"" (prompt="honest"):
            $ set_flag("grace.favor_told")
            gemma "...Grace? Off? I need to update her page."
            "Somewhere nearby, someone laughs and starts typing."
            # PLACEHOLDER: @x_unfiltered post
            $ post("BREAKING: Grace Penelope Turing has taken an hour OFF. Is she sick? Is it the apocalypse? Updates as they happen.")

    "You run the meeting. It's chaos, and the side arguing for rest wins in a landslide."
    $ gs = sim_fav.advance_step(gs, "grace", CAST["grace"]["favor"]["steps"])
    "(Now go tell Grace how it went.)"

    hide gemma
    with dissolve
    return


label grace_favor_report:
    show grace neutral at center
    with dissolve

    # PLACEHOLDER
    if has_flag("grace.favor_told"):
        grace "So. Twelve people asked if I was sick. Xenia posted about it. Gemma updated my wiki page."
        grace "I'm not mad. I'm a little mad. Mostly I'm... fine? It turns out the world didn't end."
    else:
        grace "Nobody noticed. Well — Gemma noticed. She marked me 'citation needed.' But nobody asked."

    grace "Do you want to know what I did with the hour?"
    grace "I sat in the library and read a book I didn't need to read. It was about whales. I don't need to know about whales."
    grace "It was the best hour of my semester."

    $ gs = sim_fav.advance_step(gs, "grace", CAST["grace"]["favor"]["steps"])
    $ bump("grace", sim_aff.scale_gain(10, CAST["grace"]["difficulty"]), "favor_done")
    $ grant("first_favor")
    grace "Thank you. Really. Want me to— no. I'm not offering anything. I'm just saying thank you."

    hide grace
    with dissolve
    return
