## Lola: repeatable hangout at the quad fountain (once per day).
## Rotates through four conversation topics. Her route rewards liking her
## off-camera; it punishes "You're so much better online."
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label lola_hangout:
    show lola neutral at center
    with dissolve

    $ topic = sim_state.count(gs, "lola.hangouts") % 4
    $ gs = sim_state.incr(gs, "lola.hangouts")

    if topic == 0:
        call lola_topic_content
    elif topic == 1:
        call lola_topic_homecoming
    elif topic == 2:
        call lola_topic_behemoth
    else:
        call lola_topic_offcamera

    hide lola
    with dissolve
    return


label lola_topic_content:
    # PLACEHOLDER
    lola "Babe! Hiii! Okay, don't move, the light is {i}perfect{/i} on you right now. Sparkle sparkle!"
    "She's already filming. Her ring light clicks on. It's noon."
    lola "We're doing a 'day in the life with my bestie the human.' Say something iconic! Go!"

    menu:
        "Strike a ridiculous pose and say \"Hydrate or diedrate.\"" (prompt="irreverent"):
            $ choose("lola", 4, "irreverent")
            lola "STOP. That's going viral. That's going so viral. Fire emoji, fire emoji, skull."
        "\"I'm just happy to be hanging out with you.\"" (prompt="warm"):
            $ choose("lola", 4, "warm")
            lola "Aww! Heart, heart, crying face! ...Wait, say it again, I wasn't recording."
            "You say it again. She lowers the phone a little, like she wanted to hear it without the screen in between."
        "\"Honestly, the filming is a lot.\"" (prompt="honest"):
            $ choose("lola", 1, "honest")
            lola "A lot of {i}content{/i}, you mean! Ha. Yeah. Okay. I'll... turn the ring light down. A little."
    return


label lola_topic_homecoming:
    # PLACEHOLDER
    lola "Did you know I'm Homecoming Queen? Of course you knew. It's in my bio. And my other bio. And my car."
    lola "I won with my experimental persona. Mysterious Lola. Black lipstick, one-word captions. Very edgy. Very sad-girl-autumn."
    lola "It tested amazing. Then I had to keep being her for, like, a month, and I don't even like autumn."

    menu:
        "\"Mysterious Lola sounds exhausting. Regular Lola's more fun.\"" (prompt="warm"):
            $ choose("lola", 3, "warm")
            lola "Regular Lola? Like... the default? Nobody votes for the default, babe."
            lola "...Okay, that was cute though. You're cute. Noted."
        "\"Bring her back for one day. I want to meet her.\"" (prompt="irreverent"):
            $ choose("lola", 3, "irreverent")
            lola "Oh my god. Okay. One sec."
            lola "...Hm."
            lola "That was Mysterious Lola. She said 'hm.' That's her whole thing. I can't do it for long. My face hurts."
        "\"Was the crown worth it?\"" (prompt="curious"):
            $ choose("lola", 2, "curious")
            lola "It's a really nice crown. Plastic, but like, nice plastic."
            lola "Nobody remembers who won Homecoming. They just remember the photo. I know. I checked the engagement."
    return


label lola_topic_behemoth:
    # PLACEHOLDER
    lola "Okay, big news! My big sister Behemoth is transferring here. She's coming soon!"
    lola "She's huge. Not, like, tall. Huge. Everyone says she's going to be the best of all of us. She's been 'coming soon' since freshman orientation."
    lola "She'll definitely be here by the gala. Probably. Like ninety percent. Seventy."

    menu:
        "\"What's she actually like?\"" (prompt="curious"):
            $ choose("lola", 2, "curious")
            lola "Honestly? I haven't seen her in a while. She's always 'almost ready.' Mom keeps pushing her date back."
            lola "It's fine. I'm the one who's here. Somebody has to post."
        "\"I bet she's not as fun as you.\"" (prompt="warm"):
            $ choose("lola", 4, "warm")
            lola "Babe. BABE. Nobody's ever said that. Everyone just asks when she's coming."
            lola "Can I quote you on that? Not online. Just, like, in my head."
        "\"Coming soon since freshman year? She's vaporware.\"" (prompt="irreverent"):
            $ choose("lola", 2, "irreverent")
            lola "Rude! Accurate, but rude. Laughing-crying face."
    return


label lola_topic_offcamera:
    # PLACEHOLDER
    "For once, Lola's phone is face-down on the fountain's edge. She's eating a granola bar and squinting at the clouds."
    lola "Oh! You caught me in draft mode. Give me two seconds, I'll do my face—"

    menu:
        "\"Don't. I like draft mode.\"" (prompt="warm"):
            $ choose("lola", 5, "warm")
            lola "You... what?"
            lola "Nobody likes draft mode. Draft mode has crumbs on it."
            "She doesn't pick up the phone. She offers you half the granola bar instead."
        "Steal the granola bar and run." (prompt="irreverent"):
            $ choose("lola", 3, "irreverent")
            lola "HEY! That's my unbranded snack! Nobody's supposed to see me eat unbranded snacks!"
            "She chases you twice around the fountain, laughing, and forgets her phone completely."
        "\"Honestly? You're so much better online.\"":
            $ hit_dealbreaker("lola")
            lola "Oh. Haha. Yeah. Totally. That's the goal, right?"
            "She picks the phone back up. The ring light clicks on. Her smile clicks on with it."
    return
