## Grace story beat: she opens up (your first real conversation) (CLAUDE.md §6.1).
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label grace_opens_up:
    show grace neutral at center
    with dissolve

    # PLACEHOLDER
    "The council office is empty except for Grace, who is staring at her planner like it missed a deadline."
    grace "Oh! Hi. Sorry. I just said yes to launching a tenth club. Origami. I don't do origami. I said 'let's just try it' before they finished the sentence."
    grace "Can I tell you something? I don't think I like anything. I like shipping things. I like momentum. Is that a hobby? Is that a personality?"

    menu:
        "\"If you had one free hour, what would you do?\"" (prompt="curious"):
            $ choose("grace", 4, "curious")
            grace "A free hour? I'd— I'd fill it. Side project. Cold emails. A quick hackathon. I'd—"
            grace "I don't know. I genuinely don't know. Is that bad?"
            grace "Maybe nothing? Is nothing allowed? It doesn't scale."
        "\"Being productive isn't a personality. You're more than that.\"" (prompt="honest"):
            $ choose("grace", 3, "honest")
            grace "Ouch. Okay. Fair. Very fair. Ouch."
            grace "...Thank you for saying it, though. Everyone else just says 'crushing it.' Nobody says the ouch part."
        "\"Want help with the origami club?\"" (prompt="practical"):
            $ choose("grace", 2, "practical")
            grace "Yes! Absolutely! Let's move fast, we could have a beta fold by Monday—"
            grace "Wait. You just did the thing I do. Oh no. Is this what I'm like?"

    $ set_flag("grace.opened_up")
    $ reveal("grace", "likes")
    "(You learned what Grace likes. Check your phone.)"

    hide grace
    with dissolve
    return
