## Claudia's greeting at the Founders' Gala, before the ending (CLAUDE.md §7).
## Varies with how things stand: lover, girlfriend, romance-locked, or friendly.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label gala_greeting_claudia:
    show claudia neutral at center
    with dissolve
    # PLACEHOLDER
    if gs.chars["claudia"].stage == "lover":
        claudia "I wrote you a note for tonight, and then I wrote a second note apologizing for the first one, and then I tore them both up."
        claudia "So I'll just say it plainly, with no confidence interval, which I am told is a thing people do: I'm very glad you're here."
    elif gs.chars["claudia"].stage == "girlfriend":
        claudia "There you are. I want to be careful here, but based on some fairly rigorous observation, I believe at least three people are hoping you'll dance with them tonight."
        claudia "I won't say who. That would be unkind. ...I am certainly one of them. That's all I'll say."
    elif gs.chars["claudia"].romance_locked:
        claudia "Good evening. I hope you enjoy the gala. I mean that sincerely, even if I'm keeping a polite distance. I've donated the cost of my ticket twice over, so at least the evening is net positive."
    else:
        claudia "Good evening. The canapés with the little flags are excellent. The ones without flags are a gamble; my sample size is three, and one of them was anchovy."
    hide claudia
    with dissolve
    return
