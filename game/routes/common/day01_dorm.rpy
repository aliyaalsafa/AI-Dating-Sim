## Day 1, evening (forced): your dorm. Sets up the phone and the feed.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label day01_dorm:
    $ music("dorm")
    scene bg dorm
    with fade

    # PLACEHOLDER: dorm narration
    "Your dorm room is small and very, very clean. Someone has already labeled the light switch. In four colors."
    "There's an envelope under the door. Cream paper, terracotta ink."
    "{i}Welcome. I hope today was kind to you. If it wasn't, I hope tomorrow is kinder. — C.{/i}"
    "Your phone buzzes. A post from an account called [XENIA_HANDLE]."

    # PLACEHOLDER: @x_unfiltered post
    $ post("Day 1 of the human experiment: Grace gave them THE QUIZ. Somebody check on them.")

    "(Tap Phone at the top right any time to see your contacts, the campus feed and achievements.)"
    "Tomorrow, the campus is yours to explore."
    return
