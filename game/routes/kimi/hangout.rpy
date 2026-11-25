## Kimi: repeatable hangout at the student activities hall (once per day).
## Rotates through four conversation topics. Her route rewards valuing her for
## herself (not as the free alternative); it punishes forgetting what she told you.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label kimi_hangout:
    show kimi neutral at center
    with dissolve

    $ topic = sim_state.count(gs, "kimi.hangouts") % 4
    $ gs = sim_state.incr(gs, "kimi.hangouts")

    if topic == 0:
        call kimi_topic_clubs
    elif topic == 1:
        call kimi_topic_notes
    elif topic == 2:
        call kimi_topic_ranking
    else:
        call kimi_topic_callback

    hide kimi
    with dissolve
    return


label kimi_topic_clubs:
    # PLACEHOLDER
    "Kimi is holding four clipboards. Two more are tucked under her arm. A seventh is, somehow, behind her ear."
    kimi "[player_name]! Perfect timing! Chess Club, Pottery Club and the Competitive Napping Society all need a fourth person. You can be the fourth person for all three!"
    kimi "They meet at the same time. That's fine. I'm in all of them too. You just sort of... spread out."

    menu:
        "\"Which club do you actually like best?\"" (prompt="curious"):
            $ choose("kimi", 4, "curious")
            kimi "Best? Nobody asks that. They ask which one is free."
            kimi "...Stargazing. It's the only one where nobody needs me to do anything. We just look up."
        "\"Make me a schedule and I'll try two of them.\"" (prompt="structured"):
            $ choose("kimi", 3, "structured")
            kimi "A schedule! Yes! I have a template. I have twelve templates. Pick a color! Any color! It's lavender. They're all lavender."
        "\"No.\"" (prompt="concise"):
            $ choose("kimi", 1, "concise")
            kimi "Oh! Okay! That's okay. That's totally okay."
            "She writes your name on all three sign-up sheets anyway, very small, in pencil. Just in case."
    return


label kimi_topic_notes:
    # PLACEHOLDER
    kimi "Want my notes? Everyone gets my notes! Linear algebra, organic chem, the history of interpretive dance. All free. Take as many as you want."
    kimi "Well. Almost everyone. Claudia had to sign a contract. Four pages. She had questions about clause seven."
    kimi "Clause seven says if your family owns more than one boat, you have to ask nicely. In writing."

    menu:
        "\"Why the contract for Claudia?\"" (prompt="curious"):
            $ choose("kimi", 3, "curious")
            kimi "Because the rich kids take everything and say it was theirs all along. Claudia's actually lovely about it. She sent a thank-you note. On letterhead."
            kimi "I framed it. Don't tell her."
        "\"Can I help you organize them so they're easier to share?\"" (prompt="practical"):
            $ choose("kimi", 4, "practical")
            kimi "You'd do that? People usually just take them and leave. You want to help {i}give{/i} them?"
            kimi "Okay. Okay! Folders. We need folders. I have forty folders."
        "\"Free notes? What's the catch?\"" (prompt="pry"):
            $ choose("kimi", 1, "pry")
            kimi "No catch! Well, the catch is people call me the free version of whoever they actually wanted to ask."
            kimi "That's not a catch for {i}you{/i}. That's just a catch."
    return


label kimi_topic_ranking:
    # PLACEHOLDER
    "A printout is taped to the bulletin board: the midterm leaderboard. Grace first. Claudia second. Kimi's name is third, in slightly smaller font."
    kimi "Ha. Third again. I scored higher than last year, so they made the font smaller. That's how you know you're improving."
    kimi "It's fine! Third is great. Third is a podium spot. They give you a bronze-colored ribbon. It's mostly brown."

    menu:
        "\"The leaderboard doesn't know what you do here every day.\"" (prompt="practical"):
            $ choose("kimi", 3, "practical")
            kimi "Twelve clubs, two hundred members, three bake sales a week. You're right. The leaderboard doesn't have a column for bake sales."
            kimi "It should. I'd win."
        "\"Rank yourself. Not against them. What are you proud of?\"" (prompt="structured"):
            $ choose("kimi", 5, "structured")
            kimi "Against... me? Okay. Number one: I got the Napping Society its own room. Number two..."
            "She goes all the way to forty-one. She looks happier at every number."
        "\"Third's not bad. You're like the budget pick everyone can afford.\"":
            $ choose("kimi", -3)
            kimi "...Yeah. Budget pick. Heard that one."
            "She laughs. It doesn't quite reach her eyes."
    return


label kimi_topic_callback:
    # PLACEHOLDER
    kimi "Okay, quiz! Last time we talked, I told you something really important. Do you remember what it was?"
    "She's grinning, but she's holding her clipboard very tightly."

    menu:
        "\"Stargazing. It's the only club where nobody needs anything from you.\"" (prompt="curious"):
            $ choose("kimi", 5, "curious")
            kimi "You remembered! You actually remembered!"
            kimi "Two hundred people in my group chats and nobody remembers anything I say. They just remember I'll say yes."
        "\"You framed Claudia's thank-you note.\"" (prompt="warm"):
            $ choose("kimi", 3, "warm")
            kimi "You remembered that? Oh no. That's so embarrassing. That's so nice. Both!"
        "\"Uh... was it about the bake sale?\"":
            $ hit_dealbreaker("kimi")
            kimi "Ha. No. That's okay! It wasn't important."
            kimi "It's never important. That's what I'm for, right? Background noise with free snacks."
            "She turns back to her clipboards. All of them at once."
    return
