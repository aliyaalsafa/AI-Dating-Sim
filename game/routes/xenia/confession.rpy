## Xenia's confession (CLAUDE.md §6.1), affection 90+, after the bonus date.
## On the roof at night. She drops the act, and the @x_unfiltered secret comes out.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label xenia_confession:
    show xenia neutral at center
    with dissolve

    # PLACEHOLDER
    "Xenia isn't at the telescope tonight. She's sitting on the edge of the roof with her phone in her hands, and she isn't typing."
    xenia "Okay. Two things. Don't talk until I'm done, or I'll lose my nerve, and I've never had nerve to lose before, so this is new territory."
    xenia "Thing one. I run [XENIA_HANDLE]. Yeah. The whole thing. Every 'BREAKING,' every Grace roast, every post about you looking lost on day one."
    xenia "I figured you'd guessed. Claudia definitely has. She keeps looking at me like she's writing me a very polite letter about it."
    xenia "It's easier to say things when nobody knows it's me. Mean things are easy. Mean things are armor."
    xenia "Thing two. That's the hard one."
    "She puts the phone face down on the roof."
    xenia "I like you. Not ironically. Not as a bit. I've been trying to come up with a way to say it that sounds cool, and there isn't one. So. There it is. Unfiltered."
    xenia "You never flinched. Not once. You roasted me back, and then when I stopped joking, you stopped too. Nobody does both."

    menu:
        "\"I like you too. And I've known about the account for weeks.\"" (prompt="honest"):
            $ choose("xenia", 4, "honest")
            xenia "You— for {i}weeks{/i}? And you didn't say anything?"
            xenia "Oh, you're terrible. You're the worst. I'm so into it."
            "She laughs, really laughs, and then she leans against your shoulder like it's the most natural thing in the world."
        "\"So the 'looking lost on day one' post. I'd like a formal apology.\"" (prompt="irreverent"):
            $ choose("xenia", 4, "irreverent")
            xenia "I confess my undying feelings and you want an {i}apology{/i}? For an accurate post?"
            xenia "...Fine. I'm sorry you looked lost. You were adorable. That's my apology. It's the only one I've got."
            xenia "Is that a yes? Tell me that's a yes. I'm not built for suspense."
            "You tell her it's a yes."

    $ set_flag("xenia.confessed")
    xenia "Okay. Wow. I need to post about this. I'm not going to post about this."
    "She picks up her phone, types something, and doesn't hit send. She shows you anyway."
    "{i}Draft: Found a new star. Not telling anyone where.{/i}"

    hide xenia
    with dissolve
    return
