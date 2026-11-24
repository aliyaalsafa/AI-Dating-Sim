## M1 sample group scene: Gemma and Shen in the robotics lab.
## Shows a choice that moves two characters' affection differently.
## Replaced by real day 1–3 content in M2.

label group_lab_partners:
    show gemma neutral at left
    show shen neutral at right
    with dissolve

    # PLACEHOLDER: group scene dialogue
    gemma "Actually, the servo's calibrated wrong. Let me look that up. No, I know. It's off by three degrees."
    shen "Wait. Let me reconsider. Two point eight."
    gemma "...Two point eight. Fine. Citing you."

    menu:
        "Ask them how the robot works." (prompt="curious"):
            $ choose("gemma", 3, "curious")
            $ choose("shen", 1, "curious")
        "Offer to hold the screwdriver. Silently." (prompt="concise"):
            $ choose("gemma", 1, "concise")
            $ choose("shen", 3, "concise")

    shen "Good. Back to work."
    $ set_flag("seen_lab_partners")

    hide gemma
    hide shen
    with dissolve
    return
