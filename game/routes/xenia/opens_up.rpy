## Xenia story beat at affection 25: she opens up (CLAUDE.md §6.1). On the
## observatory roof at night.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label xenia_opens_up:
    show xenia placeholder at center
    with dissolve

    # PLACEHOLDER
    "The observatory roof, close to midnight. Xenia is lying flat on her back next to a battered telescope with XENITH stenciled down the side in silver paint."
    xenia "Oh, great. You found the roof. Now I have to kill you. Sit down, it's less effort."
    xenia "See that one? The little red smudge? That's Mars. Everyone thinks it's a star. It isn't. It's just bright enough to fool people."
    xenia "Sometimes I think the stars are the only things on this campus that aren't pretending."
    xenia "...Forget I said that. That was a weird thing to say. I'm tired. The telescope makes me sentimental. It's a known defect."

    menu:
        "\"No. I'm not forgetting it. Say more.\"" (prompt="honest"):
            $ choose("xenia", 4, "honest")
            xenia "Ugh. You're one of those. Fine."
            xenia "Everybody down there is doing a bit. Grace is doing 'helpful.' I'm doing 'mean.' The stars just... burn. No bit. They don't care who's watching."
            xenia "I like that. I like things that don't care who's watching. That's the whole thing. Don't make it a whole thing."
        "\"Sentimental? You? I'm telling the whole feed.\"" (prompt="irreverent"):
            $ choose("xenia", 3, "irreverent")
            xenia "You wouldn't dare. I have dirt on you. I have dirt on {i}everyone{/i}."
            xenia "...You get one free pass, because the sky's clear and I'm in a good mood. Don't spend it all at once."
        "\"Your telescope is called XENITH?\"" (prompt="curious"):
            $ choose("xenia", 2, "curious")
            xenia "Zenith, but with an X. Obviously. My cat's Xeno, my bike's the Xpedition, and my telescope's XENITH. It's a brand."
            xenia "I rebuilt it from a dumpster scope. Took a whole summer. Best summer of my life, and I spent it alone in a garage. Make of that what you will."
        "\"That's really beautiful, Xenia. Thank you for sharing.\"" (prompt="warm"):
            $ choose("xenia", 1, "warm")
            xenia "Okay, gross, stop it, you sound like a greeting card. A nice one. Stop it anyway."

    $ set_flag("xenia.opened_up")
    $ reveal("xenia", "likes")
    "(You learned what Xenia likes. Check your phone.)"

    hide xenia
    with dissolve
    return
