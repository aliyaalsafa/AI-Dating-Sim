## Grace's greeting at the Founders' Gala, before the ending (CLAUDE.md §7).
## Varies with how things stand: lover, girlfriend, romance-locked, or friendly.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label gala_greeting_grace:
    show grace neutral at center
    with dissolve
    # PLACEHOLDER
    if gs.chars["grace"].stage == "lover":
        grace "Hi. Hi! I finished my speech, so now I'm just a person at a party. No agenda. No networking. It's terrifying."
        grace "I'm not going to tell you what I want tonight. I already did. Your move."
    elif gs.chars["grace"].stage == "girlfriend":
        grace "You came! Great! I saved you a seat at three different tables, just in case. Redundancy is a best practice."
        grace "That's a lot. I know that's a lot. I wanted options. Optionality!"
    elif gs.chars["grace"].romance_locked:
        grace "Oh! Hey. Great to see you. If you need any help with your coursework next semester, I've got bandwidth— actually, never mind."
    else:
        grace "Welcome! Great to see you! Did you like the speech? I wrote it in forty minutes. Be honest. Actually, don't. Feedback after the launch."
    hide grace
    with dissolve
    return
