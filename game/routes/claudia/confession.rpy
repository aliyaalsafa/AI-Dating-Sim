## Claudia's confession (CLAUDE.md §6.1), affection 90+, after the bonus date,
## one evening in her suite's private library.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label claudia_confession:
    show claudia neutral at center
    with dissolve

    # PLACEHOLDER
    "Claudia is standing by the window seat, holding her leather notebook against her chest. One page has been carefully torn out and folded into an envelope. It has your name on it."
    claudia "I've written you eleven letters. I didn't send any of them. They were all very beautiful and very careful, and they all said the same thing at enormous length."
    claudia "So I'm sending this one. It's the shortest. I'd like you to read it in front of me, which is the single most frightening sentence I've ever said."
    "She hands it to you. Inside, in her beautiful handwriting, there is one line."
    "{i}I like you. No footnotes. Claudia.{/i}"
    claudia "I want to say it out loud too, without hedging, because I think you deserve to hear me have an opinion about something that isn't ducks."
    claudia "I like you. I think you're honest and patient, and you ask what I think, and when I tell you, you listen as if it matters. I think I'm a little bit in love with you. That's not gossip. That's mine."

    menu:
        "\"I like you too. No footnotes.\"" (prompt="honest"):
            $ choose("claudia", 3, "honest")
            claudia "Oh."
            claudia "Oh, that's... I had seven paragraphs prepared for every possible answer, and I don't need any of them. How marvelous."
        "Write your answer on the back of the letter and hand it back." (prompt="warm"):
            $ choose("claudia", 3, "warm")
            "You write one word on the back and hand it back to her. She reads it, and presses the paper flat against her heart."
            claudia "I'm going to keep this forever. In a shoebox. Not metaphorically, this time."

    $ set_flag("claudia.confessed")
    claudia "I'm sorry I— no. I'm not sorry. For once, I'm not sorry at all."

    hide claudia
    with dissolve
    return
