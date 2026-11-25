## Kimi's confession (CLAUDE.md §6.1): plays right after the player passes her
## date quiz. She asks the player to be her girlfriend. The engine sets the stage.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label kimi_confession:
    show kimi neutral at center
    with dissolve

    # PLACEHOLDER
    "Kimi stares at you for a long moment. Then she bursts out laughing, and then she's somehow crying a little too, all at once. Parallel processing."
    kimi "You got every single one. You {i}listened{/i}. Nobody listens to me. They listen to what I can give them."
    kimi "Okay. I'm going to say it fast, the way I say everything, so I don't lose my nerve."
    kimi "I like you. A lot. More than all twelve clubs combined. Will you be my girlfriend? Just mine. Not a club. No sign-up sheet."

    menu:
        "\"Yes. And I'm not sharing you with the Napping Society.\"" (prompt="warm"):
            $ choose("kimi", 3, "warm")
            kimi "Ha! They'll survive. They'll nap through it."
        "\"Yes. Step one: you. There is no step two.\"" (prompt="structured"):
            $ choose("kimi", 3, "structured")
            kimi "That's the best list I've ever heard. I'm writing it down. On everything."

    "She throws her arms around you. For a second it feels like a whole swarm of people is hugging you at once."

    hide kimi
    with dissolve
    return
