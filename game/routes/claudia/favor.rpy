## Claudia's favor (CLAUDE.md §6.3), offered at affection 50. Two steps:
##   0. Deliver one of her never-sent letters to Xenia in the cafeteria, unread.
##   1. Tell Claudia it's done, back in her library.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label claudia_favor_offer:
    show claudia neutral at center
    with dissolve

    # PLACEHOLDER
    "Claudia is holding a single envelope. It's cream, sealed with terracotta wax, and a little soft at the corners, as if it's been carried around for a long time."
    claudia "I'd like to ask you for something, and I want to be careful, because it matters to me more than I'm going to manage to sound like it does."
    claudia "This is one of my letters. The unsent kind. It's for Xenia. I've rewritten it nine times and carried it for three weeks, and I've decided that if I don't let someone else carry it, I never will."
    claudia "Would you give it to her? She's usually in the cafeteria in the afternoons, being rude to the fries."
    claudia "And, I'm so sorry to ask this, please don't read it. It isn't that I don't trust you. It's that it's hers, and I'd like her to be the first."

    menu:
        "\"Of course. It won't leave my hands until it's in hers.\"" (prompt="warm"):
            $ choose("claudia", 2, "warm")
            claudia "Thank you. I'd write you a thank-you note, but I suspect you'd find it alarmingly long."
        "\"I won't read it. You have my word.\"" (prompt="honest"):
            $ choose("claudia", 3, "honest")
            claudia "I believe you. That's a lovely thing to be able to say. I don't get to say it very often."
        "\"Is it a love letter?\"" (prompt="pry"):
            $ choose("claudia", 0, "pry")
            claudia "It's not. That's all I'll say, and I'm sorry it's all I'll say. Perhaps that's part of why I asked you not to read it."

    $ gs = sim_fav.offer(gs, "claudia")
    "(Favor accepted: deliver Claudia's letter to Xenia in the cafeteria one afternoon, unread, then tell Claudia it's done. You have [RULES.favor_deadline_days] days.)"

    hide claudia
    with dissolve
    return


label claudia_favor_deliver:
    scene bg cafeteria
    "The cafeteria, mid-afternoon. Xenia is alone at a corner table, eating fries one at a time and typing on her phone with alarming speed."
    "Claudia's envelope is in your pocket. The wax seal is cracked a little at one edge. It would be very easy to look."

    menu:
        "Open it and read it first.":
            $ set_flag("claudia.read_letter")
            "You slip the letter out. Claudia's handwriting is beautiful, and the letter is short. For her, it's practically a telegram."
            # PLACEHOLDER: the letter's contents (only seen by players who read it)
            "{i}Dear Xenia, I want to be careful here, so I'll say it plainly instead. I know you run @x_unfiltered. I've known since the post about the soup.{/i}"
            "{i}I'm not going to tell anyone. It isn't mine to tell. I only wanted you to know that someone knows, and that it hasn't changed what she thinks of you, which is that you're much kinder than you let anyone see. Yours, with apologies for the length, Claudia.{/i}"
            "You fold it back along its creases. It doesn't quite sit the way it did before."
        "Leave it sealed.":
            "You leave it sealed. It isn't yours."

    show xenia neutral at center
    with dissolve

    # PLACEHOLDER
    xenia "Oh, it's the human. If you're here to recruit me for one of Grace's nine clubs, I'm already busy. With fries."
    "You hand her the envelope."
    xenia "Wax seal. Cream paper. Handwriting like a Victorian ghost. This is from Claudia. Nobody else on Earth still owns wax."
    "She opens it, rolling her eyes. Then she stops rolling them. She reads it twice. The fries go cold."
    xenia "..."
    xenia "Okay. Cool. Cool cool cool. Did she say anything else? Is she going to— no. She wrote she's not. She wouldn't write it if she didn't mean it. She's physically incapable."
    xenia "That's so annoying. I spent three weeks thinking nobody knew, and it turns out the one person who did just sat on it. Politely. Like a hen."
    "Xenia folds the letter very small and puts it in the inside pocket of her jacket, the one closest to her heart, then glares at you as if you'd pointed this out."
    xenia "Tell her... tell her thanks. No. Don't tell her thanks. Tell her it was too long. She'll know what it means."

    $ gs = sim_fav.advance_step(gs, "claudia", CAST["claudia"]["favor"]["steps"])
    "(Now let Claudia know it's delivered.)"

    hide xenia
    with dissolve
    return


label claudia_favor_report:
    show claudia neutral at center
    with dissolve

    # PLACEHOLDER
    claudia "You're back. Did she— no, I'll let you tell it. I've been rehearsing my calm face. How is it? Be honest. It's terrible, isn't it."
    "You tell her the letter is delivered. You pass on Xenia's message: it was too long."
    claudia "Oh. Oh, that's wonderful. That's the nicest thing she's ever said to anyone."

    if has_flag("claudia.read_letter"):
        "Claudia looks at you for a long, quiet moment. Not unkindly. Just accurately."
        claudia "You read it, didn't you."
        claudia "Please don't apologize, or explain. I could tell from the way you said her name. You said it like someone who knows something about her now."
        claudia "I'm not angry. I'm a little sad, and I think I'm allowed to be. I asked for one small thing, and it was the thing I most needed."
        claudia "But you delivered it, and you were honest with your face, if not your hands. I'll take that. And I'd ask you to keep what you read the way I've kept it."
        $ bump("claudia", -5, "read_letter")
        claudia "Thank you, still. I mean that. I've had it in my pocket for three weeks, and now it's in hers."
    else:
        claudia "And you didn't read it. I can tell. You'd look at me differently if you had, and you're looking at me exactly the same."
        claudia "Thank you. Truly. It's a strange relief, letting one of them go. I'd been carrying that letter around like a stone in my shoe, a very elegantly addressed stone."
        claudia "I think I might let another one out someday. I'm not sure who to. I have a feeling I'll know."

    $ gs = sim_fav.advance_step(gs, "claudia", CAST["claudia"]["favor"]["steps"])
    $ bump("claudia", sim_aff.scale_gain(10, CAST["claudia"]["difficulty"]), "favor_done")
    $ grant("first_favor")
    call minor_clue("claudia", "earned")
    claudia "I'm going to write you a thank-you note now. I'm sorry in advance. It's going to have a postscript."

    hide claudia
    with dissolve
    return
