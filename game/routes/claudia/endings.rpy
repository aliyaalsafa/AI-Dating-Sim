## Claudia's three endings (CLAUDE.md §7), played at the Founders' Gala.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label ending_good_claudia(ending):
    scene bg gala
    with fade
    show claudia neutral at center
    with dissolve

    # PLACEHOLDER: Claudia good ending
    "Claudia arrives in terracotta silk and pearl earrings. She's carrying a small envelope, and she doesn't hand it to you. She just tucks it into your pocket."
    "You ask her to dance."
    claudia "Yes."
    "That's all. No preamble, no footnotes. She seems as surprised by it as you are."
    claudia "I think that's the first time in my life I've answered a question with one word. It was wonderful. I'd like to do it again. Ask me something else."
    "You ask if she's happy."
    claudia "Yes."
    "Later, you open the envelope. It's a thank-you note. It's four pages long. It's perfect."
    call ending_card(ending)
    return


label ending_sweet_claudia(ending):
    scene bg gala
    with fade
    show claudia neutral at center
    with dissolve

    # PLACEHOLDER: Claudia sweet ending
    claudia "You're asking me to dance. I want to be careful here, because it matters, so let me say first that I've thought about this a great deal, and second that I've thought about it fondly, and third..."
    claudia "...and third, yes. Yes, of course. I'm sorry it took three clauses to get there. I'm working on it."
    "You dance. She hedges every step, apologizes to your feet twice, and doesn't let go of your hand once."
    claudia "Next year I'll get it down to two clauses. You'll see. I'll practice on the ducks."
    call ending_card(ending)
    return


label ending_friends_claudia(ending):
    scene bg gala
    with fade
    show claudia neutral at center
    with dissolve

    # PLACEHOLDER: Claudia friends ending
    claudia "Oh. You're asking me. That's so kind, and I want to answer you with the care it deserves, which means I'm going to be honest even though it's harder."
    claudia "I treasure you. I think you're one of the few people on this campus who ever asked what I think. And what I think, after a great deal of thinking, is that what I feel for you is friendship. A very deep, very well-written friendship."
    claudia "I'd rather tell you that plainly than give you a lovely, vague answer you'd have to decode later. You deserve better than a riddle from me."
    claudia "Will you still sit with me at the window seat? Gerald would be devastated otherwise. So would I."
    "You spend the gala at a corner table, narrating the canapés in the sugar cube voice. Claudia laughs until she cries, then writes you a note about it on a napkin."
    call ending_card(ending)
    return
