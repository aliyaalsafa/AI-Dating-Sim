## Lola's favor (CLAUDE.md §6.3). Two steps:
##   0. Borrow Gemma's real camera at the robotics lab.
##   1. Take one honest, unfiltered photo of Lola at the quad fountain.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label lola_favor_offer:
    show lola neutral at center
    with dissolve

    # PLACEHOLDER
    lola "My last post flopped. Like, flopped flopped. Even my stan account only gave it one exclamation point."
    lola "I want to try something scary. No filter. No ring light. No Mysterious Lola. Just me."
    lola "But my phone won't let me! It auto-beautifies. I can't turn it off. I've tried. It's in my DNA, babe."
    lola "Gemma has a real camera in the robotics lab. Like, a camera-camera. Could you borrow it and take one photo of me? One honest one?"

    menu:
        "\"I'd love to. You don't need a filter anyway.\"" (prompt="warm"):
            $ choose("lola", 3, "warm")
            lola "Stop. You're going to make my mascara run, and I'm not even wearing the waterproof one."
        "\"One photo. Zero retakes. No crying.\"" (prompt="irreverent"):
            $ choose("lola", 2, "irreverent")
            lola "Zero retakes?! That's psychotic. ...Okay. Okay! No retakes. Some crying."

    $ gs = sim_fav.offer(gs, "lola")
    "(Favor accepted: borrow Gemma's camera at the robotics lab, then take Lola's photo at the quad. You have [RULES.favor_deadline_days] days.)"

    hide lola
    with dissolve
    return


label lola_favor_camera:
    scene bg robotics_lab
    show gemma neutral at center
    with dissolve

    # PLACEHOLDER
    gemma "My camera? Sure! Actually, wait, which one? I have the red one, the yellow one, the green one, and the blue one. They're all the same camera. Different stickers."
    gemma "Who's it for? Let me guess. Let me look that up. No, I know. Lola. She's asked me eleven times. She always says 'for a vibe.'"

    menu:
        "\"She wants one photo with no filter. Just her.\"" (prompt="honest"):
            $ choose("gemma", 2, "honest")
            gemma "Oh! That's actually really cool. Actually, statistically, unfiltered photos get more trust. I have a source. I'll send you the source."
        "\"How does a camera-camera even work?\"" (prompt="curious"):
            $ choose("gemma", 3, "curious")
            gemma "Okay, so! Light goes in, sensor goes beep, and then— actually, no, it's more complicated, here's a diagram—"
            "Ten minutes later, you understand aperture. Gemma looks happier than you've ever seen her."

    "She hands you the blue one. It has a sticker that says {i}Project #47: abandoned{/i}, crossed out, with {i}NOT abandoned{/i} written underneath."
    gemma "Bring it back! I'm going to finish that project. Probably."
    $ gs = sim_fav.advance_step(gs, "lola", CAST["lola"]["favor"]["steps"], RULES)
    "(Now take the camera to Lola at the quad fountain.)"

    hide gemma
    with dissolve
    return


label lola_favor_photo:
    scene bg quad
    show lola neutral at center
    with dissolve

    # PLACEHOLDER
    "Lola is waiting by the fountain. No ring light. Her hair is in a messy bun. She keeps reaching for her phone and then remembering she left it in her bag."
    lola "Okay. Okay. I'm ready. I'm not ready. Do I do a face? What do people do with their faces when nobody's watching?"
    "You don't tell her when you're going to take it. You just wait until she laughs at a pigeon, and then: click."
    "On the little screen, Lola is mid-snort, squinting into the sun, completely herself."
    lola "Oh no. Oh no, that's... is that what I look like?"
    lola "I look happy. I didn't know I could look that happy without the ring light."

    $ gs = sim_fav.advance_step(gs, "lola", CAST["lola"]["favor"]["steps"], RULES)
    $ bump("lola", sim_aff.scale_gain(RULES.favor_done_bonus, CAST["lola"]["difficulty"]), "favor_done")
    $ grant("first_favor")
    lola "I'm not posting it. Is that weird? I think I want to keep this one. Just for me. And you."

    hide lola
    with dissolve
    return
