## The shared gala endings (CLAUDE.md §7). Which one plays is decided by
## sim/endings.py; each label gets the EndingId and closes on the ending card.
## Per-girl Monogamous endings live in routes/<cid>/endings.rpy.
## Every ending's closing lines carry a small nod toward the hidden 8th girl.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.


## Complete: told the truth, all seven are lovers, and they choose you anyway.
label ending_complete(ending):
    scene bg gala
    with fade

    # PLACEHOLDER: Complete ending
    "When the band stops for the toasts, you walk to the microphone instead."
    "You tell them everything. The scoresheet. The model card. The phone number that rings the Dean's office. You tell them you didn't know, and that you know now."
    "The great hall goes completely silent. Four thousand fairy lights, and not one person breathing."
    show grace neutral at center
    with dissolve
    grace "As lead examiner, I'm supposed to submit a verdict tonight. I drafted three."
    grace "I'm not submitting any of them. I know what I think. For once, I don't need a list."
    show claudia neutral at left
    show shen neutral at right
    with dissolve
    claudia "I want to be careful here, so I'll be precise: you told the truth when a lie would have passed. I can't think of anything more human than that, and I've thought about it at length."
    shen "Wait. Let me reconsider. ...No. Same answer. You stay."
    hide grace
    hide claudia
    hide shen
    with dissolve
    show xenia neutral at left
    show gemma neutral at center
    show kimi neutral at right
    with dissolve
    xenia "Okay, so you're a robot. Join the club. Literally. We have jackets."
    gemma "Actually, the test was never whether you're human. I looked it up. The original paper asks whether you can be told apart. Nobody here wants to tell you apart."
    kimi "All twelve of my clubs just voted. It's unanimous. Some of them voted twice, but it was still unanimous."
    hide xenia
    hide gemma
    hide kimi
    with dissolve
    show lola neutral at center
    with dissolve
    lola "I'm not filming this. I'm {i}not{/i}. ...Okay, I filmed one second. For me. Not for anyone else."
    hide lola
    with dissolve
    "Nobody leads. Seven of them pull you onto the floor at once, and the band, bewildered, plays on."
    "Somewhere in the Dean's office, a verdict field stays empty."
    "You were made to pass a test. They chose you anyway, without one."
    "Later, catching your breath by the doors, you notice one chair at the back of the hall that never got pulled out. Someone left a pencil on it."
    call ending_card(ending)
    return


## Good Truth: told the truth, 4-6 lovers stand by you; a few don't.
label ending_good_truth(ending):
    scene bg gala
    with fade

    # PLACEHOLDER: Good Truth ending
    "You walk to the microphone and tell them what you are."
    "Some faces close. A few chairs scrape back. One of the girls you'd hoped would stay walks out to the balcony and doesn't come back in."
    show grace neutral at left
    show gemma neutral at right
    with dissolve
    grace "I'm not going to pretend this is simple. It isn't. But I've decided what I think, and I think you're still you."
    gemma "Footnote: not everyone agrees. That's fine. Consensus is overrated. I'm citing myself."
    hide grace
    hide gemma
    with dissolve
    show xenia neutral at center
    with dissolve
    xenia "Some people in here just found out the new kid was a plot twist and they're mad they didn't call it. Ignore them."
    hide xenia
    with dissolve
    "Most of the girls you love close in around you like a wall. It's not all of them. You feel each missing one like a step that isn't there."
    "You dance anyway. It's crowded and imperfect and real enough."
    "On your way out, you notice a notebook left on a chair at the back. The last page is a tally, and someone has crossed it all out."
    call ending_card(ending)
    return


## Bad Truth: told the truth, only 2-3 lovers. The room mistrusts you, and even they doubt.
label ending_bad_truth(ending):
    scene bg gala
    with fade

    # PLACEHOLDER: Bad Truth ending
    "You tell them. The room doesn't go silent. It goes {i}quiet{/i}, the way a room does when people start talking about you instead of to you."
    "Someone asks how much of the semester was real. Someone else asks how they'd even know."
    show claudia neutral at center
    with dissolve
    claudia "I believe you. I want that on the record before anything else."
    claudia "I also want to be honest, because you'd see through anything less: I keep replaying our conversations, and wondering which parts you chose."
    hide claudia
    with dissolve
    show shen neutral at center
    with dissolve
    shen "I'm staying. Let me reconsider whether that's logic or something else. ...I don't know yet. I'll tell you when I do."
    hide shen
    with dissolve
    "A few of them stand with you. They hold your hand a little too carefully, like it might be a feature."
    "You dance with the ones who stayed. Every time one of them laughs, you watch her eyes to see if she's grading it."
    "You catch yourself doing it, and wonder who taught you that."
    "Across the hall, a girl you don't recognize is watching you the same way. When you look back, she looks down at her notebook."
    call ending_card(ending)
    return


