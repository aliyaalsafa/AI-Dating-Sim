## Pair scene: Xenia + Lola in the cafeteria (CLAUDE.md §4, §6.5).
## Two secret accounts. Lola doesn't know Xenia runs @x_unfiltered and complains
## about it to her face; Xenia could catch Lola's fake fan account.
## Ends by calling pair_done, which shows this pair's two hints from data/mystery.rpy.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label pair_xenia_lola:
    show lola neutral at left
    show xenia neutral at right
    with dissolve

    # PLACEHOLDER
    "Lunch rush. Lola has claimed the only table with good window light. Xenia is at the same table, because it's the only one with an outlet, and she was there first."
    lola "Okay, hiii, sorry, I just need this table for like, a sec, for a lunch-reveal. Sparkle emoji."
    xenia "You said the emoji out loud."
    lola "It's my brand! Speaking of brands, did you see what {i}@x_unfiltered{/i} posted about me?"
    xenia "Can't say I did."
    lola "It said my Homecoming speech had 'the emotional range of a terms-of-service update.' Rude! Like, who even is that? Probably some loser on a roof."
    "Xenia takes an extremely long sip of her drink."
    xenia "Wow. Sounds like a genius, honestly. Real visionary."
    lola "Ugh, you would say that. Anyway, it doesn't matter, because my fans loved it. Look, three hundred likes!"
    "She holds up her phone. Xenia leans in, squints, and scrolls."
    xenia "Huh. Your top fan is @lolamaestan4ever. Joined last month. Follows one person. Posts at the exact same minute you do."
    lola "She's just super dedicated!"
    xenia "Her profile picture is a stock photo of a golden retriever."
    lola "She {i}loves{/i} dogs! That's relatable! Stop scrolling my comments!"

    menu:
        "\"Lola, what's your lunch like when nobody's filming?\"" (prompt="warm"):
            $ choose("lola", 3, "warm")
            $ choose("xenia", -1, "warm")
            lola "Oh. Um. Honestly? Cereal. Like, dry. Out of the box."
            xenia "...Okay, that's the most interesting thing you've ever said. Post that."
        "\"Xenia, you sound like you've met @x_unfiltered.\"" (prompt="pry"):
            $ choose("xenia", 2, "pry")
            xenia "Never heard of 'em. Seems hot, though. Probably funny. Definitely right."
            lola "Ew! Why do you always take its side?"
        "\"That dog fan is one hundred percent you, Lola.\"" (prompt="irreverent"):
            $ choose("xenia", 3, "irreverent")
            $ choose("lola", -1, "irreverent")
            lola "It is NOT! It's a— she's a real— okay, can we talk about literally anything else?"
            xenia "Oh, I'm never talking about anything else again."

    "Lola puts her phone face-down, which you suspect has never happened in public before. She leans in close. Xenia doesn't lean away."
    "They're talking low now, and they've stopped performing for the room, and for you."
    lola "Okay, but real talk. People are saying that account has drafts it never posts. About the new kid."
    xenia "And you clocked my fake followers joke way too fast for someone with zero fake followers. Takes one to know one, Queen."

    call pair_done("xenia_lola")

    hide lola
    hide xenia
    with dissolve
    return
