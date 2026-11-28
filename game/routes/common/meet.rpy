## Day 1 afternoon: exploring campus on your own after Grace's tour.
## Girls you haven't met show as "?" on the map. Visiting one plays her short
## first-meeting scene, and meeting people takes no time today. The evening
## starts once you've met everyone, so pair scenes can begin on day 2.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

init python:

    def unmet():
        return [c for c in CAST if not has_flag("met_" + c)]


label day01_explore:
    scene bg gates
    with dissolve
    # PLACEHOLDER
    "Grace's tour ends where it started, at the gates. Then her phone buzzes, and buzzes again."
    show grace neutral at center
    with dissolve
    grace "Okay, that's three meetings, a fire drill and a club charter, all at once. Bias for action!"
    grace "You'll be fine on your own. Go meet people! Everyone's around this afternoon."
    grace "Want me to: one, check in later, two, check in sooner, or three — no. You've got this."
    hide grace
    with dissolve
    "(Visit the campus map to meet everyone. Girls you haven't met show as ?. Meeting people takes no time today.)"

    while unmet():
        call screen campus_map
        $ _loc = _return
        if LOCATIONS[_loc].get("kind") == "shop":
            $ scene_music(_loc)
            scene expression "bg " + _loc
            call screen gift_shop
        else:
            scene expression "bg " + _loc
            with dissolve
            $ _new = [c for c in sim_ev.present(LOCATIONS, _loc, gs) if not has_flag("met_" + c)]
            if _new:
                call expression "meet_" + _new[0]
            elif sim_ev.present(LOCATIONS, _loc, gs):
                "Everyone here has already met you. Somebody new must be somewhere else."
            else:
                "Nobody's here right now."

    "The sun's getting low. You've met all of them: seven students, seven very different ways of being a person."
    "Or of seeming like one."
    return


label meet_claudia:
    show claudia neutral at center
    with dissolve
    # PLACEHOLDER: Claudia's introduction
    "A girl in a camel coat looks up from a window seat, fountain pen in hand, as though she's been expecting you for a while and is too polite to say so."
    claudia "Hello. I'm Claudia. I want to be careful here, but I think you should know there are already four rumors about you."
    claudia "By my estimate, two are kind, one is neutral, and one is unkind with perhaps sixty percent confidence. I'm happy to share the kind ones."
    $ set_flag("met_claudia")
    menu:
        "\"What are the other two?\"" (prompt="pry"):
            $ choose("claudia", 2, "pry")
            claudia "Ah. Those aren't mine to share. I'm sorry. I'd say the same about you, to them, if that helps."
        "\"What do {i}you{/i} make of me so far?\"" (prompt="curious"):
            $ choose("claudia", 2, "curious")
            claudia "...Oh. People usually ask what I know, not what I think."
            claudia "I think you seem kind. Give me a week and I'll have something more nuanced. Possibly an essay."
        "\"That's sweet of you. Thank you.\"" (prompt="warm"):
            $ choose("claudia", 2, "warm")
            claudia "Of course. I'll write you a welcome note. I write everyone one. Yours may run a little long."
    hide claudia
    with dissolve
    return


label meet_gemma:
    show gemma neutral at center
    with dissolve
    # PLACEHOLDER: Gemma's introduction
    "The robotics lab smells like solder. A girl with four colored hair clips is labeling a drawer of screws in red, yellow, green and blue."
    gemma "Oh! You're the human! Hi! I'm Gemma. Your wiki page is a stub. Can I take your photo? For the page. For science."
    "Her phone camera is already out. It may have been out the entire time."
    gemma "Grace told you the cafeteria serves fourteen hundred meals a day, didn't she. Actually, it's eleven hundred and sixty. I wrote the wiki."
    $ set_flag("met_gemma")
    menu:
        "\"How many photos of me is that?\"" (prompt="curious"):
            $ choose("gemma", 3, "curious")
            gemma "Fourteen. Wait, fifteen. I'm making a timelapse of your first day. It's going to be great. I'll probably finish it."
        "\"Sure. Get my good side.\"" (prompt="warm"):
            $ choose("gemma", 2, "warm")
            gemma "Both sides are statistically fine. That's a compliment. Source: me."
    hide gemma
    with dissolve
    return


label meet_xenia:
    show xenia neutral at center
    with dissolve
    # PLACEHOLDER: Xenia's introduction
    "In the back corner of the cafeteria, a girl in an all-black hoodie is eating fries and typing very fast with one thumb."
    xenia "Oh look. The human. Let me guess: Grace gave you the three-part orientation."
    $ set_flag("met_xenia")
    menu:
        "\"The quiz was my favorite part.\"" (prompt="irreverent"):
            $ choose("xenia", 3, "irreverent")
            xenia "Ha! Deadpan. Okay. You might be fun."
        "\"Grace has been really welcoming, actually.\"" (prompt="warm"):
            $ choose("xenia", 1, "warm")
            xenia "Ew. Sincerity. Gross. Anyway."
    xenia "I'm Xenia. Welcome to robot prep school. Try not to get assimilated."
    "Her phone lights up face-down on the table. She flips it over before you can see the screen."
    hide xenia
    with dissolve
    return


label meet_lola:
    # PLACEHOLDER: Lola's introduction
    "A ring light swings into view before its owner does."
    show lola neutral at center
    with dissolve
    lola "Hiii! Don't mind me, I'm live! Say hi to the feed, babe!"
    lola "Everyone, this is the human. The {i}human{/i}. Exclusive first look. Sparkle sparkle, heart, heart."
    lola "I'm Lola. Homecoming Queen. You've probably seen my posts. Everyone's seen my posts."
    $ set_flag("met_lola")
    menu:
        "Wave at the camera like you're on a talk show." (prompt="irreverent"):
            $ choose("lola", 2, "irreverent")
            lola "Okay, a natural! Love that. Laughing-crying face. You're going in the highlights."
        "\"Nice to meet you. The camera, too, I guess.\"" (prompt="warm"):
            $ choose("lola", 2, "warm")
            lola "Aww. Polite to the camera. Nobody's polite to the camera."
    lola "Okay, bye, babe! Follow me! I'll follow you back. Probably!"
    hide lola
    with dissolve
    return


label meet_kimi:
    show kimi neutral at center
    with dissolve
    # PLACEHOLDER: Kimi's introduction
    kimi "Hi! Hi. You're new! New people need clubs! Here!"
    "Three clipboards land in your arms. A fourth lands on top of those."
    kimi "I'm Kimi! Chess, Pottery, Stargazing, Competitive Napping, Bake Sale Committee, and seven more. I run all of them. At the same time."
    kimi "Sign up for as many as you want. Everything's free! Well, free for you. Not for anyone with a trust fund."
    $ set_flag("met_kimi")
    menu:
        "\"Which one should I start with?\"" (prompt="structured"):
            $ choose("kimi", 2, "structured")
            kimi "Oh, you're a planner! Start with Stargazing. It's the quiet one. Then everything else. Simultaneously."
        "Sign every single clipboard." (prompt="practical"):
            $ choose("kimi", 2, "practical")
            kimi "All of them? Nobody's ever signed all of them. I'm going to cry. I'm not going to cry. I'm a little bit going to cry."
    kimi "See you everywhere! I mean it. I'm everywhere."
    hide kimi
    with dissolve
    return


label meet_shen:
    show shen neutral at center
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
