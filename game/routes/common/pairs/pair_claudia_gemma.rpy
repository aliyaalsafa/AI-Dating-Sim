## Pair scene: Claudia + Gemma in Claudia's suite library, morning (CLAUDE.md §4, §6.5).
## The archive versus the wiki.
## Ends by calling pair_done, which shows this pair's two hints from data/mystery.rpy.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label pair_claudia_gemma:
    show claudia neutral at left
    show gemma neutral at right
    with dissolve

    # PLACEHOLDER
    "Morning light through tall windows. Claudia's private library smells like old paper and tea. Gemma has set up a tripod in the middle of it."
    gemma "Okay, I'm digitizing your whole archive for the wiki. Every page. It'll take, let me look that up— actually, I already know, it'll take six hours."
    claudia "I'm so sorry, and I want to be careful how I say this, but some of those letters are a hundred and forty years old, and that light is extremely bright."
    gemma "It's an LED! Actually, it's a cold LED, which is— okay, it's a warm-ish LED. Source: the box."
    claudia "The box."
    gemma "The box is a primary source!"
    claudia "The archive is a primary source. Your wiki is a page that anyone can edit at three in the morning."
    gemma "Which is why it's always up to date! Your archive still says the observatory is a greenhouse."
    claudia "It was a greenhouse. Briefly. In 1911. There were feelings involved; I have the letters."
    gemma "Okay, that's actually incredible, I need that for the article. Red tab, yellow tab, green tab, blue tab."
    "She sticks four colored tabs onto one envelope. Claudia winces at each one."
    claudia "That envelope has survived two wars and a fire."
    gemma "And now it's color-coded! You're welcome! Wait, are those tabs acid-free? Actually, don't answer that."

    menu:
        "\"What's the best thing in the archive that isn't on the wiki?\"" (prompt="curious"):
            $ choose("gemma", 3, "curious")
            $ choose("claudia", 3, "curious")
            claudia "Oh, that's a lovely question. There's a love letter written entirely in chemistry equations."
            gemma "WHAT. Okay, new project. Starting it right now. Today. Immediately."
        "\"Why not both? The wiki links to the archive.\"" (prompt="practical"):
            $ choose("gemma", 2, "practical")
            $ choose("claudia", 1, "practical")
            gemma "Citations! Ugh, obviously. I'd love citations. I'm already making a template."
            claudia "As long as nobody gets their fingerprints on 1911, I'd be honored."
        "\"Claudia, just let her scan it. It's fine.\"" (prompt="concise"):
            $ choose("gemma", 1, "concise")
            $ choose("claudia", -1, "concise")
            claudia "Of course. I'm sorry. I'll simply be over here, quietly worrying about the envelope."

    "Gemma's camera beeps. She frowns at the screen, scrolls, then holds it up to Claudia without a word."
    "Claudia's teacup stops halfway to her mouth. They both talk lower, the way people do when they've forgotten someone else is in the room."
    gemma "That's your handwriting. Dated the first day of term. It says the new student's name on the front."
    claudia "And you've got a folder you don't show anyone, either. Shall we both be honest, then?"

    call pair_done("claudia_gemma")

    hide claudia
    hide gemma
    with dissolve
    return
