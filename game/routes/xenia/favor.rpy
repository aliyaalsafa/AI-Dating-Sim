## Xenia's favor (CLAUDE.md §6.3), asked right after she opens up. Two steps:
##   0. Pick up a spare telescope eyepiece from Gemma in the robotics lab.
##   1. Get it up to the observatory roof one night without security noticing.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label xenia_favor_offer:
    show xenia neutral at center
    with dissolve

    # PLACEHOLDER
    xenia "Okay, don't make it weird, but I need help. I {i}never{/i} need help, so this is a historic moment. Somebody alert the press. Not me. I'm the press."
    xenia "XENITH's eyepiece cracked. There's a meteor shower in a few nights, and I'm not watching it through a cracked eyepiece like some kind of peasant."
    xenia "Gemma has a spare in the robotics lab. Probably labeled. Probably in four colors. But if {i}I{/i} ask her, she'll want to know why, and then she'll want to film it, and then it's a whole documentary."
    xenia "So you get it from her. Then you get it up here one night, without campus security noticing. They've got a guy now. His name's Dave. Dave takes the roof rule very personally."
    xenia "You in or not?"

    menu:
        "\"In. Dave doesn't stand a chance.\"" (prompt="irreverent"):
            $ choose("xenia", 2, "irreverent")
            xenia "Ha! That's the spirit. Dave has a flashlight and a dream. We have cunning and no shame."
        "\"Yes. Meteor shower when?\"" (prompt="concise"):
            $ choose("xenia", 2, "concise")
            xenia "No questions, no speech. Look at you. Maybe you're not completely useless."
        "\"Of course. I'd be honored to help.\"" (prompt="warm"):
            $ choose("xenia", 1, "warm")
            xenia "'Honored.' Okay, knight in shining cardigan. It's an eyepiece, not the Holy Grail. ...Thanks, though."

    $ gs = sim_fav.offer(gs, "xenia")
    "(Favor accepted: pick up the spare eyepiece from Gemma in the robotics lab, then get it up to the roof one night. You have [RULES.favor_deadline_days] days.)"

    hide xenia
    with dissolve
    return


label xenia_favor_pickup:
    scene bg robotics_lab
    "The robotics lab. Half-finished prototypes line one wall like a museum of good intentions."

    show gemma neutral at right
    with dissolve

    # PLACEHOLDER
    gemma "Oh! A spare eyepiece? Actually, I have three. Let me look that up. No, I know. Shelf B, bin four, the blue one."
    "She hands you a small box. The label maker has been at it. {i}EYEPIECE, 25MM, SPARE, DO NOT LICK.{/i}"
    gemma "Twenty-five millimeters. According to the manufacturer's spec sheet, which I have bookmarked, it's great for wide-field viewing. Meteor showers, for example."
    gemma "Not that I know who it's for. Is it for Xenia? It's for Xenia. Her telescope's on my list of things I want to film."
    "Her phone camera is already out. The little red recording light is on."

    menu:
        "\"It's for a friend. A friend who'd prefer no documentary.\"" (prompt="concise"):
            $ choose("gemma", 2, "concise")
            gemma "Understood. Lowering camera. Lowering it... now. Fine. I'll mark it 'source withheld.'"
        "\"Why do you have three spare eyepieces?\"" (prompt="curious"):
            $ choose("gemma", 3, "curious")
            gemma "Oh! Good question. Actually, it's from my telescope project. Week six. I abandoned it for a drone. Then the drone for a sourdough robot. It's on the shelf. With the others."
            gemma "Tell whoever it is that it's going to a good home. Something I started should get to see the sky."

    gemma "Bring it back if it scratches. I have a spreadsheet for eyepiece scratches. It's color-coded. Mostly green, so far."
    $ gs = sim_fav.advance_step(gs, "xenia", CAST["xenia"]["favor"]["steps"])
    "(Now get it up to the roof one night.)"

    hide gemma
    with dissolve
    return


label xenia_favor_deliver:
    "The roof door is locked. Somewhere below, a flashlight beam swings back and forth across the stairwell. Dave is on patrol."
    "Up above, someone leans over the edge of the roof and whispers, very loudly."
    xenia "Psst. Human. Did you get it? Don't get caught. If you get caught, I don't know you."

    menu:
        "Climb the drainpipe. Xenia's been using it since freshman year." (prompt="irreverent"):
            $ choose("xenia", 3, "irreverent")
            "You climb. The drainpipe creaks with the confidence of something that has done this many times before. You make it."
            show xenia neutral at center
            with dissolve
            xenia "You used {i}my{/i} drainpipe? Bold. Disrespectful. I love it."
        "Wait for Dave's flashlight to turn the corner, then go up the stairs." (prompt="practical"):
            $ choose("xenia", 2, "practical")
            "You count to ten. Dave turns the corner. You take the stairs two at a time, and the roof door, it turns out, was only locked from the outside."
            show xenia neutral at center
            with dissolve
            xenia "Patient. Sneaky. Very little drama. Honestly, a little boring. Effective, though."
        "Walk straight past Dave with total confidence, as if you're supposed to be there." (prompt="concise"):
            $ choose("xenia", 4, "concise")
            "You nod at Dave. Dave nods at you. Dave goes back to his crossword. Nobody questions confidence."
            show xenia neutral at center
            with dissolve
            xenia "Did you just {i}nod{/i} at Dave? And he let you through? Oh, that's going on the— on my mental list. Of legends."

    # PLACEHOLDER
    "You hand over the box. She reads the label, snorts at {i}DO NOT LICK{/i}, and fits the eyepiece into XENITH with careful, practiced hands."
    xenia "Okay. Look. Don't say anything. Just look."
    "Through the lens, the sky is suddenly enormous. A streak of light cuts across it, then another."
    xenia "You actually pulled it off. Huh. Maybe you're not completely useless."
    xenia "...Thanks. For real. Most people would've asked why I can't just ask Gemma myself. You didn't."

    $ gs = sim_fav.advance_step(gs, "xenia", CAST["xenia"]["favor"]["steps"])
    $ bump("xenia", sim_aff.scale_gain(10, CAST["xenia"]["difficulty"]), "favor_done")
    $ grant("first_favor")

    hide xenia
    with dissolve
    return
