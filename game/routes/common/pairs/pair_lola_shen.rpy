## Pair scene: Lola + Shen at the quad fountain (CLAUDE.md §4, §6.5).
## Lola wants to film Shen's free notes; Shen hates being content.
## Ends by calling pair_done, which shows this pair's two hints from data/mystery.rpy.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label pair_lola_shen:
    show lola neutral at left
    show shen neutral at right
    with dissolve

    # PLACEHOLDER
    "The quad fountain is Lola's photo spot. Today Shen is sitting on its edge, handing out stapled notes to a line of first-years. Lola has noticed."
    lola "Oh my gosh, hi, sorry, are you giving those away? For {i}free{/i}? That's so content."
    shen "It's not content. It's organic chemistry."
    lola "Okay but what if it was organic chemistry, and content? Like, 'scholarship girl shares her secret study notes,' sparkle, sparkle, link in bio."
    shen "There's no secret. They're notes. You read them. Then you know things."
    lola "Iconic. Can you say that again but slower and looking at the fountain?"
    shen "No."
    "Lola is already filming. Shen holds a stapled packet in front of her face."
    lola "Okay, that's actually a really good shot? Mysterious? Very 'genius who doesn't do interviews'?"
    shen "Wait. Let me reconsider. ...No. Still no."
    lola "Can I at least have a copy? For, like, me? Not for the camera?"
    "Shen pauses. Then she hands Lola a packet. Lola looks at it like no one has given her something without a reason in a long time."
    shen "Page four has an error. I fixed it in the margin."

    menu:
        "\"Shen, why do you give them away for nothing?\"" (prompt="curious"):
            $ choose("shen", 2, "curious")
            $ choose("lola", 1, "curious")
            shen "Knowledge is cheaper when it's shared. Also, people stop asking me questions. Net time saved."
            lola "That's so wholesome and also so rude. I love it."
        "\"Lola, put the camera down. Just read it.\"" (prompt="honest"):
            $ choose("shen", 3, "honest")
            $ choose("lola", -1, "honest")
            lola "Rude! Ugh. Fine. Okay. ...Oh, this is actually really clear?"
            shen "Thank you."
        "\"You two should do a study stream together.\"" (prompt="practical"):
            $ choose("lola", 3, "practical")
            $ choose("shen", 1, "practical")
            lola "YES. Collab! Brains and beauty! Wait, which one am I?"
            shen "One stream. No filters. I choose the topic."

    "The line of first-years thins out. Lola lowers her phone, and the light on it blinks off."
    "Shen notices. Her voice goes flat and quiet, and Lola's drops to match. They seem to have forgotten you're on the other side of the fountain."
    shen "Your voice changes when it's off."
    lola "And you've been carrying the same printout in your bag all week. About a student. You read it like a manual."

    call pair_done("lola_shen")

    hide lola
    hide shen
    with dissolve
    return
