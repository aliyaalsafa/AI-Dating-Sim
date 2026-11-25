## Pair scene: Grace + Claudia in the student council office (CLAUDE.md §4, §6.5).
## Old friends; Claudia is the only one who knows Shen scares Grace.
## Ends by calling pair_done, which shows this pair's two hints from data/mystery.rpy.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label pair_grace_claudia:
    show grace neutral at left
    show claudia neutral at right
    with dissolve

    # PLACEHOLDER
    "The council office door is open. Grace is at her desk. Claudia is in the good chair, holding a teacup like she owns the building, which, through a trust, she might."
    claudia "I brought you a note. Before you ask, yes, it's about the budget meeting, and no, it isn't scolding. It's mostly encouragement, with one gentle footnote."
    grace "Great! Thank you! I love footnotes. What's the footnote?"
    claudia "That you agreed with all four people who spoke, in a row, and they wanted four different things."
    grace "That's— okay, that's fair. In my defense, all four of them made really good points."
    claudia "They did. Then the fifth person spoke, and you agreed with him too."
    grace "Was there a fifth person?"
    claudia "There was a janitor. He said the room was cold. You formed a committee."
    grace "...The thermostat committee is doing very important work, Claudia."
    claudia "I'm sure it is. I'll write it a note."
    "Grace laughs, a real one, not the debate-club one. Then the office phone buzzes with a calendar reminder, and her face changes."
    grace "Study group. Library. Third floor."
    claudia "Ah. Third floor. I'm sorry, I can sit with you for a while if you'd like. I'd be very quiet and very obviously reading."
    grace "No! No, it's fine. I'm fine. It's just a library. With a person in it. Who is fine."
    "Claudia says nothing, which somehow says a great deal."

    menu:
        "\"Is someone on the third floor giving you trouble?\"" (prompt="pry"):
            $ choose("claudia", 1, "pry")
            $ choose("grace", 1, "pry")
            claudia "I think that's Grace's to answer, if she'd like to. I hope you don't mind my saying so."
            grace "Nobody! Nobody is trouble. Everybody on every floor is great."
        "\"You don't have to be fine. You can just be in the office.\"" (prompt="warm"):
            $ choose("grace", 3, "warm")
            $ choose("claudia", 2, "warm")
            grace "Oh. That's— huh. Can I? Is that allowed? I'm the president. I could make it allowed."
            claudia "That's very kind of you. I've been trying to tell her that for six years, at greater length."
        "\"Who's the scariest person on the third floor, then?\"" (prompt="irreverent"):
            $ choose("claudia", 2, "irreverent")
            $ choose("grace", -1, "irreverent")
            claudia "Oh, that's rather good. I won't answer it, but it's good."
            grace "There's no scariest person! Ha. Hahaha. Next agenda item."

    "Grace pulls a folder out of her bottom drawer, looks at it, and puts it back without opening it."
    "Claudia lowers her voice. Neither of them seems to remember you're sitting by the door."
    claudia "You looked at it again."
    grace "I always look at it. I just don't open it. It's about the new student, and if I open it I have to decide something."

    call pair_done("grace_claudia")

    hide grace
    hide claudia
    with dissolve
    return
