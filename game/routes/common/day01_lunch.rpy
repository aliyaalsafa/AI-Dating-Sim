## Day 1, afternoon (forced group scene): lunch with Grace, Gemma and Xenia.
## Shows two relationships from the brief: Gemma fact-checks Grace, Xenia roasts her.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label day01_lunch:
    scene bg cafeteria
    with dissolve

    show grace placeholder at center
    with dissolve

    # PLACEHOLDER: lunch group scene
    grace "And this is the cafeteria! Fun fact: it serves fourteen hundred meals a day."

    show gemma placeholder at right
    with moveinright

    gemma "Actually, it's eleven hundred and sixty. Let me look that up — no, I know. Eleven sixty. It's on the wiki. I wrote the wiki."
    grace "Right — great catch, Gemma! I was rounding."
    gemma "Up. By twenty percent."
    gemma "Hi! I'm Gemma. You're the human! Your wiki page is a stub. Can I take your photo? For the page. For science."
    "Her phone camera is already out. It may have been out the entire time."
    $ set_flag("met_gemma")

    show xenia placeholder at left
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
    return
