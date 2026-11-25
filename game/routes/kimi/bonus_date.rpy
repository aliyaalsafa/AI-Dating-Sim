## Kimi's night date (CLAUDE.md §6.1): the student activities hall after
## everyone's gone, her favorite place. The engine runs her date quiz afterward.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label kimi_bonus_date:
    show kimi neutral at center
    with dissolve

    # PLACEHOLDER
    "The activities hall at night. The chairs are stacked, the banners are drooping, and for the first time all semester it's empty except for Kimi."
    kimi "Hi! Welcome to the only meeting I've ever scheduled with just one member."
    kimi "No clipboards tonight. I left them all in the closet. It felt like leaving twelve children with a babysitter."
    "She's strung a line of little fairy lights along the bulletin board, right over the leaderboard, so you can't read it anymore."
    kimi "This is my favorite place in the world when it's loud. I wanted to see if it was still my favorite when it was quiet. With you."

    menu:
        "\"Tell me about the first club you ever started.\"" (prompt="curious"):
            $ choose("kimi", 4, "curious")
            kimi "Stargazing Club. I was the only member for a month. I made posters. Nobody came."
            kimi "Then one person came. Then two hundred. But I still think about that first month. It was the only time it was just mine."
        "Help her take down the leaderboard, one pin at a time." (prompt="practical"):
            $ choose("kimi", 4, "practical")
            kimi "We can't! We're not allowed! We're—"
            "She takes out the last pin herself and folds the leaderboard into a paper firefly."
            kimi "...Okay. That felt amazing."
        "\"Plan our next date. Every detail.\"" (prompt="structured"):
            $ choose("kimi", 3, "structured")
            kimi "Our {i}next{/i} date? Oh. Okay. I need a clipboard. I promised no clipboards. I'll use a napkin."
            "The napkin plan has sixteen bullet points. Every one of them is something {i}you{/i} told her you liked."

    kimi "Can I test something? I want to see if you really know me. Not the free version. Me."

    hide kimi
    with dissolve
    return
