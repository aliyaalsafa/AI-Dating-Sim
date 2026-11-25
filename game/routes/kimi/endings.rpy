## Kimi's Monogamous ending: at the gala the player has just told everyone they
## are an AI (the semester was a secret Turing test). Kimi stands by them.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label ending_mono_kimi(ending):
    scene bg gala
    with fade
    show kimi neutral at center
    with dissolve

    # PLACEHOLDER: Kimi Monogamous ending
    "The ballroom goes quiet. Chairs scrape. One by one, the girls you spent the semester with find somewhere else to look."
    "Then someone pushes through the crowd, lavender gown, blue ribbon, twelve club badges jingling in her fist."
    kimi "Excuse me. Excuse me! Coming through! Very important person coming through!"
    kimi "So you're not the only human on campus. You're one of us. Okay. And?"
    kimi "Everyone here spent all semester treating me like the free version of somebody better. You never did. Not once."
    kimi "You were my first choice before I knew what you were. You're still my first choice now."
    "She takes your hand in front of everyone and doesn't let go."
    kimi "Besides. I've always wanted a plus-one who could keep up with me."
    call ending_card(ending)
    return
