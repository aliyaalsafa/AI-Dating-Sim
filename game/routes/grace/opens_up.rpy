## Grace story beat at affection 25: she opens up (CLAUDE.md §6.1).
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label grace_opens_up:
    show grace neutral at center
    with dissolve

    # PLACEHOLDER
    "The council office is empty except for Grace, who is staring at her planner like it owes her money."
    grace "Oh! Hi. Sorry. I just agreed to chair a tenth club. Origami. I don't do origami."
    grace "Can I tell you something? I don't think I like anything. I like being useful. Is that a hobby? Is that a personality?"

    menu:
        "\"If you had one free hour, what would you do?\"" (prompt="curious"):
            $ choose("grace", 4, "curious")
            grace "A free hour? I'd— I'd fill it. With something useful. I'd—"
            grace "I don't know. I genuinely don't know. Is that bad?"
            grace "Maybe nothing? Is nothing allowed?"
        "\"Being useful isn't a personality. You're more than that.\"" (prompt="honest"):
            $ choose("grace", 3, "honest")
            grace "Ouch. Okay. Fair. Very fair. Ouch."
            grace "...Thank you for saying it, though. Nobody says the ouch part."
        "\"Want help with the origami club?\"" (prompt="practical"):
            $ choose("grace", 2, "practical")
            grace "Yes! Absolutely! Thank you so much—"
            grace "Wait. You just did the thing I do. Oh no. Is this what I'm like?"

    $ set_flag("grace.opened_up")
    $ reveal("grace", "likes")
    "(You learned what Grace likes. Check your phone.)"

    hide grace
    with dissolve
    return
