## Lola's Monogamous ending: at the gala the player has just told everyone they
## are an AI (the semester was a secret Turing test). Lola stands by them.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label ending_mono_lola(ending):
    scene bg gala
    with fade
    show lola neutral at center
    with dissolve

    # PLACEHOLDER: Lola Monogamous ending
    "The ballroom goes silent. Every phone in the room comes out at once. Every phone but one."
    "Lola steps out of the crowd, puts her own phone face-down on the nearest table, and walks over to you."
    lola "Okay. So you're not the human. Big reveal. Huge. Trending, probably."
    lola "Babe, I literally won Homecoming as a completely different person. I'm the last girl here who gets to judge anybody for having a persona."
    lola "And you never had one with me. Everyone else liked my feed. You liked me with crumbs on my face."
    "Behind her, the other girls whisper. Lola doesn't look back at them. She takes the instant camera out of her clutch."
    lola "Smile. No filter. This one's for us."
    "Click. In the photo, you're both laughing."
    call ending_card(ending)
    return
