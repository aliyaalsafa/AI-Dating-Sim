## Grace: repeatable hangout at the student council office (once per day).
## Rotates through four conversation topics. Her route rewards kind disagreement
## and asking what she wants; it punishes treating her as a homework service.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label grace_hangout:
    show grace neutral at center
    with dissolve

    if gs.inventory:
        menu:
            grace "Hi, [player_name]! Want me to: one, catch you up, two, quiz you, or three, both?"
            "Just talk.":
                pass
            "Give her a gift.":
                call give_gift_flow("grace")
                hide grace
                with dissolve
                return

    $ topic = sim_state.count(gs, "grace.hangouts") % 4
    $ gs = sim_state.incr(gs, "grace.hangouts")

    if topic == 0:
        call grace_topic_midterms
    elif topic == 1:
        call grace_topic_clubs
    elif topic == 2:
        call grace_topic_agreeing
    else:
        call grace_topic_shen

    hide grace
    with dissolve
    return


label grace_topic_midterms:
    # PLACEHOLDER
    grace "Okay! Midterms are in three weeks, so I made a study plan. It's color-coded. It has a legend. The legend has a legend."

    menu:
        "\"This is overkill. You're allowed to sleep.\"" (prompt="honest"):
            $ choose("grace", 4, "honest")
            grace "I— huh. Is it? Nobody's ever said that. Everyone just asks for a copy."
            grace "...I could sleep. I could try sleeping."
        "\"Walk me through how it works.\"" (prompt="structured"):
            $ choose("grace", 2, "structured")
            grace "Great question! So: blue is reading, green is review, and sea green — which is different from green — is reviewing the review."
        "\"Can you add a color for snacks?\"" (prompt="irreverent"):
            $ choose("grace", 2, "irreverent")
            grace "A snack color. Is that a joke? I can't tell if that's a joke. I'll add it, just in case."
        "\"Could you just do my problem set? You're faster.\"":
            $ hit_dealbreaker("grace")
            grace "Of course! I'd be happy to—"
            grace "...No. Actually, no. Everyone asks me that. I thought you were different."
    return


label grace_topic_clubs:
    # PLACEHOLDER
    grace "So I'm in nine clubs. Here they are, ranked by meeting frequency: one, Debate. Two, Model UN. Three, Ethics Bowl. Four—"

    menu:
        "\"Which one do you actually like?\"" (prompt="curious"):
            $ choose("grace", 6, "curious")
            grace "Like? I— they're all very valuable. They all—"
            grace "Debate. I like Debate. Because you're allowed to argue a side even if... even if people don't like it."
            grace "Wow. I didn't know that until just now."
        "\"You're amazing for doing all that.\"" (prompt="warm"):
            $ choose("grace", 2, "warm")
            grace "Thank you! That's what everyone says. It's nice. It's... nice."
        "\"Quit three of them. Today.\"" (prompt="concise"):
            $ choose("grace", 2, "concise")
            grace "Ha! Quit! Ha. ...Which three, hypothetically?"
    return


label grace_topic_agreeing:
    # PLACEHOLDER
    "You decide to test something. You tell Grace, with total confidence, that the library is closed on Thursdays because of the moon."
    grace "Oh, absolutely — great point. The lunar schedule. Very important for— for books."

    menu:
        "Gently point out that none of that was true." (prompt="honest"):
            $ choose("grace", 4, "honest")
            grace "It— wasn't? Oh no. I'm so sorry. I do that. I agree with whoever spoke last."
            grace "Could you... do that again sometime? Tell me when I'm wrong? Nobody does."
        "Keep going. Tell her the moon also runs the cafeteria." (prompt="irreverent"):
            $ choose("grace", 1, "irreverent")
            grace "That would explain the soup! ...Wait. Are you messing with me?"
        "\"Do you ever disagree with anyone?\"" (prompt="pry"):
            $ choose("grace", 3, "pry")
            grace "Of course I do! I disagree all the time. Constantly. Don't you think?"
            grace "...I just agreed with you about disagreeing, didn't I."
    return


label grace_topic_shen:
    # PLACEHOLDER
    grace "Did you see Shen's lab report? It's three pages. Mine was eleven. Hers was better. Which is great! For her. Great."

    menu:
        "\"What is it about her that scares you?\"" (prompt="honest"):
            $ choose("grace", 3, "honest")
            grace "Scares— I'm not— "
            grace "She does what I do with less. If she can do that, what am I for?"
            grace "...Please don't tell anyone I said that. Claudia knows. That's already one too many."
        "\"You don't have to beat her. Just be you.\"" (prompt="warm"):
            $ choose("grace", 3, "warm")
            grace "Be me. Sure. Totally. I'll just... figure out what that means by Friday."
        "\"Honestly, her report {i}was{/i} tighter.\"" (prompt="irreverent"):
            $ choose("grace", 0, "irreverent")
            grace "Right. No, you're right. Of course. Everyone's right. Great."
    return
