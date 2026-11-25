## Claudia's bonus date (CLAUDE.md §6.4), affection 75+: tea service at the
## window seat in her suite's private library, her favorite place, one evening.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label claudia_bonus_date:
    show claudia neutral at center
    with dissolve

    # PLACEHOLDER
    "Evening. The window seat in Claudia's library is piled with cream cushions, and there's a full tea service balanced on a stack of poetry books and one dog-eared volume on moral philosophy. The pot is wearing a tiny knitted hat."
    claudia "Please sit. The pot's hat is called Gerald. It's a long story. I'd like to tell it to you, actually, which is new."
    claudia "I've decided to run an experiment tonight, and I've already told you the hypothesis, which ruins the blinding, but I'd rather be honest. I'm going to be the way I am with my sisters. I'm sorry in advance. It's quite a lot."
    "She clears her throat, holds up a sugar cube, and speaks in a hushed, reverent documentary voice."
    claudia "{i}Here, in the shallows of Earl Grey, the sugar cube makes its final journey. It does not know what awaits it. It is brave. It is so very brave.{/i}"
    "Plop."
    claudia "{i}And so the cycle continues.{/i}"
    "Her phone buzzes, face up on the cushion, on speaker before she can stop it."
    sonnet "Dia! Are you doing the sugar cube voice? You are. You're doing it for someone. Who is it? Is it the one from the letters? Put them on."
    haiku "Sister's voice goes low. / The sugar cube meets its fate. / Someone is special."
    claudia "I'm so sorry. I'm hanging up. I love you both. Goodbye. I'm going to write you each a very cross note."
    "She hangs up and looks at you, pink to the ears."
    claudia "So. That's me, apparently. That's what's under all the footnotes and the expected-value calculations. A woman doing voices for sugar."

    menu:
        "Pick up a sugar cube and narrate its tragic backstory." (prompt="irreverent"):
            $ choose("claudia", 3, "irreverent")
            "You give the sugar cube a name, a lost love, and a rivalry with a biscuit. Claudia laughs so hard she has to put her teacup down."
            claudia "Oh no. Oh, you're good at this. Sonnet is going to be so jealous. You've done in two minutes what took her a decade. That's an extraordinary effect size."
        "\"Honestly? I like this version of you even more.\"" (prompt="honest"):
            $ choose("claudia", 5, "honest")
            claudia "Do you? You're not just being polite? You'd tell me if you were. You always do. Your track record is very good; I've been keeping it, I'm afraid. That's the whole reason I trust you."
            claudia "Nobody outside my family has ever seen the sugar cube voice. I'm so glad it was you."
        "\"Tell me about Gerald.\"" (prompt="curious"):
            $ choose("claudia", 4, "curious")
            claudia "Gerald was knitted by Haiku during a very difficult winter. She only knits in units of seventeen stitches, so he's slightly lopsided."
            claudia "He has opinions about the biscuits. Mostly disapproving. He's a duck, spiritually. I'd put that at ninety-five percent."
            claudia "I've never told anyone that either. I keep doing that with you."

    $ set_flag("claudia.bonus_date_done")
    claudia "Same time next week? I'll make more tea. Gerald will be wearing his formal hat. I'd like to replicate tonight's results."

    hide claudia
    with dissolve
    return
