## Grace's confession (CLAUDE.md §6.1), affection 90+, after the bonus date.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label grace_confession:
    show grace neutral at center
    with dissolve

    # PLACEHOLDER
    "Grace is waiting by the window. She's holding her planner, and she looks like she's about to give a pitch she hasn't rehearsed. That would be a first."
    grace "Okay. I made a deck. Twelve slides. Then I threw it out, because I think the deck was a way of not saying it."
    grace "My whole life, I've said yes to everything and moved fast so I'd never have to stop and ask what I wanted. People like you when you agree with them. People like you when you ship."
    grace "And then you showed up and disagreed with me, kindly, constantly, and made me slow down, and I realized I'd rather argue with you than agree with anyone else."
    grace "I like you. That's not a guess. I validated it. Several times. Color-coded. Statistically significant."
    "She tears a page out of her planner, the one that said {i}Thursday, 9 p.m.{/i}, and gives it to you."

    menu:
        "\"I like you too. No deck needed.\"" (prompt="honest"):
            $ choose("grace", 3, "honest")
            grace "Okay. Okay! Great — no. Not great. Better than great. Ten-x great. No, that's not it either. I don't have a word for it. I'll find one."
        "\"Did you color-code your feelings?\"" (prompt="irreverent"):
            $ choose("grace", 2, "irreverent")
            grace "Sea green. Obviously. There's a roadmap. Don't laugh. ...Okay, you can laugh a little."
            grace "Is that a yes? I need it to be a yes. I'm not used to launching without knowing the outcome."
            "You tell her it's a yes."

    $ set_flag("grace.confessed")
    grace "Want me to—"
    grace "No. What do {i}you{/i} want?"
    "For once, she doesn't move fast. She waits for the answer."

    hide grace
    with dissolve
    return
