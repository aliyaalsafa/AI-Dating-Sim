## Xenia's greeting at the Founders' Gala, before the player chooses (CLAUDE.md §7).
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label gala_greeting_xenia:
    show xenia placeholder at center
    with dissolve
    # PLACEHOLDER
    if has_flag("xenia.confessed"):
        "Xenia is leaning against a pillar in a black suit with electric-blue cuffs. She isn't looking at her phone."
        xenia "Don't say I clean up nice. I'll throw myself off the roof. ...Okay, you can say it once."
    elif gs.chars["xenia"].romance_locked:
        xenia "Oh look, the hall monitor showed up. Here to tell me to keep it down? Pass."
    elif gs.chars["xenia"].affection >= RULES.sweet_min:
        xenia "You actually wore that. Bold. I respect it. I'm going to roast it later, but I respect it."
        xenia "The roof's got a better view than this whole party, by the way. Just saying."
    else:
        xenia "Someone spiked the punch with sparkling water. Worst crime I've seen all year."
    hide xenia
    with dissolve
    return
