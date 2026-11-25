## Shen's greeting at the Founders' Gala, before the ending (CLAUDE.md §7).
## Varies with how things stand: lover, girlfriend, romance-locked, or friendly.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label gala_greeting_shen:
    show shen neutral at center
    with dissolve
    # PLACEHOLDER
    if gs.chars["shen"].stage == "lover":
        shen "I calculated the probability that you'd come talk to me first tonight. I was wrong. You came second."
        shen "Wait. Let me reconsider. You're here now. The order doesn't matter."
    elif gs.chars["shen"].stage == "girlfriend":
        shen "This suit was secondhand. It cost eleven dollars. It looks like it cost two hundred."
        shen "Doing more with less. You can tell people. Actually, don't. Just stand next to me."
    elif gs.chars["shen"].romance_locked:
        shen "Grace is over there, if that's who you're looking for. Everyone else is."
    else:
        shen "The free food is good. I've already had four plates. Efficient use of an evening."
    hide shen
    with dissolve
    return
