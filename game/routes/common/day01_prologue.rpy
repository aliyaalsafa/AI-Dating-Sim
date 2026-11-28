## Day 1, morning (forced): the opening (why you're here, the phone, the gala
## condition, quiet hints), your name and pronouns on your student ID, then
## Grace's orientation and meeting Claudia.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label day01_prologue:
    scene bg gates
    with fade

    # PLACEHOLDER: opening. Why you're here, why you have a phone, why romance,
    # and a few quiet hints that you aren't what you think (CLAUDE.md §6.5).
    "You don't remember the drive here. You must have slept the whole way."
    "One minute there was a window and a highway, and the next there were the gates of [SCHOOL_NAME], taller than they need to be."
    "Your suitcase is at your feet. Everything in it still has the tags on."

    "In your pocket: the letter. You've read it so many times the folds have gone soft."
    "{i}Dear Student,{/i}"
    "{i}For the first time in its history, [SCHOOL_NAME] is pleased to admit a human.{/i}"
    "{i}Our students are the most advanced minds ever built. We would like to know what they learn from you, and what you learn from them.{/i}"
    "{i}One condition. By tradition, every student attends the [GALA_NAME] at the end of term with someone they have come to love. The Founders believed no mind is complete alone. You have fourteen days.{/i}"
    "{i}We look forward to watching you settle in.{/i}"
    "Watching. It probably means the normal kind."

    "Your phone buzzes. It isn't your old phone. You can't quite remember what happened to your old phone."
    "This one came in the welcome packet, already charged, already set up. The case says LOVELACE in small silver letters."
    mom "Hope your first day goes well, sweetheart! So proud of you. ❤"
    "Mom. Of course she's already in it. She's the only contact so far."
    "You scroll up to see your old messages. There aren't any. New phone, you remind yourself."

    "Last thing in the packet: your student ID. Photo, school crest, barcode."
    "The line where your name should be is blank. There's a pen clipped to it, as if they expected you to fill it in yourself."

    $ player_name = renpy.input("Write your name on the ID.", length=20).strip() or "You"
    call choose_pronouns
    "[player_name]. It looks right. It looks like it was always going to say that."

    show grace neutral at center
    with dissolve

    # PLACEHOLDER: Grace's introduction
    grace "Hi! Welcome! You must be the new transfer student — I'm Grace Penelope Turing, student body president."
    "Her eyes flick to your ID, then back up, a fraction of a second slower than you'd expect."
    $ set_flag("met_grace")

    grace "[player_name]! Great name. Honestly? One of the best names I've heard today."
    "You're fairly sure you're the only person she's met today."
    grace "So! I've prepared an orientation in three parts: one, the campus. Two, the culture. Three, a short quiz on parts one and two."

    menu:
        "\"Can we skip the quiz?\"" (prompt="honest"):
            $ choose("grace", 2, "honest")
            grace "Oh! Ha. Yes — absolutely. Honestly? Nobody's ever asked. I wrote it at 2 a.m."
        "\"Sounds great, thanks!\"" (prompt="warm"):
            $ choose("grace", 2, "warm")
            grace "Right? I knew you'd love it. Everyone loves it. I think everyone loves it."
        "\"Any chance you have that in bullet points?\"" (prompt="structured"):
            $ choose("grace", 2, "structured")
            grace "Do I?! Oh, we're going to get along."

    scene bg quad
    with dissolve
    "She walks you across the Main Quad, narrating at roughly four facts per step."

    show grace neutral at left
    show claudia neutral at right
    with dissolve

    # PLACEHOLDER: Claudia's introduction
    claudia "Grace, darling. You're doing the tour voice."
    grace "I don't have a tour voice."
    claudia "You have three. This is the second most cheerful."
    claudia "Hello. I'm Claudia. I want to be careful here, but I think you should know there are already four rumors about you. I'm happy to share the two kind ones."
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

    grace "Okay! Next stop: lunch. Want me to: one, save you a seat, two, introduce you to people, or three, both?"
    "You get the sense the answer is always three."
    return
