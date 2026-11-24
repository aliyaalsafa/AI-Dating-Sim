## Gemma's confession (CLAUDE.md §6.1), affection 90+, after the bonus date.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label gemma_confession:
    show gemma neutral at center
    with dissolve

    # PLACEHOLDER
    "Gemma is standing by the graveyard shelf. She's holding her phone, but the screen is dark."
    gemma "I tried to look something up. For about three days. Every search engine, every database, the whole library. Shen helped. Shen was very confused."
    gemma "The question was: how do you tell someone you like them without it being a project you might quit?"
    gemma "There are zero reliable sources. Actually, there are thousands of sources, and they all disagree, and none of them have met you."
    gemma "So I'm just going to say it, uncited. I like you. A lot. You're the one thing I never wanted to put on the shelf."
    "She holds out a label. It says your name. It's blue."

    menu:
        "\"I like you too. You can quote me on that.\"" (prompt="honest"):
            $ choose("gemma", 3, "honest")
            gemma "Quote you. Primary source. Okay. That's the best citation I've ever had."
        "\"Can I ask follow-up questions? I have so many.\"" (prompt="curious"):
            $ choose("gemma", 4, "curious")
            gemma "Follow-up— yes. Yes! Ask everything. I'll answer everything. That's what I'm best at."
            gemma "Is that a yes, though? I need it to be a yes. I can't look this one up."
            "You tell her it's a yes."

    $ set_flag("gemma.confessed")
    gemma "Okay. I'm putting my phone in the drawer. The red drawer. Red means important."
    "She closes the drawer, and for once she isn't looking at anything but you."

    hide gemma
    with dissolve
    return
