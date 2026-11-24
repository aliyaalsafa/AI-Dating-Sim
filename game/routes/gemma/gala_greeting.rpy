## Gemma's greeting at the Founders' Gala, before the player chooses (CLAUDE.md §7).
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label gala_greeting_gemma:
    show gemma neutral at center
    with dissolve
    # PLACEHOLDER
    if has_flag("gemma.confessed"):
        gemma "Okay, so I made a list of reasons tonight would go well, and it's color-coded, and every color says the same thing."
        gemma "It says you. All four colors. That's never happened before."
    elif gs.chars["gemma"].romance_locked:
        gemma "Hi. I'm livestreaming. Please don't— just. Don't say the B-word on camera."
    elif gs.chars["gemma"].affection >= RULES.sweet_min:
        gemma "You're here! I'm filming! Actually, I'm filming {i}you{/i}. For the wiki. That's a normal thing to say."
        gemma "Also I finished something this semester. Did I tell you? I'm telling everyone."
    else:
        gemma "Fun fact! The first Founders' Gala had forty guests. Actually, forty-two. Actually, let me look that up. No, it was forty."
    hide gemma
    with dissolve
    return
