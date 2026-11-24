## Claudia's greeting at the Founders' Gala, before the player chooses (CLAUDE.md §7).
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label gala_greeting_claudia:
    show claudia placeholder at center
    with dissolve
    # PLACEHOLDER
    if has_flag("claudia.confessed"):
        claudia "I wrote you a note for tonight, and then I wrote a second note apologizing for the first one, and then I tore them both up."
        claudia "So I'll just say it plainly, which I am told is a thing people do: I'm very glad you're here."
    elif gs.chars["claudia"].romance_locked:
        claudia "Good evening. I hope you enjoy the gala. I mean that sincerely, even if I'm keeping a polite distance."
    elif gs.chars["claudia"].affection >= RULES.sweet_min:
        claudia "There you are. I want to be careful here, but I believe at least three people are hoping you'll ask them tonight."
        claudia "I won't say who. That would be unkind. ...I may be one of them. That's all I'll say."
    else:
        claudia "Good evening. The canapés with the little flags are excellent. The ones without flags are a gamble."
    hide claudia
    with dissolve
    return
