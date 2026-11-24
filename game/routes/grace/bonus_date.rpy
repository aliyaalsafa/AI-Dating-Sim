## Grace's bonus date (CLAUDE.md §6.4), affection 75+: the council office after
## everyone leaves, her favorite place.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label grace_bonus_date:
    show grace placeholder at center
    with dissolve

    # PLACEHOLDER
    "The council office after hours. The lights are off except for one desk lamp, and Grace is sitting on the floor."
    grace "Hi. Come sit. The floor's very clean. I cleaned it. Obviously."
    grace "Look."
    "She opens her planner. Every hour of the semester is filled in, in tiny, perfect handwriting. Except one."
    "{i}Thursday, 9 p.m.{/i} Blank."
    grace "I didn't fill it. On purpose. I wanted to see what would happen. And then I wanted you to be there when I found out."

    menu:
        "\"Then let's do absolutely nothing.\"" (prompt="warm"):
            $ choose("grace", 3, "warm")
            grace "Nothing. Okay. I can do nothing. How long does nothing usually take?"
            "It takes about an hour. Most of it is spent sharing vending-machine crackers and laughing at nothing in particular."
        "Make her a numbered list of fun things to do." (prompt="structured"):
            $ choose("grace", 3, "structured")
            grace "One, crackers. Two, more crackers. Three... you're mocking me."
            grace "...Keep going. I like it when you mock me. Is that weird? That's probably weird."
        "\"What do {i}you{/i} want to do?\"" (prompt="curious"):
            $ choose("grace", 5, "curious")
            grace "What do I—"
            "She thinks about it for a long time. Longer than you've ever seen her think about anything."
            grace "I want to stay here. With you. Not being useful. Just... here."

    $ set_flag("grace.bonus_date_done")
    grace "Same time next week? I'll leave it blank. I'll leave it blank in pen."

    hide grace
    with dissolve
    return
