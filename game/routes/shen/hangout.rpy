## Shen: repeatable hangout at the 24-hour library or the robotics lab (once per day).
## Rotates through four conversation topics. Her route rewards concise, honest,
## practical answers and seeing her on her own terms; it punishes comparing her to Grace.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label shen_hangout:
    show shen neutral at center
    with dissolve

    if gs.inventory:
        menu:
            shen "[player_name]. Sit. You have something in your bag. Wait. Let me reconsider. That's none of my business. Is it for me?"
            "Just talk.":
                pass
            "Give her a gift.":
                call give_gift_flow("shen")
                hide shen
                with dissolve
                return

    $ topic = sim_state.count(gs, "shen.hangouts") % 4
    $ gs = sim_state.incr(gs, "shen.hangouts")

    if topic == 0:
        call shen_topic_notes
    elif topic == 1:
        call shen_topic_jobs
    elif topic == 2:
        call shen_topic_laptop
    else:
        call shen_topic_grace

    hide shen
    with dissolve
    return


label shen_topic_notes:
    # PLACEHOLDER
    "Shen is photocopying a stack of notes. It is a very tall stack."
    shen "Linear algebra. Forty copies. I leave them on the table downstairs. They're gone by noon."
    shen "People ask why I don't charge. Step one: it costs me nothing to share. Step two: more people understand the material. Step three: the curve goes up, so I have to work harder. Good."

    menu:
        "\"Smart. Everyone wins.\"" (prompt="concise"):
            $ choose("shen", 4, "concise")
            shen "Correct. Three words. You're learning."
        "\"Doesn't it bother you that nobody credits you?\"" (prompt="honest"):
            $ choose("shen", 3, "honest")
            shen "Yes."
            shen "Wait. Let me reconsider. Not the sharing. The part where people assume they came from somewhere else. That part bothers me."
        "\"Could you make a shorter version? With fewer steps?\"" (prompt="practical"):
            $ choose("shen", 3, "practical")
            shen "Fewer steps. Hm. Page four is redundant. And page seven. You just saved me two pages of toner. Thank you."
        "\"You should sell them and get a better laptop.\"" (prompt="irreverent"):
            $ choose("shen", 1, "irreverent")
            shen "I could. Then only people with money would have them. That's the system I'm trying to beat."
    return


label shen_topic_jobs:
    # PLACEHOLDER
    shen "I have eleven minutes before my shift at the dining hall. Then the library desk until ten. Ask me something worth eleven minutes."

    menu:
        "\"What would you do with one free evening?\"" (prompt="curious"):
            $ choose("shen", 3, "curious")
            shen "Free evening. Let me think. Sleep: no, I'd feel guilty. Study: that's not free. Street food market: yes."
            shen "Answer: the night market. Skewers. Six of them. Precisely six."
        "\"Want me to cover the library desk sometime?\"" (prompt="practical"):
            $ choose("shen", 4, "practical")
            shen "You're not on payroll."
            shen "Wait. Let me reconsider. You could keep me company on it. The desk has two chairs. That's allowed."
        "\"How do you do all this and still tie for first?\"" (prompt="honest"):
            $ choose("shen", 3, "honest")
            shen "Short version: I don't waste anything. Not time, not money, not words."
            shen "Long version: I'm tired. Don't tell anyone."
        "Tell her about your weekend. In detail. All of it." (prompt="warm"):
            $ choose("shen", 0, "warm")
            "You get to Saturday afternoon before Shen glances at the clock."
            shen "That was nine minutes. I have two left. ...Was there a point?"
    return


label shen_topic_laptop:
    # PLACEHOLDER
    "Shen's laptop makes a sound like a small airplane taking off. She pats it."
    shen "Six years old. Fourth owner. The stickers are structural. The whale is holding the hinge on."

    menu:
        "\"It's not broken. It's optimized.\"" (prompt="irreverent"):
            $ choose("shen", 2, "irreverent")
            shen "Hm. That's almost funny. Don't push it."
        "\"Which sticker is load-bearing?\"" (prompt="curious"):
            $ choose("shen", 3, "curious")
            shen "Good question. The whale. Then the robotics club logo. Gemma gave me that one. Then a sticker that says 'Free Samples.' I don't remember where that came from."
        "\"What does it run, and how fast?\"" (prompt="structured"):
            $ choose("shen", 3, "structured")
            shen "Four gigs of memory. A fan that sounds like that. It trains a small model overnight if I don't open a browser."
            shen "The point isn't the machine. The point is what you do with it."
        "\"Does it work? Then it's fine.\"" (prompt="concise"):
            $ choose("shen", 5, "concise")
            shen "...Yes. Exactly that."
            shen "Everyone else asks why I don't buy a new one. You're the first to ask the right question."
    return


label shen_topic_grace:
    # PLACEHOLDER
    "Across the room, Grace walks past with three tote bags of color-coded binders. Shen watches her go."
    shen "She has a tutor. A private one. And a printer in her room. And a mini fridge."
    shen "Not that I'm keeping a list. Wait. Let me reconsider. I am keeping a list."

    menu:
        "\"You did the same work with way less. That's yours.\"" (prompt="honest"):
            $ choose("shen", 5, "honest")
            shen "...Mine. Yes."
            shen "People usually say 'the same as Grace.' You said mine. Noted. Strongly noted."
        "\"What would you do with a printer?\"" (prompt="irreverent"):
            $ choose("shen", 1, "irreverent")
            shen "Print more notes. Obviously. Was that a joke? Jokes cost time."
        "\"Do you actually dislike her?\"" (prompt="pry"):
            $ choose("shen", 2, "pry")
            shen "Dislike. Let me think. She's fast. She's careful. She says 'great' too much."
            shen "Answer: no comment. Next question."
        "\"Honestly, you're basically the scrappy version of Grace.\"":
            $ hit_dealbreaker("shen")
            shen "The scrappy version."
            shen "I'm not a version of anyone. I'm going to go now. That's an efficient use of my time."
    return
