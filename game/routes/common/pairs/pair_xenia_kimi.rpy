## Pair scene: Xenia + Kimi on the observatory roof at night (CLAUDE.md §4, §6.5).
## They share the roof. This is the only place Kimi's quiet "Moonshot" nod lives.
## Ends by calling pair_done, which shows this pair's two hints from data/mystery.rpy.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label pair_xenia_kimi:
    show xenia neutral at left
    show kimi neutral at right
    with dissolve

    # PLACEHOLDER
    "The observatory roof, past midnight. Xenia is flat on her back by the telescope. Kimi is sitting cross-legged beside her with eleven open laptops."
    xenia "Kimi. It's one a.m. Why are there laptops on my roof."
    kimi "Our roof! We agreed. You get the telescope, I get the outlet, Xeno gets the warm laptop."
    "A black cat is asleep on the warmest keyboard, typing a long line of the letter J into a club newsletter."
    xenia "Xeno, you traitor. I raised you. I named you."
    kimi "You name everything with an X. You named the telescope Xtreme."
    xenia "Because it's xtremely good, dumbass. Don't make me explain branding."
    kimi "Sorry! I'm running the astronomy club and the poetry club at the same time and they've merged by accident. Do you want to hear a haiku about Jupiter?"
    xenia "Absolutely not. ...Is it good?"
    kimi "It's pretty good."
    xenia "Fine. Later. Shut up. Look up."
    "They both go quiet. The moon is enormous tonight, close enough to touch."
    kimi "When I was little I wanted to go there. Not visit. Go. Like it was a place you could just decide to reach."
    xenia "That's the least stupid thing anyone's said on this roof."
    kimi "Everyone else just wants to be first. I wanted to be the one who got there anyway."

    menu:
        "\"You'd both be insufferable astronauts.\"" (prompt="irreverent"):
            $ choose("xenia", 3, "irreverent")
            $ choose("kimi", 1, "irreverent")
            xenia "Correct. I'd name the ship. You know what I'd name it."
            kimi "Is it something with an X?"
            xenia "It's {i}everything{/i} with an X."
        "\"Kimi, what would you do when you got there?\"" (prompt="curious"):
            $ choose("kimi", 3, "curious")
            $ choose("xenia", 1, "curious")
            kimi "Oh! Nobody asks that. Um. I think I'd just sit. By myself. For once."
            xenia "Huh. Same, honestly. Don't tell anyone I said something nice."
        "\"Shouldn't you two be asleep? It's a school night.\"" (prompt="practical"):
            $ choose("xenia", -2, "practical")
            $ choose("kimi", 1, "practical")
            xenia "Wow. Okay, hall monitor. Go back inside and lecture the radiator."

    "Xenia rolls onto her side, pulls out her phone, and scrolls to a folder labeled DRAFTS. She doesn't post anything. She just looks."
    "Kimi glances over. They talk softly, like you've already gone back downstairs."
    kimi "You've been staring at that one for a week."
    xenia "And you went quiet when your swarm got back from wherever you sent it. So we both have a thing."

    call pair_done("xenia_kimi")

    hide xenia
    hide kimi
    with dissolve
    return
