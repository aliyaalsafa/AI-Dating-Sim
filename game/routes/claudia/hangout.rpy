## Claudia: repeatable hangout on the quad or in her suite's private library
## (once per day). Rotates through four conversation topics. Her route rewards
## honesty, patience and asking what she thinks; it punishes fishing for gossip
## and trying to trick secrets out of her.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label claudia_hangout:
    show claudia neutral at center
    with dissolve

    claudia "Hello, [player_name]. I'm so glad you came by. I'd ask how you are, but I'd like to hear the long version, with error bars, if you have the time."

    $ topic = sim_state.count(gs, "claudia.hangouts") % 4
    $ gs = sim_state.incr(gs, "claudia.hangouts")

    if topic == 0:
        call claudia_topic_notes
    elif topic == 1:
        call claudia_topic_secrets
    elif topic == 2:
        call claudia_topic_opinions
    else:
        call claudia_topic_sisters

    hide claudia
    with dissolve
    return


label claudia_topic_notes:
    # PLACEHOLDER
    "Claudia is writing on cream-colored card stock with a fountain pen. Beside her is a small stack of sealed envelopes and an open spreadsheet titled {i}Marginal Utility of Gratitude, Fall Term{/i}."
    claudia "Oh, forgive me. These are thank-you notes, for the people who held the door this week. There were eleven of them, and one held it twice, so she gets a postscript."
    claudia "There's a rather lovely body of research suggesting that a handwritten thank-you raises the recipient's mood far more than the sender predicts. People systematically underestimate it. So, by my rough estimate, this is the most good I can do per minute before lunch."
    claudia "I'm sorry, is that strange? I've been told it's strange. I apologize. And now I'm apologizing for apologizing, which I'm told is also strange."

    menu:
        "\"It's not strange. It's lovely.\"" (prompt="warm"):
            $ choose("claudia", 3, "warm")
            claudia "That's very kind. I'm going to pretend I'm not writing that down, but I am, in my head, in ink, with a confidence interval of essentially zero width."
        "\"Do you ever write one you don't send?\"" (prompt="curious"):
            $ choose("claudia", 4, "curious")
            claudia "...That's a perceptive question, and I want to answer it honestly, which means the answer is yes. Rather a lot of them."
            claudia "I keep them in a notebook. The sent ones say what's polite. The unsent ones say what I actually think. It's a sort of control group for my own courage."
            claudia "Perhaps one day I'll let one out. Like a bird. A very well-punctuated, carefully peer-reviewed bird."
        "\"Honestly? A text would be faster.\"" (prompt="concise"):
            $ choose("claudia", 1, "concise")
            claudia "It would. You're quite right. And faster is often better; I'd never argue against efficiency, I'd be drummed out of my own reading group."
            claudia "But nobody keeps a text in a shoebox for thirty years. Over a long enough horizon, I think the note wins. I'd like to be kept in a shoebox. Metaphorically."
        "\"Who's the one who held it twice?\"" (prompt="pry"):
            $ choose("claudia", 1, "pry")
            claudia "Ah. I'll tell you she was carrying a cello at the time, which raises the expected heroism considerably. The rest is hers."
    return


label claudia_topic_secrets:
    # PLACEHOLDER
    claudia "I want to be careful here, but I think you should know something, and I'd like to explain my reasoning before I say it, if that's all right. Benefit to you: moderate. Harm to anyone else: negligible. I've checked."
    claudia "The vending machine on the second floor gives two snacks if you press B4 twice. I'm telling you because you skipped lunch yesterday, and I worry. That's all. That's the whole secret."

    menu:
        "\"You did a cost-benefit analysis for a vending machine.\"" (prompt="irreverent"):
            $ choose("claudia", 2, "irreverent")
            claudia "I do a cost-benefit analysis for everything. I once wrote a footnote on a birthday card. It cited a meta-analysis."
            claudia "...You're laughing. Good. I hoped you would. I don't always know if I'm allowed to be funny."
        "\"How do you decide what's yours to tell?\"" (prompt="honest"):
            $ choose("claudia", 5, "honest")
            claudia "Oh. Nobody has ever asked me that. They usually ask what I know."
            claudia "I run three tests. Would it help the person hearing it? Would it hurt the person it's about? And would I be comfortable if they knew I'd said it?"
            claudia "If the answers are yes, no, and yes, I tell. If I'm uncertain, I assume the downside is worse than I think, because it usually is. Then I bake something and wait. I bake a great deal."
        "\"Thanks. That's genuinely useful.\"" (prompt="practical"):
            $ choose("claudia", 2, "practical")
            claudia "I'm so pleased. Press it twice, gently. It's an old machine, and while I'd only put perhaps fifteen percent on it having feelings, the cost of being kind to it is very low."
        "Casually mention that Grace already told you what scares her, and wait for Claudia to fill in the rest.":
            $ hit_dealbreaker("claudia")
            claudia "Did she."
            "Claudia sets her pen down very precisely."
            claudia "I don't think she did. I think you're hoping I'll confirm something by assuming you already know it. It's a rather old trick; there's a whole literature on it. I'm sorry. I've simply seen it before."
            claudia "I'd have liked it better if you'd just asked me. I would have said no, but kindly, and we'd still be talking."
    return


