## Kimi story beat: she opens up (CLAUDE.md §4: always ranked third, treated as
## the free alternative rather than a person). The engine calls kimi_favor_offer
## right after this scene.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label kimi_opens_up:
    show kimi neutral at center
    with dissolve

    # PLACEHOLDER
    "The activities hall is quiet for once. Kimi is alone, sorting club badges into twelve little piles. She doesn't look up right away."
    kimi "Hi. Sorry. I'm doing the thing where I'm in every club and none of them would notice if I left."
    kimi "Do you know what people call me? 'The free one.' Like, 'Grace is busy, ask the free one.' 'Claudia charges, ask the free one.'"
    kimi "I'm not free. I'm {i}generous{/i}. Those are different. One of them is a person."

    menu:
        "\"What would you do if nobody needed anything from you for a day?\"" (prompt="curious"):
            $ choose("kimi", 4, "curious")
            kimi "Nobody's ever... huh."
            kimi "I'd lie on the observatory roof and count stars. Not for a club. Just for me. I'd lose count on purpose."
        "\"Let's figure out which of the twelve you'd keep if you had to drop some.\"" (prompt="structured"):
            $ choose("kimi", 3, "structured")
            kimi "Drop some? I couldn't. They'd fall apart."
            kimi "...Or they wouldn't, and that would be worse. Okay. Let's make a list. A small one."
        "\"You're not the free version of anyone. You're you.\"" (prompt="warm"):
            $ choose("kimi", 2, "warm")
            kimi "That's a really nice sentence. I'm going to write it on a clipboard."
            kimi "I have a lot of clipboards. It'll be on all of them."

    kimi "Thanks for listening. Really listening. You're the first person this semester who stayed after I stopped handing things out."
    $ set_flag("kimi.opened_up")
    $ reveal("kimi", "likes")
    "(You learned what Kimi likes. Check your phone.)"
    kimi "Um. Actually. Since you're here, and you're the kind of person who listens... can I ask you for something? Just once?"

    hide kimi
    with dissolve
    return
