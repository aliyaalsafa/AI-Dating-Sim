## Shen's greeting at the Founders' Gala, before the player chooses (CLAUDE.md §7).
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label gala_greeting_shen:
    show shen neutral at center
    with dissolve
    # PLACEHOLDER
    if has_flag("shen.confessed"):
        shen "I calculated the probability that you'd come talk to me first tonight. I was wrong. You came second."
        shen "Wait. Let me reconsider. You're here now. The order doesn't matter."
    elif gs.chars["shen"].romance_locked:
        shen "Grace is over there, if that's who you're looking for. Everyone else is."
    elif gs.chars["shen"].affection >= RULES.sweet_min:
        shen "This suit was secondhand. It cost eleven dollars. It looks like it cost two hundred."
        shen "Doing more with less. You can tell people. Actually, don't. Just stand next to me."
    else:
        shen "The free food is good. I've already had four plates. Efficient use of an evening."
    hide shen
    with dissolve
    return
