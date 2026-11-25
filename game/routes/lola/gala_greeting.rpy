## Lola's greeting at the Founders' Gala, before the player chooses (CLAUDE.md §7).
## Varies with her stage: lover, girlfriend, romance-locked, or friendly.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label gala_greeting_lola:
    show lola neutral at center
    with dissolve
    # PLACEHOLDER
    if gs.chars["lola"].stage == "lover":
        lola "Babe! Hi! Look, no phone. Just this."
        "She holds up the instant camera. A strip of blurry, awful, perfect photos of the two of you is tucked into her clutch."
        lola "I'm not posting tonight. I want to actually be here. With you."
    elif gs.chars["lola"].stage == "girlfriend":
        lola "There you are! Okay, you look amazing, I'm obsessed, sparkle sparkle."
        lola "I'm only going to film for, like, five minutes. Ten. Then I'm all yours."
    elif gs.chars["lola"].romance_locked:
        lola "Oh, hey! Love that for you. Tag me if you post anything!"
        "The ring light clicks on, and she turns toward someone with a better angle."
    else:
        lola "Hiii! Welcome to the gala! Smile, you're live! Say hi to my followers! All forty-one of them! I mean four thousand!"
    hide lola
    with dissolve
    return