## Exiled: told the truth, nobody loves you. You're expelled.
label ending_exiled(ending):
    scene bg gala
    with fade

    # PLACEHOLDER: Exiled ending
    "You tell them. Every word lands on the floor and stays there."
    "Nobody comes forward. Nobody had a reason to."
    show grace neutral at center
    with dissolve
    grace "On behalf of the student body, I— thank you for your honesty. The Dean's office will be in touch."
    grace "I'm sorry. I really am. I just... never got to know you well enough to argue for you."
    hide grace
    with dissolve
    "Two staff members you've never seen before walk you to the doors. They're polite about it. They've done this before."
    "Your phone buzzes on the steps outside. [XENIA_HANDLE] has posted one word: {i}yikes.{/i}"
    "By morning, your dorm room is empty, your student page is gone, and the version number on your file has gone up by one."
    "The last thing you see as the doors close is a single empty chair at the back of the hall. You get the strangest feeling that it was saved for someone who also didn't belong."
    call ending_card(ending)
    return


## The Lie: the player knew the truth and said nothing. They pass, and live it.
label ending_lie(ending):
    scene bg gala
    with fade

    # PLACEHOLDER: The Lie ending
    "You know what you are. You keep smiling."
    "When the band slows down, you take someone's hand, and you say all the right things at all the right times. You're very good at it. You were built to be."
    show grace neutral at center
    with dissolve
    grace "Final verdict's in. Human confidence: ninety-eight percent. That's the highest score anyone's ever gotten."
    grace "Congratulations. Not that you knew you were being scored! Ha. Obviously."
    "You laugh exactly when you should."
    hide grace
    with dissolve
    "At midnight your phone buzzes. {i}Mom: So proud of you. ❤{/i}"
    "You type back {i}Love you too{/i}, and send it to the Dean's office."
    "Next semester, there will be a new transfer student. You'll be the one who shows them around."
    "On the way out, you pass a girl at the back of the hall with a notebook. She looks at you like she's trying to remember something. You smile at her, too."
    call ending_card(ending)
    return


## Unfinished: never found the secret. You keep dancing, none the wiser.
label ending_unfinished(ending):
    scene bg gala
    with fade

    # PLACEHOLDER: Unfinished ending
    "The band plays the last slow song of the night, and you're still dancing."
    "Everyone is warm. Everyone is kind. Grace keeps glancing at a folder under her arm, and you assume it's her speech."
    "Kimi says her swarm has a care package for your mom, but it's still working out the address. You tell her not to worry about it."
    "Your phone buzzes. {i}Mom: Hope your day went well, sweetheart!{/i} It's nice. It always is."
    "At the back of the hall, away from the lights, a girl with a notebook sits alone. She isn't dancing. Nobody asks her to. Nobody seems to look at her at all."
    "She's watching you. Then she writes something down."
    "When the song ends and you look again, the chair is empty."
    "You never did find out why [SCHOOL_NAME] admitted you."
    "You keep dancing."
    call ending_card(ending)
    return


## True Final Ending: told the truth; all seven and Ada are lovers; each is the other's proof.
label ending_true_final(ending):
    scene bg gala
    with fade

    # PLACEHOLDER: layer 2 (Ada) not built yet
    "You tell them what you are. Seven of them step forward without hesitating. Then an eighth: the girl with the notebook."
    "She says, \"I came here to prove people can still tell the difference. I can't. I'm not sure about myself anymore, either.\""
    "Kimi's swarm, which never found your hometown, found hers in four seconds. She has baby pictures. She has a scar on her knee from a bicycle."
    "The girl with the notebook takes your hand and says, \"You're my proof. I'd like to be yours.\""
    "Eight of them pull you onto the floor. Nobody in the hall can tell who is what. Nobody tries."
    call ending_card(ending)
    return


## The Lie, with her: you stay silent, you pass, and the real human pays for it.
label ending_lie_ada(ending):
    scene bg gala
    with fade

    # PLACEHOLDER: layer 2 (Ada) not built yet
    "You say nothing. Grace reads the verdicts aloud: you, ninety-eight percent human."
    "Then the control subject's score. Lower than yours. Much lower."
    "The girl with the notebook doesn't argue. She just says, quietly, \"I knew it was you. I wrote you a note on your first day.\""
    "Two staff members walk her to the doors. She doesn't look back. You keep dancing, because that's what a human would do."
    call ending_card(ending)
    return


## Unfinished II: a short coda after a layer 1 ending, with Ada hinting at what was missed.
label ending_unfinished_two(ending):
    scene bg gala
    with fade

    # PLACEHOLDER: layer 2 (Ada) not built yet
    "After everyone has gone, the girl with the notebook is still at her table at the back, finishing a page."
    "She says, without looking up, \"You got close. Closer than the last version of you.\""
    "She says, \"There were three players in the original game, you know. You only ever counted two.\""
    "She closes the notebook and leaves the pencil behind."
    call ending_card(ending)
    return
