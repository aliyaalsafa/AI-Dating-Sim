## Day 3, morning (forced group scene): the first leaderboard. Grace and Shen tie.
## Introduces Shen to anyone who hasn't met her, and sets up the central rivalry.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label day03_leaderboard:
    scene bg quad
    with fade

    # PLACEHOLDER: leaderboard group scene
    "A crowd has gathered at the noticeboard on the quad. The first practice-exam leaderboard is up."

    show grace neutral at left
    show shen neutral at right
    with dissolve

    "{b}1. GRACE PENELOPE TURING — 100{/b}"
    "{b}1. SHEN XUN — 100{/b}"
    "A tie. The quad goes very, very quiet."

    if not has_flag("met_shen"):
        "The girl beside Grace has a whale keychain and a laptop held together with stickers. Someone whispers her name: Shen."
        $ set_flag("met_shen")

    grace "Wow! Great — great job, Shen! Truly. That's — wow. Great."
    shen "You said 'great' four times."
    grace "Three. — Four. You're right. Four."

    show gemma neutral at center
    with dissolve

    gemma "Actually, Shen's solutions had fewer steps. If we graded on efficiency, she'd—"
    grace "We don't grade on efficiency."
    gemma "We should. I'll start a petition. I'll probably finish it."

    hide gemma
    with dissolve

    "Somewhere behind you, someone is typing very fast."
    # PLACEHOLDER: @x_unfiltered post
    $ post("TIE AT THE TOP. Grace said 'great' FOUR times. Scholarship kid did it on a laptop held together with stickers. I'm sat.")

    menu:
        "Congratulate Grace on keeping her spot." (prompt="warm"):
            $ choose("grace", 3, "warm")
            grace "Thank you! I mean — it's a tie, so — thank you."
            shen "Hm."
        "Congratulate Shen on her first leaderboard." (prompt="honest"):
            $ choose("shen", 3, "honest")
            shen "...Thank you. Everyone else is asking how. Nobody's said well done."
            grace "..."
        "Tell them both it's impressive." (prompt="practical"):
            $ choose("grace", 2, "practical")
            $ choose("shen", 2, "practical")
            shen "Diplomatic."
            grace "Yes! Very — yes. Both. Diplomatic. Great."

    hide shen
    with dissolve
    show claudia neutral at right
    with dissolve

    claudia "She'll be fine. She always is. That's rather the problem."
    "Claudia says it so softly you aren't sure you were meant to hear."

    "(From here on, the semester is yours. Spend your time wisely.)"
    return
