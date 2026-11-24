## Claudia story beat at affection 25: she opens up (CLAUDE.md §6.1), in her
## suite's private library.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label claudia_opens_up:
    show claudia placeholder at center
    with dissolve

    # PLACEHOLDER
    "Claudia's library is all dark wood and terracotta cushions. She's at her desk with a leather notebook open, and she closes it when you come in. Not quickly. Just carefully."
    claudia "Hello. Forgive me, I was drafting something. A letter. I'm not going to send it. I almost never do."
    claudia "May I ask you something, and may I apologize in advance for how long the question will be?"
    claudia "People come to me for what I know. Who's dating whom, who failed what, who's secretly in three clubs under a pseudonym. And I'm careful, I truly am, I only share what I think should be shared."
    claudia "But I've started to worry that being careful is all I am. That if you took away the secrets, there'd be a very polite empty chair."

    menu:
        "\"Then tell me something you think. Not something you know.\"" (prompt="curious"):
            $ choose("claudia", 5, "curious")
            claudia "Something I think. All right. Give me a moment, I want to choose well."
            claudia "I think the fountain on the quad is ugly, and I think everyone secretly agrees, and I think one day someone will say it out loud and the whole campus will weep with relief."
            claudia "...That felt wonderful. Is it always like that? Having an opinion in public?"
        "\"You're not an empty chair. You're just careful. Those aren't the same.\"" (prompt="honest"):
            $ choose("claudia", 4, "honest")
            claudia "That's... a kind distinction, and I think it's also a true one, which is my favorite kind."
            claudia "I may write that down. I may write you a note about it. You've been warned."
        "\"So who's in three clubs under a pseudonym?\"" (prompt="pry"):
            $ choose("claudia", 0, "pry")
            claudia "Ah. You see? That's the question. It's always the question."
            claudia "I'm not cross. I'm just a little tired. Perhaps another day you'll ask me the other one."

    $ set_flag("claudia.opened_up")
    $ reveal("claudia", "likes")
    "(You learned what Claudia likes. Check your phone.)"

    hide claudia
    with dissolve
    return