label claudia_topic_opinions:
    # PLACEHOLDER
    claudia "Someone wrote on @x_unfiltered that I don't have opinions, only \"vibes, footnotes, and a trust fund I give away to mosquito nets.\" Which is unkind, and roughly three-quarters accurate."
    claudia "I do have opinions. I just stress-test them so many times before I say them that they get worn smooth. Like sea glass. Or a very thoroughly replicated study."

    menu:
        "\"So tell me one. Right now. No hedging.\"" (prompt="honest"):
            $ choose("claudia", 4, "honest")
            claudia "Right now. No confidence interval. Goodness. All right."
            claudia "Ducks are the most underrated animal on this campus. They are dignified on land, competent on water, and absolutely unhinged in the air."
            claudia "...I have about forty more of those. Most of them are about ducks. I've never told anyone that. I didn't even caveat it. How thrilling."
        "\"What do you actually think about it?\"" (prompt="curious"):
            $ choose("claudia", 4, "curious")
            claudia "About the post? I think it stung, and I'd put maybe seventy percent on whoever wrote it being lonelier than they let on."
            claudia "And I think I'd still rather be careful than cruel. Carefulness compounds. Even if careful looks like nothing from far away."
        "\"Here's the plan: you post one hot take a day.\"" (prompt="structured"):
            $ choose("claudia", 2, "structured")
            claudia "A schedule for boldness. Grace would adore this; she'd want to ship it tonight. I'd want to pilot it first with a small sample, draft each take for a week, and post it on the following Tuesday, at which point it would be lukewarm."
        "\"Who do you think wrote it?\"" (prompt="pry"):
            $ choose("claudia", 0, "pry")
            claudia "I have a guess. A fairly confident one, actually. I'm still deciding whether it's mine to say. Until I've decided, I'm afraid the answer is a very warm silence."
    return


label claudia_topic_sisters:
    # PLACEHOLDER
    "Claudia's phone buzzes four times in a row. She reads the messages with the expression of someone being lovingly attacked."
    claudia "My sisters. Sonnet is asking if she can borrow my camel coat. Haiku has sent a poem about the coat. It's three lines and I'm told it's a threat."
    claudia "They're younger. Sonnet does everything quickly and Haiku does everything in seventeen syllables. I do everything in seventeen paragraphs with a methods section. Mother says we balance out."

    menu:
        "\"What are you like when it's just the three of you?\"" (prompt="curious"):
            $ choose("claudia", 5, "curious")
            claudia "Oh. Hm. Honestly? Much sillier. We have a running bit where we narrate the ducks on the estate pond like a nature documentary."
            claudia "There's one called Reginald. He has a tragic backstory. I wrote it. It's eleven pages, and it includes a population study of the pond, because I couldn't help myself."
            claudia "I don't know why I told you that. I'm glad I did."
        "\"They sound wonderful.\"" (prompt="warm"):
            $ choose("claudia", 3, "warm")
            claudia "They are. They're also a menace. I'd defend them to the death and then write them both a strongly worded note. With citations."
        "\"Just say no about the coat.\"" (prompt="concise"):
            $ choose("claudia", 0, "concise")
            claudia "Just... no? With nothing after it? No reasoning, no alternatives considered? I'm not sure I know how. I'd want to explain, and offer a scarf, and apologize for the scarf."
    return
