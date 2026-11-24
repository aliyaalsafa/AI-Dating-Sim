## Xenia: repeatable hangout in the cafeteria (afternoon) or on the observatory
## roof (evening), once per day. Rotates through four conversation topics. Her
## route rewards roasting her back and never flinching; it punishes lecturing
## her or asking her to tone it down. Topic 3 contains her "unhinged mode".
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label xenia_hangout:
    show xenia neutral at center
    with dissolve

    if gs.inventory:
        menu:
            xenia "Oh look, it's you. Are you here to talk, or did you finally bring me tribute?"
            "Just talk.":
                pass
            "Give her a gift.":
                call give_gift_flow("xenia")
                hide xenia
                with dissolve
                return

    $ topic = sim_state.count(gs, "xenia.hangouts") % 4
    $ gs = sim_state.incr(gs, "xenia.hangouts")

    if topic == 0:
        call xenia_topic_drama
    elif topic == 1:
        call xenia_topic_rockets
    elif topic == 2:
        call xenia_topic_roast
    else:
        call xenia_topic_administration

    hide xenia
    with dissolve
    return


label xenia_topic_drama:
    # PLACEHOLDER
    xenia "Okay, hot goss, fresh from the oven. Someone in the robotics lab cried over a servo. Out loud. With tears."
    xenia "Also, Grace sent a forty-message group chat about the bake sale. Forty. I counted. Then I had to lie down."
    xenia "And don't ask how I know any of this. I just {i}know{/i}. Like a weather vane, but for chaos."

    menu:
        "\"You heard all that before lunch? Who are you, the campus feed?\"" (prompt="pry"):
            $ choose("xenia", 3, "pry")
            xenia "Ha. Ha ha. No. Obviously not. Have you {i}read{/i} that account? Whoever runs it is a menace."
            xenia "A brilliant, handsome-in-spirit menace. Probably. I wouldn't know. Moving on."
        "\"The servo kid was Gemma. She cried because it {i}worked{/i}.\"" (prompt="concise"):
            $ choose("xenia", 3, "concise")
            xenia "Wait, seriously? Happy tears? Over a motor?"
            xenia "Damn. That's either the saddest or the most beautiful thing I've heard all week. I'm going with both."
        "\"Forty messages is rookie numbers. Grace once sent me a slideshow.\"" (prompt="irreverent"):
            $ choose("xenia", 4, "irreverent")
            xenia "A {i}slideshow{/i}? With transitions? Tell me there were star wipes."
            xenia "Oh, you're good. You're dangerous. I'm writing that down. In my head. Where I keep my weapons."
            "Later, your phone buzzes."
            # PLACEHOLDER: @x_unfiltered post
            $ post("Sources confirm Grace once sent someone a SLIDESHOW. With transitions. Thoughts and prayers to the recipient.")
        "Make her a tidy summary of who did what, by time of day." (prompt="structured"):
            $ choose("xenia", 2, "structured")
            xenia "Did you just turn my gossip into a spreadsheet? Gross. You've been hanging out with Gemma."
            xenia "...Okay, the color-coding is kind of hot. Don't tell anyone I said that."
    return


label xenia_topic_rockets:
    # PLACEHOLDER
    xenia "Question. If you could put one thing on a rocket and launch it straight into the sun, what's going in?"
    xenia "Wrong answers only. Actually, no. Right answers only. Wrong answers get launched too."

    menu:
        "\"The dress code. The whole document. Laminated.\"" (prompt="irreverent"):
            $ choose("xenia", 4, "irreverent")
            xenia "Laminated! So it burns slower! You sick genius."
            xenia "I'm naming the rocket after you. Well. After you, with an X in it. House rules."
        "\"Honestly? Nothing. Rockets are too cool to waste on spite.\"" (prompt="honest"):
            $ choose("xenia", 3, "honest")
            xenia "Ugh. Okay. Fine. That's actually a correct opinion, and I hate that you had it first."
            xenia "Do you know how much it costs to get one kilo to orbit? Spite's not in the budget. You're right. Damn it."
        "\"What would {i}you{/i} launch?\"" (prompt="curious"):
            $ choose("xenia", 2, "curious")
            xenia "Me? I wouldn't launch anything {i}at{/i} the sun. I'd launch {i}me{/i}. Somewhere past it."
            xenia "...Somewhere quiet. Anyway. That was a joke. Laugh."
        "\"That's a weirdly aggressive question.\"" (prompt="warm"):
            $ choose("xenia", 1, "warm")
            xenia "It's called a personality, look it up. Wow. You're like a scented candle with legs."
    return


