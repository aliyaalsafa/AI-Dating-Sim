## Day 2: optional early meeting with Shen (library or robotics lab).
## If you miss her, you meet her at the leaderboard on day 3.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label day02_meet_shen:
    show shen placeholder at center
    with dissolve

    # PLACEHOLDER: Shen's introduction
    "A girl in a thrifted sweater vest is typing on a laptop held together entirely by stickers. A whale keychain hangs from her backpack."
    shen "You're blocking the outlet."
    shen "Wait. Let me reconsider. You're not blocking it. You're near it. Sorry. I'm Shen."
    shen "You're the other transfer. I came in mid-year too. People will tell you things about me. Most of them are about Grace."
    $ set_flag("met_shen")

    menu:
        "\"I'd rather hear about you.\"" (prompt="honest"):
            $ choose("shen", 3, "honest")
            shen "...Efficient question. I like algorithms, cheap noodles and winning. Usually in that order."
        "\"Need anything? I'm heading to the store.\"" (prompt="practical"):
            $ choose("shen", 3, "practical")
            shen "No. But that was a useful offer. Noted."
        "\"So you're the one who's basically Grace 2.0?\"":
            $ hit_dealbreaker("shen")
            shen "Yes. That's me. The sequel. Excuse me, I have work."

    if not gs.chars["shen"].romance_locked:
        shen "Here. Calculus notes. Everyone gets a copy. They're free."
        "She hands you a stack of notes so neat they look typeset."

    hide shen
    with dissolve
    return
