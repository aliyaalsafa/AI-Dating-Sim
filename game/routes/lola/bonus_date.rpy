## Lola's night date (CLAUDE.md §6.1): the quad fountain after golden hour has
## passed, phone away. The engine runs her date quiz afterward.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label lola_bonus_date:
    show lola neutral at center
    with dissolve

    # PLACEHOLDER
    "The quad at night. Golden hour ended a long time ago. The fountain is lit from underneath, and Lola is sitting on its edge in a hoodie."
    lola "Hi. Don't freak out. My phone's in my dorm. On airplane mode. In a drawer. Under a sweater."
    lola "I've been having withdrawals for forty minutes. I keep framing things with my hands."
    "She makes a little rectangle with her fingers and looks at you through it."
    lola "Golden hour's my favorite time here. Everyone knows that. It's in my bio. But I wanted to see if I liked it after. When there's no good light. When it's just us."

    menu:
        "\"You look better without the good light.\"" (prompt="warm"):
            $ choose("lola", 4, "warm")
            lola "That's either the nicest thing anyone's ever said to me or a really sneaky roast."
            lola "...It's the nice one. I can tell. You're bad at sneaky."
        "Dare her to put her feet in the fountain." (prompt="irreverent"):
            $ choose("lola", 4, "irreverent")
            lola "It's {i}freezing{/i}— okay, fine, fine!"
            "She shrieks, then laughs so hard she nearly falls in. Nobody films it. It's the best thing that's happened all week."
        "\"What do you actually like, when nobody's watching?\"" (prompt="curious"):
            $ choose("lola", 2, "curious")
            lola "Honestly? Crosswords. The really hard ones. I'm so bad at them. I'd never post it."
            lola "Don't tell anyone. My brand is 'sparkle,' not 'seven-letter word for persistent.'"

    lola "Okay, babe, pop quiz. Let's see if you were paying attention to me. The real me. Not the feed."

    hide lola
    with dissolve
    return
