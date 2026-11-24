## Gemma: repeatable hangout in the robotics lab (once per day).
## Rotates through four conversation topics. Her route rewards curiosity and
## nerding out with her; it punishes dismissing her interests or calling her "Bard".
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label gemma_hangout:
    show gemma placeholder at center
    with dissolve

    if gs.inventory:
        menu:
            gemma "Oh! [player_name]! Hold still, the lighting's good. Okay. Hi. What's up?"
            "Just talk.":
                pass
            "Give her a gift.":
                call give_gift_flow("gemma")
                hide gemma
                with dissolve
                return

    $ topic = sim_state.count(gs, "gemma.hangouts") % 4
    $ gs = sim_state.incr(gs, "gemma.hangouts")

    if topic == 0:
        call gemma_topic_new_project
    elif topic == 1:
        call gemma_topic_wiki
    elif topic == 2:
        call gemma_topic_labels
    else:
        call gemma_topic_freshman

    hide gemma
    with dissolve
    return


label gemma_topic_new_project:
    # PLACEHOLDER
    gemma "Okay, okay, okay. New project. A robot that waters the plants in the lab. It reads soil moisture, it texts the plant's owner, it has a little face."
    gemma "Actually, the lab only has one plant. And it's plastic. But the {i}principle{/i} is sound."

    menu:
        "\"How does it read the moisture? Show me the sensor.\"" (prompt="curious"):
            $ choose("gemma", 5, "curious")
            gemma "You want to see the sensor? Nobody wants to see the sensor!"
            "She shows you the sensor. Then the wiring diagram. Then a second wiring diagram that contradicts the first one, which she defends with total confidence."
            gemma "Both are correct. Depending on the day."
        "\"Cool. What are the milestones?\"" (prompt="structured"):
            $ choose("gemma", 3, "structured")
            gemma "Milestones! Yes. Red for hardware, yellow for software, green for testing, blue for... finishing."
            gemma "Blue's always empty. I don't know why. It's a very nice blue."
        "\"Didn't you start a different robot last week?\"" (prompt="pry"):
            $ choose("gemma", 1, "pry")
            gemma "That one's... resting. On the shelf. It's fine. Let me look that up — no, I know. It's fine."
    return


label gemma_topic_wiki:
    # PLACEHOLDER
    gemma "So I just fixed Grace's wiki page again. She said the library has four floors. It has three and a mezzanine. Source: the building."
    gemma "I put the citation in. Footnote forty-one. She's going to love it. Actually, she's going to say she loves it, which is different."

    menu:
        "\"Why do you care so much about getting it right?\"" (prompt="curious"):
            $ choose("gemma", 4, "curious")
            gemma "Because if it's written down, it should be true. Otherwise what's the point of writing it down?"
            gemma "...Also I hate being wrong in public. Footnote forty-two."
        "\"You could just tell her in person.\"" (prompt="honest"):
            $ choose("gemma", 2, "honest")
            gemma "In person? With my face? Huh. That's... an interface I haven't tested much."
        "\"Who reads the campus wiki, anyway?\"" (prompt="irreverent"):
            $ choose("gemma", 0, "irreverent")
            gemma "Eleven hundred people a week. Actually, eleven hundred and four. I check. Every day."
            gemma "Oh. You were dismissing it. Okay. Noted."
    return


label gemma_topic_labels:
    # PLACEHOLDER
    "Gemma's label maker clicks like a tiny typewriter. Every drawer in the lab has a label. Some labels have labels."
    gemma "Red is dangerous, yellow is fragile, green is safe, blue is mine. Hold out your hand."
    "She sticks a label on your sleeve. It says {i}BLUE.{/i}"

    menu:
        "\"Teach me the system. All of it.\"" (prompt="structured"):
            $ choose("gemma", 4, "structured")
            gemma "All of it? Okay, sit down, this takes forty minutes. Thirty-five if you don't ask about the purple exception."
            gemma "There's no purple exception. Actually, there is. We'll get there."
        "\"I'm keeping this label forever.\"" (prompt="warm"):
            $ choose("gemma", 3, "warm")
            gemma "You— really? It's just tape. With letters on it."
            "She takes a photo of the label on your sleeve. For the wiki. For science. Probably."
        "\"Why blue for you?\"" (prompt="concise"):
            $ choose("gemma", 2, "concise")
            gemma "Blue's the last color. In my system. It's for things I'm keeping. Most things don't make it to blue."
    return


label gemma_topic_freshman:
    # PLACEHOLDER
    gemma "Shen and I recalibrated the arm this morning. She didn't say a single word for two hours. It was perfect. Best lab session of the semester."
    gemma "Freshman year I had a lab partner who wanted to talk about weekends. I didn't know what to say. I still don't, really."

    menu:
        "\"What were you like freshman year?\"" (prompt="curious"):
            $ choose("gemma", 3, "curious")
            gemma "Louder. Wronger. I said a lot of things very confidently. Some of them were true!"
            gemma "I'm better now. I check things first. Mostly. Let me look that up."
        "\"I don't do small talk either. Want to just work?\"" (prompt="practical"):
            $ choose("gemma", 3, "practical")
            gemma "Oh thank goodness. Yes. Hand me the hex key. The blue one."
            "You work in comfortable silence. It's nice. She seems to think so too."
        "\"Weren't you called 'Bard' back then?\"":
            $ hit_dealbreaker("gemma")
            gemma "...Where did you hear that?"
            gemma "Actually, don't tell me. I don't want to know. I've been trying very hard for a year to not be that person."
            "She picks her phone up and very deliberately doesn't take your picture."
    return
