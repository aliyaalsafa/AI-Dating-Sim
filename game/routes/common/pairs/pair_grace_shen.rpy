## Pair scene: Grace + Shen at the 24-hour library, evening (CLAUDE.md §4, §6.5).
## The central rivalry (the old "study night" scene, reworked as a pair scene).
## Ends by calling pair_done, which shows this pair's two hints from data/mystery.rpy.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label pair_grace_shen:
    show shen neutral at right
    with dissolve

    # PLACEHOLDER
    "The third floor of the library is silent except for the hum of the vending machine. Shen is at her usual table by the only outlet."
    "You've barely sat down at the next table when the door opens."

    show grace neutral at left
    with dissolve

    grace "Oh! Hi! I didn't— I'm just here for a book. A specific book. On a specific shelf."
    shen "The stacks close at nine. It's nine fifteen."
    grace "...Then I'm here for the outlet."
    shen "There's one outlet."
    "They both look at the outlet. Then at each other. Then, for some reason, at you."
    grace "We could share! I have an adapter. Well, I have four adapters. I brought one for every possible situation."
    shen "Wait. Let me reconsider. ...Fine. One plug each. Don't talk."
    "It takes them eleven minutes to stop being polite and start arguing about integrals."
    shen "Your method has nine steps."
    grace "Your method skips four of them!"
    shen "Because they're unnecessary."
    grace "They're {i}thorough{/i}. Thorough is a value. I put it on the debate-club poster."

    menu:
        "\"Show me both methods. I'll judge which is better.\"" (prompt="structured"):
            $ choose("grace", 2, "structured")
            $ choose("shen", 1, "structured")
            grace "Great idea! Step one— okay, there are nine, so get comfortable."
            shen "Step one. Done. Step two. Done."
            "Shen finishes first. Grace's answer is the same. Both of them pretend not to be pleased about it."
        "\"Shen's is shorter. Shorter wins.\"" (prompt="concise"):
            $ choose("shen", 3, "concise")
            $ choose("grace", -1, "concise")
            shen "Correct."
            grace "Totally fair! Really great point. I agree. I— wait, do I agree?"
        "\"You two should study together on purpose sometime.\"" (prompt="practical"):
            $ choose("grace", 2, "practical")
            $ choose("shen", 2, "practical")
            shen "That would be efficient. I hate that it would be efficient."
            grace "I'd bring snacks! Four kinds. In case."

    "Grace's phone lights up. She angles it away, but not before Shen sees a spreadsheet, a column of percentages, and a name at the top."
    "Shen doesn't look up from her notes. Her voice drops. They seem to have forgotten you're one table over."
    shen "You're doing it again."
    grace "Doing what?"
    shen "The thing you do after the new student leaves a room."

    call pair_done("grace_shen")

    hide grace
    hide shen
    with dissolve
    return
