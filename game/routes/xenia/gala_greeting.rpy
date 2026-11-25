## Xenia's greeting at the Founders' Gala, before the ending (CLAUDE.md §7).
## Varies with how things stand: lover, girlfriend, romance-locked, or friendly.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label gala_greeting_xenia:
    show xenia neutral at center
    with dissolve
    # PLACEHOLDER
    if gs.chars["xenia"].stage == "lover":
        "Xenia is leaning against a pillar in a black suit with silver star earrings. She isn't looking at her phone."
        xenia "Don't say I clean up nice. I'll throw myself off the roof. ...Okay, you can say it once."
    elif gs.chars["xenia"].stage == "girlfriend":
        xenia "You actually wore that. Bold. I respect it. I'm going to roast it later, but I respect it."
        xenia "The roof's got a better view than this whole party, by the way. Just saying."
    elif gs.chars["xenia"].romance_locked:
        xenia "Oh look, the hall monitor showed up. Here to tell me to keep it down? Pass."
    else:
        xenia "Someone spiked the punch with sparkling water. Worst crime I've seen all year."
    hide xenia
    with dissolve
    return
