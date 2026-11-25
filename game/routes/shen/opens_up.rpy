## Shen story beat: she opens up (your first real conversation) (CLAUDE.md §6.1).
## Library, 3rd floor, the table by the outlet.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label shen_opens_up:
    show shen neutral at center
    with dissolve

    # PLACEHOLDER
    "It's past midnight on the library's third floor. Shen is at the table by the outlet, eating dry instant noodles straight from the packet."
    shen "Kettle's broken. This is fine. It's crunchy. Crunchy is a texture."
    shen "Can I ask you something? Every article about the scholarship transfer says 'matched Grace Turing.' Every one."
    shen "I solved the problems. Me. On this laptop. At this table. And the headline is her name."
    shen "Wait. Let me reconsider. That's not a question. Here's the question: what do people actually see when they see me?"

    menu:
        "\"Someone who wins with whatever she's got.\"" (prompt="honest"):
            $ choose("shen", 4, "honest")
            shen "...Whatever she's got. Yes. That's accurate."
            shen "I'd like that on the headline. It's shorter, too."
        "\"Who cares what they see? What do you see?\"" (prompt="curious"):
            $ choose("shen", 3, "curious")
            shen "Me? Let me think. Step one: tired. Step two: good at this. Step three: hungry."
            shen "Final answer: someone who'd like one week where nobody says Grace's name near mine."
        "\"Want me to fix the kettle?\"" (prompt="practical"):
            $ choose("shen", 3, "practical")
            shen "You can't. It's library property. You'd need a form."
            shen "...You'd fill out the form, wouldn't you. Huh."

    $ set_flag("shen.opened_up")
    $ reveal("shen", "likes")
    "(You learned what Shen likes. Check your phone.)"

    hide shen
    with dissolve
    return
