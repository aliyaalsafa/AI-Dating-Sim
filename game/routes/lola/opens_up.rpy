## Lola story beat: she opens up (CLAUDE.md §4: she isn't as popular as she
## thinks, and secretly runs a fake fan account that hypes her posts). The engine
## calls lola_favor_offer right after this scene.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label lola_opens_up:
    show lola neutral at center
    with dissolve

    # PLACEHOLDER
    "Lola is sitting on the edge of the fountain, scrolling, and not smiling. You didn't know her face could do that."
    lola "Oh! Babe. Hi. Don't look at my screen."
    "You've already seen it. Two phones. On one, her own account. On the other, an account called @lolamae_stan_4ever, typing 'QUEEN!!! heart-eyes heart-eyes heart-eyes' under her latest post."
    lola "Okay. So. You saw that."
    lola "Forty-one likes. My last post got forty-one likes. Mysterious Lola got four thousand. Regular me gets forty-one, and nine of them are me."
    lola "Everyone thinks I'm the most popular girl on campus. {i}I{/i} thought I was the most popular girl on campus. Turns out it's mostly just... me, cheering for me."

    menu:
        "\"I don't care about the likes. I like hanging out with you.\"" (prompt="warm"):
            $ choose("lola", 4, "warm")
            lola "You're saying that because I'm sad."
            lola "...You're not, though. Are you. You never even look at my phone when we talk."
        "\"Nine of them? Your stan account needs a raise.\"" (prompt="irreverent"):
            $ choose("lola", 3, "irreverent")
            lola "She's unpaid! She's very dedicated! She comments within four seconds!"
            "She's laughing now. It's the real laugh, the one with a snort in it that she always edits out."
        "\"Why do you need everyone to like you?\"" (prompt="honest"):
            $ choose("lola", 1, "honest")
            lola "Wow, okay, straight for the throat."
            lola "...Because if they like the posts, maybe they'd like me. And if they don't like the posts, they {i}definitely{/i} wouldn't."

    lola "Please don't tell anyone. Especially not Xenia. She'd have it posted before I finished blinking."
    $ set_flag("lola.opened_up")
    $ reveal("lola", "likes")
    "(You learned what Lola likes. Check your phone.)"
    lola "Hey, um. Since you already know the worst thing about me... could you help me with something? Off-camera?"

    hide lola
    with dissolve
    return