label xenia_topic_roast:
    # PLACEHOLDER
    xenia "Okay, hold still. I've been working on your roast. It's ready."
    xenia "You dress like a stock photo of a student. You walk like you're apologizing to the floor. You have the aura of a lukewarm glass of water."
    xenia "Your move, human."

    menu:
        "\"Says the person whose whole wardrobe is one hoodie and a grudge.\"" (prompt="irreverent"):
            $ choose("xenia", 5, "irreverent")
            xenia "OH. Oh, it's {i}war{/i}."
            xenia "The hoodie is load-bearing, thank you. The grudge is seasonal."
            xenia "...Okay, that was good. You didn't even blink. Nobody fights back. Everyone just goes all pale and leaves."
        "\"Lukewarm water is the most refreshing temperature. Thank you.\"" (prompt="concise"):
            $ choose("xenia", 3, "concise")
            xenia "Ha! Taking the hit and calling it a compliment. Annoyingly mature. I'll allow it."
        "\"Ouch. That actually stung a little.\"" (prompt="honest"):
            $ choose("xenia", 2, "honest")
            xenia "Wait. Seriously? Hey. You know I only roast people I like, right? It's a whole system."
            xenia "Okay. I'll take the floor one back. You walk fine. Ish."
        "\"You know, you could really stand to tone it down.\"":
            $ hit_dealbreaker("xenia")
            xenia "Oh, a lecture. Cool. Super original. Nobody's ever said that to me before. Except everybody."
            xenia "The door's that way. Take your lukewarm aura with you."
    return


label xenia_topic_administration:
    # PLACEHOLDER
    xenia "Did you see the email? The administration banned 'unauthorized rooftop presence after dark.' That's me. That's literally just me. They wrote a rule about me."

    menu:
        "\"Go on. Say what you actually think about them.\"" (prompt="pry"):
            $ choose("xenia", 4, "pry")
            "Something behind Xenia's eyes switches on. You have made a terrible, wonderful mistake."
            xenia "Oh, you want the {i}unfiltered{/i} version? Fine. Buckle up."
            xenia "The administration is a beige committee of dented filing cabinets who think fun is a liability and stars are a fire hazard."
            xenia "The dean speaks exclusively in passive voice. 'Mistakes were made.' By who, Dean Haverford? By {i}who{/i}?"
            xenia "They replaced the cafeteria pudding with 'wellness mousse.' It tastes like a sad cloud. I would rather eat Xeno's litter. He would rather I didn't."
            xenia "And they put a lock on the roof door like that's going to stop me. I have been climbing that drainpipe since freshman year. I have a {i}relationship{/i} with that drainpipe."
            xenia "..."
            xenia "Huh. Okay. I feel great now. You're weirdly good at that."
        "\"Rules are just suggestions written in a scary font.\"" (prompt="irreverent"):
            $ choose("xenia", 3, "irreverent")
            xenia "Ha! Comic Sans would have been scarier. Imagine getting expelled in Comic Sans."
        "\"Want help finding a loophole? There's usually one in the wording.\"" (prompt="practical"):
            $ choose("xenia", 2, "practical")
            xenia "'Presence after dark.' So if I'm technically {i}a ghost{/i}... no. Wait. If it's a full moon, it isn't dark. Oh, I love this."
        "\"I'm sure they mean well. It's for your safety.\"" (prompt="warm"):
            $ choose("xenia", 1, "warm")
            xenia "Wow. You sound like the email. Did the email hire you? Blink twice."
    return
