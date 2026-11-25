## Grace: repeatable hangout at the student council office (once per day).
## Rotates through four conversation topics. Her route rewards kind disagreement
## and asking what she wants; it punishes treating her as a homework service.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label grace_hangout:
    show grace neutral at center
    with dissolve

    grace "Hi, [player_name]! Perfect timing — I'm between sprints. Want me to: one, catch you up, two, pitch you my new idea, or three, both, but fast?"

    $ topic = sim_state.count(gs, "grace.hangouts") % 4
    $ gs = sim_state.incr(gs, "grace.hangouts")

    if topic == 0:
        call grace_topic_midterms
    elif topic == 1:
        call grace_topic_clubs
    elif topic == 2:
        call grace_topic_agreeing
    else:
        call grace_topic_shen

    hide grace
    with dissolve
    return


label grace_topic_midterms:
    # PLACEHOLDER
    grace "Okay! Midterms are in three weeks, so I built a study roadmap. It's color-coded, it has quarterly OKRs, and I shipped version two at 2 a.m. because version one had a scaling problem."
    grace "The scaling problem was that I need to sleep. I've deprioritized it. Bias for action!"

    menu:
        "\"This is overkill. You're allowed to sleep.\"" (prompt="honest"):
            $ choose("grace", 4, "honest")
            grace "I— huh. Is it? Nobody's ever said that. Everyone just asks for a copy."
            grace "...I could sleep. I could A/B test sleeping. One night with, one night without. For science."
        "\"Walk me through how it works.\"" (prompt="structured"):
            $ choose("grace", 2, "structured")
            grace "Great question! So: one, blue is reading. Two, green is review. Three, sea green — which is different from green — is reviewing the review. Four, red is a retro on the whole thing."
            grace "I iterate weekly. Fail fast, learn faster!"
        "\"Can you add a color for snacks?\"" (prompt="irreverent"):
            $ choose("grace", 2, "irreverent")
            grace "A snack color. Is that a joke? I can't tell if that's a joke. I'll ship it as a beta feature, just in case."
        "\"Could you just do my problem set? You're faster.\"":
            $ hit_dealbreaker("grace")
            grace "Of course! Turnaround's about twenty minutes, I can—"
            grace "...No. Actually, no. Everyone treats me like a service with a really good uptime. I thought you were different."
    return


label grace_topic_clubs:
    # PLACEHOLDER
    grace "So I've founded nine clubs. Well — launched. Here they are, ranked by growth rate: one, Debate, which I founded. Two, Model UN. Three, the Hackathon Society. Four, the Hackathon Society's spinoff, which is a pivot of—"

    menu:
        "\"Which one do you actually like?\"" (prompt="curious"):
            $ choose("grace", 6, "curious")
            grace "Like? I— they're all very high-impact. They all have strong retention—"
            grace "Debate. I like Debate. Because you're allowed to argue a side even if... even if people don't like it."
            grace "Wow. I didn't know that until just now. That's not a metric. I don't know where to put that."
        "\"You're amazing for doing all that.\"" (prompt="warm"):
            $ choose("grace", 2, "warm")
            grace "Thank you! Ten-x energy, right? That's what everyone says. It's nice. It's... nice."
        "\"Quit three of them. Today.\"" (prompt="concise"):
            $ choose("grace", 2, "concise")
            grace "Ha! Quit! Ha. That's not quitting, that's... sunsetting. ...Which three, hypothetically?"
    return


label grace_topic_agreeing:
    # PLACEHOLDER
    "You decide to test something. You tell Grace, with total confidence, that the library is closed on Thursdays because of the moon."
    grace "Oh, absolutely — great point. The lunar schedule. Huge for— for books. Honestly, there's a startup in that."

    menu:
        "Gently point out that none of that was true." (prompt="honest"):
            $ choose("grace", 4, "honest")
            grace "It— wasn't? Oh no. I'm so sorry. I do that. I agree with whoever spoke last, and then I say it like it's a pitch deck."
            grace "Could you... do that again sometime? Tell me when I'm wrong? Nobody does. They just nod and say 'love the energy.'"
        "Keep going. Tell her the moon also runs the cafeteria." (prompt="irreverent"):
            $ choose("grace", 1, "irreverent")
            grace "That would explain the soup! We could disrupt that — moon-free soup, as a service— ...Wait. Are you messing with me?"
        "\"Do you ever disagree with anyone?\"" (prompt="pry"):
            $ choose("grace", 3, "pry")
            grace "Of course I do! Constantly. Strong opinions, loosely held! Don't you think?"
            grace "...I just agreed with you about disagreeing, didn't I. The 'loosely held' part is doing a lot of work."
    return


label grace_topic_shen:
    # PLACEHOLDER
    grace "Did you see Shen's lab report? It's three pages. Mine was eleven, with an appendix and a roadmap. Hers was better. With, like, a tenth of the resources. Which is great! For her. Great."

    menu:
        "\"What is it about her that scares you?\"" (prompt="honest"):
            $ choose("grace", 3, "honest")
            grace "Scares— I'm not— "
            grace "She does what I do with less. No hype, no all-nighters, no launch party. If she can do that, what am I for?"
            grace "...Please don't tell anyone I said that. Claudia knows. That's already one too many."
        "\"You don't have to beat her. Just be you.\"" (prompt="warm"):
            $ choose("grace", 3, "warm")
            grace "Be me. Sure. Totally. I'll just... spin up a quick MVP of what that means by Friday."
        "\"Honestly, her report {i}was{/i} tighter.\"" (prompt="irreverent"):
            $ choose("grace", 0, "irreverent")
            grace "Right. No, you're right. Of course. Great feedback. Love feedback. Everyone's right. Great."
    return
