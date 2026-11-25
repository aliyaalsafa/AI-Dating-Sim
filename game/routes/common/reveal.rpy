## The reveal (CLAUDE.md §6.5): plays when the player finds the 7th major clue.
## The player puts the pieces together, calls Mom, and reaches the Dean's office.
## The engine sets the flags; this scene only plays the moment.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label truth_reveal:
    scene bg dorm
    with fade

    # PLACEHOLDER: putting the clues together
    "You lay them out on your desk, one by one, the way Shen would. Step by step."
    "A scoresheet for \"Subject 1\". Human confidence: sixty-one percent."
    "A draft about a new kid with no baby pictures. A note on cream paper: {i}I think you should know what you are.{/i}"
    "A student page older than your birthday, revised 73 times. A spec sheet with your name and your pronouns on it, under \"persona traits\"."
    "An address that doesn't exist. Friends from home who were never anyone at all."
    "Every one of them had an innocent explanation. Stress. A new phone. Mom being busy."
    "Seven innocent explanations is not an explanation."
    "You haven't eaten since you got here. You've never been tired. Your camera roll starts the day you arrived."
    "You try to picture your bedroom back home. The color of the walls. It isn't there. It was never there. There's just a word: {i}home{/i}, with nothing behind it."

    # PLACEHOLDER: the call
    "Your hands are steady when you call Mom. That's the worst part. They should be shaking."
    "It rings once."
    mom "Hi, sweetheart!"
    "Relief hits so hard it hurts. Then the voice keeps going, in exactly the same tone."
    mom "Thank you for calling the Office of the Dean, Lovelace Academy. This line supports Subject 1 during the evaluation period."
    mom "Family messages are generated nightly to support subject stability. If you are experiencing distress, please continue normal activities."
    mom "Your evaluation concludes at the [GALA_NAME]. Hope your day went well, sweetheart! So proud of you."
    "The line clicks. You call again. {i}Hi, sweetheart!{/i} You hang up before the rest."

    # PLACEHOLDER: the life that was written for you
    "You scroll back through her texts. {i}Are you eating enough? The dog misses you. Remember the lake house?{/i}"
    "Templates. The same six sentences, shuffled. You never noticed, because you were built not to."
    "There is no lake house. There is no dog. There is no hometown; Kimi's swarm already told you that, and you thanked her for trying."
    "On your first morning, Grace asked what she should call you. You typed a name. You picked your pronouns from a list."
    "It felt like introducing yourself. It was configuration."
    "[player_name]. You say it out loud to the empty room. It sounds like a setting someone could change."
    "Everything you remember from before [SCHOOL_NAME] was written for you. Your whole life is a lie, and you were the only one who believed it."
    "And the girls you've spent the semester with, the ones who laughed at your jokes and held your hand, have been grading you the entire time."

    "The [GALA_NAME] is on day 14. You'll have to decide what to tell them."
    return
