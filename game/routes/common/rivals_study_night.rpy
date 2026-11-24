## Grace + Shen group scene (sets up the secret Rivals ending, CLAUDE.md §7).
## Plays at Shen's library table one evening once both trust you (60+, both opened up).
## Getting them to study together sets RIVALS_EVENT_FLAG; both still need 75+ at the gala.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label rivals_study_night:
    show shen placeholder at right
    with dissolve

    # PLACEHOLDER
    "Shen is at her usual table by the outlet. You've barely sat down when the door opens."

    show grace placeholder at left
    with dissolve

    grace "Oh! Hi! I didn't— I'm just here for a book. A specific book. On a specific shelf."
    shen "The library closes its stacks at nine. It's nine fifteen."
    grace "...Then I'm here for the outlet."
    shen "There's one outlet."
    "They both look at the outlet. Then at each other. Then, for some reason, at you."

    menu:
        "\"There's room for two laptops. Study together.\"" (prompt="practical"):
            $ choose("grace", 3, "practical")
            $ choose("shen", 3, "practical")
            $ set_flag("rivals_joint_event_done")
            shen "Wait. Let me reconsider. ...Efficient. Fine."
            grace "Great! Great. I'll take— I'll take the left side. If that's okay. Is that okay?"
            "It takes them eleven minutes to stop being polite and start arguing about integrals. It's the happiest you've seen either of them."
            shen "Your method has nine steps."
            grace "Your method skips four of them!"
            shen "Because they're unnecessary."
            grace "They're {i}thorough{/i}."
            "At midnight, they're still at it. Neither of them notices you leave."
        "\"Grace, you take it. Shen can share mine.\"" (prompt="warm"):
            $ choose("grace", 2, "warm")
            $ choose("shen", -1, "warm")
            shen "I don't need charity. I need the outlet."
            grace "No, it's fine, I'll go. I'll— sorry. Sorry."
            hide grace
            with dissolve
            "Grace leaves. Shen watches the door for a long moment after it closes."
        "\"Honestly? You two are more alike than you think.\"" (prompt="honest"):
            $ choose("grace", 2, "honest")
            $ hit_dealbreaker("shen")
            shen "Alike. As in, I'm the cheaper copy."
            grace "That's not what they meant— is it what you meant?"
            hide grace
            with dissolve
            "Shen packs up her laptop without another word."

    hide grace
    hide shen
    with dissolve
    return


label ending_rivals(ending):
    scene bg gala
    with fade
    show grace placeholder at left
    show shen placeholder at right
    with dissolve

    # PLACEHOLDER: Rivals secret ending
    "You find them both by the entrance. They're arguing. They're arguing about you."
    grace "We were each going to say yes to you, and then we realized we'd both be thinking about the other one all night."
    shen "So we did the math. Wait. Let me reconsider. We did the math twice."
    grace "And the optimal solution is: we go together. And you come with us. Obviously."
    shen "Obviously. You introduced us. Properly. That's not nothing."
    "Grace takes one of your arms. Shen takes the other."
    grace "I made a plan for tonight."
    shen "I made a better one."
    grace "We'll compromise."
    shen "We will not compromise."
    "You spend the gala being dragged between two dance floors by two people who refuse to admit they're having the time of their lives."
    call ending_card(ending)
    return
