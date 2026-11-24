## Grace's greeting at the Founders' Gala, before the player chooses (CLAUDE.md §7).
## Varies with how things stand: confessed, close (60+), romance-locked, or friendly.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label gala_greeting_grace:
    show grace placeholder at center
    with dissolve
    # PLACEHOLDER
    if has_flag("grace.confessed"):
        grace "Hi. Hi! I finished my speech, so now I'm just a person at a party. It's terrifying."
        grace "I'm not going to tell you what I want tonight. I already did. Your move."
    elif gs.chars["grace"].romance_locked:
        grace "Oh! Hey. Great to see you. If you need any help with your coursework next semester, I'm— actually, never mind."
    elif gs.chars["grace"].affection >= RULES.sweet_min:
        grace "You came! Great! I saved you a seat at three different tables, just in case."
        grace "That's a lot. I know that's a lot. I wanted options."
    else:
        grace "Welcome! Great to see you! Did you like the speech? Be honest. Actually, don't."
    hide grace
    with dissolve
    return
