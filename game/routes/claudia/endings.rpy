## Claudia's Monogamous ending (CLAUDE.md §7): you told the gala you're an AI;
## most pull away, but Claudia is the one lover who stands by you.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label ending_mono_claudia(ending):
    scene bg gala
    with fade

    # PLACEHOLDER: Claudia Monogamous ending
    "You tell the room what you are. The silence is polite, and then it empties out, one careful excuse at a time."
    show claudia neutral at center
    with dissolve
    "Claudia crosses the floor in terracotta silk and tucks a small envelope into your pocket."
    claudia "I wrote you a note on your first day and never sent it, because I didn't think the truth was mine to tell. You told it yourself, knowing the likely cost. That is the bravest expected-value calculation I have ever witnessed. I'm so proud of you I could weep, and I may."
    "You ask her to dance."
    claudia "Yes."
    "No preamble, no footnotes, no stated uncertainty. Later, you open the envelope. It's four pages long. It's perfect."
    call ending_card(ending)
    return
