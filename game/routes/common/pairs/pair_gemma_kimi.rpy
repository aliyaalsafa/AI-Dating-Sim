## Pair scene: Gemma + Kimi in the robotics lab (CLAUDE.md §4, §6.5).
## Kimi's swarm quietly adopts Gemma's abandoned projects.
## Ends by calling pair_done, which shows this pair's two hints from data/mystery.rpy.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label pair_gemma_kimi:
    show gemma neutral at left
    show kimi neutral at right
    with dissolve

    # PLACEHOLDER
    "The robotics lab is louder than usual. The shelf of Gemma's abandoned prototypes is empty. Every single one of them is switched on and running."
    gemma "Okay, who touched my graveyard?"
    kimi "Me! Hi! Well, technically my swarm. Well, technically the Tuesday half of my swarm. The chess club, the knitting circle and the drone team split it."
    gemma "That plant-watering robot was dead. I killed it. On purpose. It had a funeral."
    kimi "It waters the knitting circle's plants now! It's so happy. Look at it go."
    "A small four-colored robot trundles past, watering a cactus with great dignity."
    gemma "That's— actually, that's the version with the moisture sensor, which means you fixed the sensor, which I said was impossible, source: me."
    kimi "Oh, it wasn't impossible! It just needed a second person. And then a third person. And then nine more of me."
    gemma "And the translation glasses?"
    kimi "The language exchange club loves them! And the homework planner app runs the drama club. And the karaoke drone is, um, the karaoke drone."
    "The karaoke drone floats overhead, quietly singing a power ballad."
    gemma "You finished all of them. In a week. While running twelve clubs."
    kimi "You started all of them! That's the hard part! Finishing is just... a lot of people saying yes."

    menu:
        "\"Gemma, which one do you wish you'd finished yourself?\"" (prompt="curious"):
            $ choose("gemma", 3, "curious")
            $ choose("kimi", 2, "curious")
            gemma "The glasses. Obviously the glasses. Actually, no, the plant robot. Actually— both. Total confidence."
            kimi "Then take them back! They're yours. I'll make the swarm write you a handover doc. Twelve handover docs."
        "\"Make it official. One project, two names.\"" (prompt="structured"):
            $ choose("gemma", 2, "structured")
            $ choose("kimi", 3, "structured")
            kimi "Co-credit! A shared spreadsheet! Color-coded!"
            gemma "In red, yellow, green and blue. It's non-negotiable. Fine. Yes. Okay."
        "\"Kimi, you're like the free version of a whole lab.\"" (prompt="irreverent"):
            $ choose("kimi", -2, "irreverent")
            $ choose("gemma", 1, "irreverent")
            kimi "Ha! Yeah. The free version. Everybody says that."
            "She keeps smiling. It doesn't quite reach her eyes."

    "Gemma pulls up the campus wiki on the big screen to log the projects. Then she stops, and scrolls down to a page that isn't about robots."
    "Kimi leans in. Their voices drop, and the lab noise covers the rest. They've forgotten you entirely."
    kimi "Wait. Go back. Look at the date on that page."
    gemma "And you. Your swarm went looking for something last week. What did they find?"

    call pair_done("gemma_kimi")

    hide gemma
    hide kimi
    with dissolve
    return
