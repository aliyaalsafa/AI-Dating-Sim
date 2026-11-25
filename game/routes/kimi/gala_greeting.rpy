## Kimi's greeting at the Founders' Gala, before the player chooses (CLAUDE.md §7).
## Varies with her stage: lover, girlfriend, romance-locked, or friendly.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label gala_greeting_kimi:
    show kimi neutral at center
    with dissolve
    # PLACEHOLDER
    if gs.chars["kimi"].stage == "lover":
        kimi "[player_name]! Look! I'm wearing it!"
        "The blue {i}1st{/i} ribbon is pinned to her lavender gown, right over her heart. Every club badge is gone. Just the ribbon."
        kimi "I didn't organize a single thing tonight. I just came to be with you."
    elif gs.chars["kimi"].stage == "girlfriend":
        kimi "Hi! You came! I only volunteered for three gala committees, which is very restrained for me."
        kimi "I saved you a seat. Just one. Next to mine."
    elif gs.chars["kimi"].romance_locked:
        kimi "Oh, hi! Welcome! Free snacks are over there. Everything's free. You know how it is."
        "She's already turned away, handing out programs to someone else."
    else:
        kimi "Hi, hi! I'm running the coat check, the playlist, and the dessert table. Simultaneously! Want a cookie?"
    hide kimi
    with dissolve
    return
