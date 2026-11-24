## Xenia's bonus date (CLAUDE.md §6.4), affection 75+: the observatory roof at
## night, her favorite place. She shows you one of her unposted star notes.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label xenia_bonus_date:
    show xenia placeholder at center
    with dissolve

    # PLACEHOLDER
    "The observatory roof. Xenia has dragged up two beanbags, a thermos of instant noodles and a cat carrier. Inside the carrier, Xeno glares at you."
    xenia "Xeno wanted to meet you properly. He's decided you're tolerable. That's his highest rating. He gave it to a moth once."
    xenia "Okay. I'm going to show you something, and if you laugh, I'm pushing you off this roof. Lovingly. But firmly."
    "She pulls a phone out of her hoodie pocket and opens a notes app. There are dozens of drafts. None of them have been posted."
    "She turns the screen toward you."
    "{i}Tonight Vega was so bright it looked like it was trying to say something. The light hitting my eyes left it twenty-five years ago. Someone looked up the night it left and didn't know I'd be here to catch it. Maybe nothing's ever really lost. Maybe it's just still on its way.{/i}"
    xenia "So. That's... I write those. Sometimes. A lot. I never post them. Obviously. Can you imagine? My brand would {i}die{/i}."

    menu:
        "\"Xenia. That's genuinely beautiful. I mean it.\"" (prompt="honest"):
            $ choose("xenia", 5, "honest")
            xenia "Don't—"
            "She stops. She doesn't make a joke. For a long moment, she just looks at you, and then back at the sky."
            xenia "...Okay. Thank you. Nobody's ever read one. You're the first. That's a weird thing to be the first at."
            xenia "Don't make it weird. ...You can make it a little weird."
        "\"Your brand was already dying. This is a glow-up.\"" (prompt="irreverent"):
            $ choose("xenia", 3, "irreverent")
            xenia "Excuse me? My brand is {i}thriving{/i}. My brand is a supernova."
            xenia "...Which is technically a dying star. Damn it. You walked me right into that."
            xenia "Okay. You're allowed to read one more. Only because you didn't get mushy about it."
        "\"How many of these have you written?\"" (prompt="pry"):
            $ choose("xenia", 3, "pry")
            xenia "Four hundred and twelve. Not that I counted. I counted."
            xenia "One for every night I came up here instead of sleeping. Some of them are just 'cloudy, rude.' But most of them are... like that one."

    $ set_flag("xenia.bonus_date_done")
    xenia "Same roof next week? Bring better noodles. Xeno has standards. So do I. Low ones, apparently, since I invited you."

    hide xenia
    with dissolve
    return
