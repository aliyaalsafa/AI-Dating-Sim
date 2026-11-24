## Gemma story beat at affection 25: she opens up (CLAUDE.md §6.1).
## The robotics lab and her shelf of dead prototypes.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label gemma_opens_up:
    show gemma placeholder at center
    with dissolve

    # PLACEHOLDER
    "There's a shelf at the back of the robotics lab you've never noticed. It's full of half-built gadgets, each one with a neat little label and a date."
    "{i}Desk Drone, three weeks.{/i} {i}Smart Mug, eleven days.{/i} {i}Friend-Finder App, discontinued.{/i}"
    gemma "Oh. You found the shelf. I call it the archive. Actually, I call it the graveyard. Actually, I don't call it anything, I just don't look at it."
    gemma "Every one of these was going to be amazing. And then a newer, more amazing idea came along. So I... moved on."
    gemma "I can find the answer to almost anything in under a minute. I just can't figure out why I never finish."

    menu:
        "\"Tell me about each one. Start with the drone.\"" (prompt="curious"):
            $ choose("gemma", 4, "curious")
            gemma "The drone? It was going to follow you around and take photos. So you'd never miss a moment."
            gemma "It kept flying into the ceiling. I think it was trying to escape me. Ha."
            "She goes through every single one. Her voice gets faster with each prototype. By the end she's smiling."
        "\"Maybe you stop because you're scared it won't be good enough?\"" (prompt="honest"):
            $ choose("gemma", 3, "honest")
            gemma "What? No. That's not— I'd need data to support that."
            gemma "...I have data. The data is this whole shelf. Ugh."
        "\"So pick one and finish it. Simple.\"" (prompt="practical"):
            $ choose("gemma", 2, "practical")
            gemma "Simple. Sure. Simple. I'll just do the one thing I've never done. Simply."
            gemma "Sorry. That came out sharp. It's not you. It's the shelf."

    $ set_flag("gemma.opened_up")
    $ reveal("gemma", "likes")
    "(You learned what Gemma likes. Check your phone.)"

    hide gemma
    with dissolve
    return
