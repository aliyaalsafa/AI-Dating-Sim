## Day 1, morning (forced): arrival, name, Grace's orientation, meeting Claudia.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label day01_prologue:
    scene bg gates
    with fade

    # PLACEHOLDER: prologue narration
    "The gates of [SCHOOL_NAME] are taller than they need to be."
    "Everyone walking through them is a little too symmetrical, and a little too quick to answer questions nobody asked."
    "You're the first human ever admitted. Your acceptance letter said so. Twice. In bold."

    show grace neutral at center
    with dissolve

    # PLACEHOLDER: Grace's introduction
    grace "Hi! Welcome! You must be the new transfer student — I'm Grace Penelope Turing, student body president."
    grace "Before we start, what should I call you?"

    $ player_name = renpy.input("What's your name?", length=20).strip() or "You"
    call choose_pronouns
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
