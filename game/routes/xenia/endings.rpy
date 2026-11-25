## Xenia's Monogamous ending (CLAUDE.md §7): you told the gala you're an AI;
## most pull away, but Xenia is the one lover who stands by you.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label ending_mono_xenia(ending):
    scene bg gala
    with fade

    # PLACEHOLDER: Xenia Monogamous ending
    "You tell the room what you are. The whispering starts before you've finished. People drift toward the walls."
    show xenia neutral at center
    with dissolve
    "Xenia pushes through them in a black suit, silver star earrings, phone in her pocket for once."
    xenia "Oh, {i}now{/i} everyone's scared of honesty? Cute. You all love it when it's me doing it."
    xenia "You know what the stars taught me? Everything's farther away than it looks, and closer than you think. I used to think that was sad."
    xenia "I don't anymore. ...Okay. That's enough sincerity. You look like a lukewarm glass of water, by the way. My favorite kind."
    "She pulls you onto the empty dance floor. Later, [XENIA_HANDLE] posts one line: {i}mine. fight me.{/i}"
    call ending_card(ending)
    return
