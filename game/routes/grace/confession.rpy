## Grace's confession (CLAUDE.md §6.1), affection 90+, after the bonus date.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label grace_confession:
    show grace placeholder at center
    with dissolve

    # PLACEHOLDER
    "Grace is waiting by the window. She's holding her planner, and she looks like she's about to give a speech she hasn't rehearsed. That would be a first."
    grace "Okay. I made a list of things to say, and then I threw it out, because I think the list was a way of not saying them."
    grace "My whole life, I've agreed with everyone. It's easy. People like you when you agree with them."
    grace "And then you showed up and disagreed with me, kindly, constantly, and I realized I'd rather argue with you than agree with anyone else."
    grace "I like you. That's not a guess. I checked. Several times. Color-coded."
    "She tears a page out of her planner, the one that said {i}Thursday, 9 p.m.{/i}, and gives it to you."

    menu:
        "\"I like you too. No list needed.\"" (prompt="honest"):
            $ choose("grace", 3, "honest")
            grace "Okay. Okay! Great — no. Not great. Better than great. I don't have a word for it. I'll find one."
        "\"Did you color-code your feelings?\"" (prompt="irreverent"):
            $ choose("grace", 2, "irreverent")
            grace "Sea green. Obviously. Don't laugh. ...Okay, you can laugh a little."
            grace "Is that a yes? I need it to be a yes. I'm not used to not knowing."
            "You tell her it's a yes."

    $ set_flag("grace.confessed")
    grace "Want me to—"
    grace "No. What do {i}you{/i} want?"
    "For once, she waits for the answer."

    hide grace
    with dissolve
    return
