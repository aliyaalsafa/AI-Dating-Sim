## Shen's confession (CLAUDE.md §6.1), affection 90+, evening, after the bonus date.
## Library, 3rd floor. She reasons her way there out loud, step by step.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label shen_confession:
    show shen placeholder at center
    with dissolve

    # PLACEHOLDER
    "The third floor is empty. Shen is at the table by the outlet, and for once, her laptop is closed and the whale keychain is sitting on top of it."
    shen "I need to work something out. Out loud. Don't interrupt. It's going to take a while."
    shen "Step one. I spend more time with you than with anyone. I track my time. The data is clear."
    shen "Step two. That time is not efficient. We talk about nothing. I don't mind. That's new."
    shen "Step three. When people talk about me, they say Grace's name. When you talk about me, you just say mine."
    shen "Wait. Let me reconsider. Step three should have been step one. It's the most important one."
    shen "Step four. I've been thinking about this for eleven days. That's too long for any problem I've ever had. Which means it isn't a problem."
    shen "Conclusion. I like you. Precisely you. Not as a comparison. Not as a variable."
    "She slides the whale keychain across the table to you."

    menu:
        "\"I like you too. Precisely.\"" (prompt="concise"):
            $ choose("shen", 4, "concise")
            shen "Good. Verified. ...I'm smiling. Don't comment on it."
        "\"That was the longest you've ever talked. Are you okay?\"" (prompt="irreverent"):
            $ choose("shen", 1, "irreverent")
            shen "No. My heart rate is very high. It's unscientific."
            shen "Answer the question. The real one."
            "You tell her yes."
            shen "...Okay. Good. That was a lot of steps for a yes. Worth it."

    $ set_flag("shen.confessed")
    shen "Keep the whale. I'll get another one. They're cheap."
    shen "Wait. Let me reconsider. That one isn't cheap. That one's yours."

    hide shen
    with dissolve
    return
