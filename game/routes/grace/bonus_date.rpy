## Grace's bonus date (CLAUDE.md §6.4), affection 75+: the council office after
## everyone leaves, her favorite place.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label grace_bonus_date:
    show grace neutral at center
    with dissolve

    # PLACEHOLDER
    "The council office after hours. The lights are off except for one desk lamp and a whiteboard covered in launch dates. Grace is sitting on the floor."
    grace "Hi. Come sit. The floor's very clean. I cleaned it at 2 a.m. while waiting for a build to finish. Obviously."
    grace "Look."
    "She opens her planner. Every hour of the semester is filled in: sprints, standups, a hackathon, a hackathon about hackathons. In tiny, perfect handwriting. Except one."
    "{i}Thursday, 9 p.m.{/i} Blank."
    grace "I didn't fill it. On purpose. It's an experiment — no hypothesis, no success metric. I wanted to see what would happen. And then I wanted you to be there when I found out."

    menu:
        "\"Then let's do absolutely nothing.\"" (prompt="warm"):
            $ choose("grace", 3, "warm")
            grace "Nothing. Okay. I can do nothing. I can crush nothing. How long does nothing usually take? What's the benchmark?"
            "It takes about an hour. Most of it is spent sharing vending-machine crackers and laughing at nothing in particular. She checks her phone only twice, which is a personal record."
        "Make her a numbered list of fun things to do." (prompt="structured"):
            $ choose("grace", 3, "structured")
            grace "One, crackers. Two, more crackers. Three, iterate on crackers... you're mocking me."
            grace "...Keep going. I like it when you mock me. Is that weird? That's probably weird. Ship it anyway."
        "\"What do {i}you{/i} want to do?\"" (prompt="curious"):
            $ choose("grace", 5, "curious")
            grace "What do I—"
            "She thinks about it for a long time. Longer than you've ever seen her think about anything. No pivot. No pitch."
            grace "I want to stay here. With you. Not building anything. Not being useful. Just... here."

    $ set_flag("grace.bonus_date_done")
    grace "Same time next week? I'll leave it blank. I'll leave it blank in pen. That's the most committed I've ever been to not shipping something."

    hide grace
    with dissolve
    return
