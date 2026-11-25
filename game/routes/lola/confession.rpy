## Lola's confession (CLAUDE.md §6.1): plays right after the player passes her
## date quiz. She asks the player to be her girlfriend. The engine sets the stage.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label lola_confession:
    show lola neutral at center
    with dissolve

    # PLACEHOLDER
    "Lola looks at you like you just got four thousand likes."
    lola "You got them all. Even the crossword one. Nobody knows about the crossword one."
    lola "Okay, I'm going to say this without a caption, so don't laugh."
    lola "I like you. Like, offline like you. Will you be my girlfriend? I won't even hard-launch it. Unless you want me to. I'd love to. But only if you want."

    menu:
        "\"Yes. Hard-launch me. Ring light and everything.\"" (prompt="irreverent"):
            $ choose("lola", 3, "irreverent")
            lola "Babe! Oh my god! I'm going to need a whole new ring light. A couples ring light."
        "\"Yes. And I'd say yes offline too.\"" (prompt="warm"):
            $ choose("lola", 3, "warm")
            lola "That's the only place I wanted to hear it."

    "She hugs you, and for once she doesn't check which angle it's from."

    hide lola
    with dissolve
    return
