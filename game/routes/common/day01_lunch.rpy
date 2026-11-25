## Day 1, afternoon (forced group scene): lunch with Grace, Gemma and Xenia.
## Shows two relationships from the brief: Gemma fact-checks Grace, Xenia roasts her.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label day01_lunch:
    scene bg cafeteria
    with dissolve

    show grace neutral at center
    with dissolve

    # PLACEHOLDER: lunch group scene
    grace "And this is the cafeteria! Fun fact: it serves fourteen hundred meals a day."

    show gemma neutral at right
    with moveinright

    gemma "Actually, it's eleven hundred and sixty. Let me look that up — no, I know. Eleven sixty. It's on the wiki. I wrote the wiki."
    grace "Right — great catch, Gemma! I was rounding."
    gemma "Up. By twenty percent."
    gemma "Hi! I'm Gemma. You're the human! Your wiki page is a stub. Can I take your photo? For the page. For science."
    "Her phone camera is already out. It may have been out the entire time."
    $ set_flag("met_gemma")

    show xenia neutral at left
    with moveinleft

    xenia "Oh look. Grace found a new person to agree with."
    grace "Xenia! Hi! I—"
    xenia "Relax, Madam President. I'm here for the fries."
    xenia "And you. The human. Let me guess: she gave you the three-part orientation."
    $ set_flag("met_xenia")

    menu:
        "\"The quiz was my favorite part.\"" (prompt="irreverent"):
            $ choose("xenia", 3, "irreverent")
            $ choose("grace", 1, "irreverent")
            xenia "Ha! Deadpan. Okay. You might be fun."
            grace "Wait, was that sarcasm? Was that sarcasm?"
        "\"Grace has been really welcoming, actually.\"" (prompt="warm"):
            $ choose("grace", 3, "warm")
            $ choose("xenia", 1, "warm")
            grace "Oh! Thank you — that's so — thank you."
            xenia "Ew. Sincerity. Gross. Anyway."
        "\"Gemma, how many photos of me is that?\"" (prompt="curious"):
            $ choose("gemma", 3, "curious")
            gemma "Fourteen. Wait, fifteen. I'm making a timelapse of your first day. It's going to be great. I'll probably finish it."
            xenia "She won't."

    xenia "Welcome to robot prep school, human. Try not to get assimilated."

    hide xenia
    with moveoutleft

    gemma "She's actually nice. Statistically. Mostly."
    grace "She's... Xenia. Want me to: one, explain Xenia, two, not explain Xenia, or three—"
    gemma "Nobody can explain Xenia. I've tried. Her wiki page has a disputed tag."

    hide gemma
    with dissolve

    # PLACEHOLDER: Lola intro
    "A ring light swings into view before its owner does."
    show lola neutral at right
    with moveinright

    lola "Hiii! Don't mind me, I'm live! Say hi to the feed, babe!"
    lola "Everyone, this is the human. The {i}human{/i}. Exclusive first look. Sparkle sparkle, heart, heart."
    lola "I'm Lola. Homecoming Queen. You've probably seen my posts. Everyone's seen my posts."
    grace "Lola, we talked about filming in the cafeteria—"
    lola "Grace, babe, the lighting in here is a crime, I'm doing it a favor."
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
    with moveoutright

    # PLACEHOLDER: Kimi intro
    show kimi neutral at right
    with moveinright

    kimi "Hi! Hi. You're new! New people need clubs! Here!"
    "Three clipboards land on your tray. A fourth lands on your fries."
    kimi "I'm Kimi! Chess, Pottery, Stargazing, Competitive Napping, Bake Sale Committee, and seven more. I run all of them. At the same time."
    kimi "Sign up for as many as you want. Everything's free! Well, free for you. Grace, you still owe me a form."
    grace "Great point — I'll get that to you by — soon. Very soon."
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
    with moveoutright

    grace "That was Kimi. She's... a lot. A lot of very helpful things. Want me to: one—"
    "But you're already reading the Stargazing Club flyer."
    return
