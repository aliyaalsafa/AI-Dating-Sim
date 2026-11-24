## Shen's bonus date (CLAUDE.md §6.4), affection 75+, evening: starts at the
## 24-hour library, then she takes you out for cheap street food.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label shen_bonus_date:
    show shen placeholder at center
    with dissolve

    # PLACEHOLDER
    "Shen closes her laptop at exactly 8:00 p.m. You've never seen her close it on purpose."
    shen "I budgeted an evening. For you. It's in the spreadsheet. The column is called 'not studying.'"
    shen "Come on. Night market. I have twelve dollars and a plan."
    "She leads you three blocks off campus, to a row of food stalls glowing under string lights. She knows every vendor by name. Every vendor knows her order."
    shen "Skewers from the second stall. Dumplings from the fourth. The first stall is overpriced. The third is a trap."
    shen "Total cost for two: eleven dollars and fifty cents. I calculated it on the walk. Twice."

    menu:
        "\"You planned this down to the cent. I love it.\"" (prompt="honest"):
            $ choose("shen", 3, "honest")
            shen "Down to the half cent. I rounded for you."
            shen "...You love it. Okay. I'm going to think about that later. Carefully."
        "Let her order for you. Don't say a word." (prompt="concise"):
            $ choose("shen", 5, "concise")
            "You just nod. Shen orders for both of you in four efficient words."
            shen "You didn't ask a single unnecessary question. Do you know how rare that is?"
            shen "This is the best evening I've had since I got here. That's not an estimate."
        "\"So is this a date, or a field study?\"" (prompt="irreverent"):
            $ choose("shen", 1, "irreverent")
            shen "Let me think. Two people. Food. String lights. I paid."
            shen "Wait. Let me reconsider. Conclusion: shut up and eat your dumpling."

    "You eat on the curb, sharing a paper plate. She has fifty cents left over and buys a single sesame candy, which she splits exactly in half."

    $ set_flag("shen.bonus_date_done")
    shen "Same budget next week. I'll find a cheaper dumpling. Then we can afford two candies."

    hide shen
    with dissolve
    return
