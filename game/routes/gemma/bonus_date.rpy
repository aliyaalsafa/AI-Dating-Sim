## Gemma's bonus date (CLAUDE.md §6.4), affection 75+: the robotics lab after
## midnight, her favorite place.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label gemma_bonus_date:
    show gemma neutral at center
    with dissolve

    # PLACEHOLDER
    "The robotics lab after midnight. The overhead lights are off. Every screen and status LED glows red, yellow, green or blue, like a very nerdy aquarium."
    gemma "You came! It's twelve-oh-four. Actually, twelve-oh-five. Come here, come here, I built something."
    "On the workbench is a small, lopsided robot with a round face. It rolls toward you, stops, and displays your name."
    gemma "I built it just for you. In one week. Start to finish. It doesn't do anything useful. It just says hi to you. Only you."
    "Her phone is face-down on the bench. She hasn't touched it once."

    menu:
        "\"How does it know it's me?\"" (prompt="curious"):
            $ choose("gemma", 5, "curious")
            gemma "Okay, so, facial recognition, but I trained it on— wait. Hm. I trained it on the photos I took of you. All of them."
            gemma "That's a lot of photos. That's maybe a concerning number of photos. It's a very well-trained robot."
            "The robot says hi to you again. Gemma laughs so hard she has to sit down."
        "\"It's perfect. Don't change anything.\"" (prompt="warm"):
            $ choose("gemma", 3, "warm")
            gemma "Don't change anything. I've never had a project where that was an option."
            gemma "Okay. I won't. It's finished. It's the second finished thing ever. Both because of you."
        "\"You're not taking a photo of this?\"" (prompt="pry"):
            $ choose("gemma", 2, "pry")
            gemma "No. I don't want to. Isn't that weird? I always want to."
            gemma "I think I take photos so I can look things up later. I don't need to look this up. I'll remember it."

    $ set_flag("gemma.bonus_date_done")
    gemma "Stay a bit? The lab's quiet till six. I'll explain the LEDs. All of them. You'll love it. Actually, you'll tolerate it. That's enough."

    hide gemma
    with dissolve
    return
