## Kimi's favor (CLAUDE.md §6.3). Two steps:
##   0. Get Grace to sign a room swap at the student council office.
##   1. Tell Kimi at the student activities hall.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label kimi_favor_offer:
    show kimi neutral at center
    with dissolve

    # PLACEHOLDER
    kimi "So. Funny story. All twelve of my clubs booked the activities hall for the same hour. Thursday at four."
    kimi "Because I booked them. All at once. In parallel. It felt very efficient at the time."
    kimi "Grace can sign a room swap, but every time I ask, she says 'Great question!' and gives me three options and none of them are 'yes.'"
    kimi "Could you ask her? People listen to you. Well. Grace listens to whoever talked last, so just... talk last."

    menu:
        "\"Write down which clubs need which rooms, and I'll take it to her.\"" (prompt="practical"):
            $ choose("kimi", 3, "practical")
            kimi "Already done! I made a spreadsheet. And a backup spreadsheet. And a spreadsheet explaining the spreadsheets."
        "\"How did twelve clubs end up in one room?\"" (prompt="curious"):
            $ choose("kimi", 2, "curious")
            kimi "I said yes twelve times in one second. It's a gift. It's also a problem. It's a gift-problem."

    $ gs = sim_fav.offer(gs, "kimi")
    "(Favor accepted: get Grace to sign a room swap at the council office, then tell Kimi. You have [RULES.favor_deadline_days] days.)"

    hide kimi
    with dissolve
    return


label kimi_favor_swap:
    scene bg council_office
    show grace neutral at center
    with dissolve

    # PLACEHOLDER
    grace "Hi! Welcome to the council office! How can I help? Want me to: one, check room bookings, two, explain room bookings, or three—"
    "You hand her Kimi's spreadsheet. And the backup. And the spreadsheet about the spreadsheets."
    grace "Oh. Kimi. Twelve clubs, one room. She's asked me four times. I keep meaning to say yes, but then someone else talks and I agree with them instead."

    menu:
        "\"Kimi does more for this campus than anyone. Sign it.\"" (prompt="honest"):
            $ choose("grace", 2, "honest")
            grace "That's... true. She runs the bake sales. All of them. I take credit for some of them in my reports. Oh no."
        "Lay out a step-by-step swap that keeps every club happy." (prompt="structured"):
            $ choose("grace", 2, "structured")
            grace "Step one, Chess to Room B. Step two, Pottery to the art annex. Step three... oh, this is beautiful. This is a numbered list. You speak my language."

    "Grace signs the swap with a flourish. She initials every page. Twice."
    grace "Tell Kimi I'm sorry it took so long. And tell her the bake sale numbers in my reports were hers. I'll fix them."
    $ gs = sim_fav.advance_step(gs, "kimi", CAST["kimi"]["favor"]["steps"], RULES)
    "(Now go tell Kimi at the activities hall.)"

    hide grace
    with dissolve
    return


label kimi_favor_report:
    scene bg activities_hall
    show kimi neutral at center
    with dissolve

    # PLACEHOLDER
    "You hand Kimi the signed swap. She reads it three times, then holds it up to the light like it might be a forgery."
    kimi "She signed it. She signed it! Twelve clubs, twelve rooms, zero fistfights!"
    kimi "Do you know how many people I've helped this semester? I counted. Two hundred and six."
    kimi "Do you know how many helped me back? One. You."

    $ gs = sim_fav.advance_step(gs, "kimi", CAST["kimi"]["favor"]["steps"], RULES)
    $ bump("kimi", sim_aff.scale_gain(RULES.favor_done_bonus, CAST["kimi"]["difficulty"]), "favor_done")
    $ grant("first_favor")
    kimi "I'm adding you to every club's honorary member list. All twelve. You don't have to come. I just want your name on things."

    hide kimi
    with dissolve
    return
