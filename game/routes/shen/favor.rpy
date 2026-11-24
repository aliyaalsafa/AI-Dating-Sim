## Shen's favor (CLAUDE.md §6.3), offered at affection 50. Three steps:
##   0. Ask Claudia, in her suite's library, where the copying rumor came from.
##   1. Check the campus wiki's edit history with Gemma in the robotics lab.
##   2. Report back to Shen at the library.
## The truth: Gemma's wiki auto-merged Shen's freely shared notes into Grace's
## study-guide page and credited Grace. Nobody did anything malicious.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label shen_favor_offer:
    show shen neutral at center
    with dissolve

    # PLACEHOLDER
    shen "I need a favor. I'll be brief."
    shen "People say I copied Grace's notes. I didn't. I want to know where that started."
    shen "Wait. Let me reconsider. I don't want revenge. I want the facts. Fairly. No sneaking into anyone's email. No rumors to fight rumors."
    shen "I'd do it myself, but if I ask, it looks like I'm guilty. You're neutral. Mostly."

    menu:
        "\"I'll find out. Fairly.\"" (prompt="concise"):
            $ choose("shen", 3, "concise")
            shen "Good. Four words. Thank you."
        "\"And if it turns out to be Grace?\"" (prompt="honest"):
            $ choose("shen", 2, "honest")
            shen "Then it's Grace. I'd still want to know."
            shen "...I don't think it's Grace. She's annoying, but she's not that kind of annoying."

    $ gs = sim_fav.offer(gs, "shen")
    "(Favor accepted: find out where the rumor came from. Start by asking Claudia in her suite's library. You have [RULES.favor_deadline_days] days.)"

    hide shen
    with dissolve
    return


label shen_favor_claudia:
    show claudia neutral at center
    with dissolve

    # PLACEHOLDER
    "Claudia's private library smells like old paper and very expensive tea. She sets down a fountain pen when you come in."
    claudia "Oh, how lovely, please do sit; I was only writing a thank-you note to my sister for a thank-you note she wrote me, which I realize is a loop, and I apologize for it."
    "You explain what Shen asked you to find out."
    claudia "Ah. The rumor. I want to be careful here, but I think it matters that you're asking where it came from rather than whether it's true, because those are two very different questions."

    menu:
        "\"Come on, you know everything. Who started it?\"" (prompt="pry"):
            $ choose("claudia", -1, "pry")
            claudia "I'm so sorry, but I don't think I'll answer that, and I'd gently suggest that the way you asked it is rather how rumors begin in the first place."
            claudia "That said, I wouldn't want Shen to suffer for my scruples, so: wikis keep records. Edit histories. They're very dull, and dull things are usually honest."
        "\"I want to do this fairly. Where should I look?\"" (prompt="honest"):
            $ choose("claudia", 3, "honest")
            claudia "Thank you for putting it that way; it makes this so much easier, and I'm sorry it was ever hard."
            claudia "I won't tell you who said what, because I genuinely don't think anyone set out to say anything. But I'd look at the campus wiki. Specifically, the edit history of Grace's study guide."
            claudia "Something there has always struck me as a little odd. The handwriting, so to speak, changes halfway down the page."

    claudia "Gemma runs the wiki. Do be kind to her; she cares about accuracy more than almost anyone I know, and I suspect this will sting."
    "She hands you a small card in elegant ink. It says: {i}Good luck. Be fair. C.{/i}"

    $ gs = sim_fav.advance_step(gs, "shen", CAST["shen"]["favor"]["steps"])
    "(Next: ask Gemma about the wiki in the robotics lab.)"

    hide claudia
    with dissolve
    return


label shen_favor_wiki:
    show gemma neutral at center
    with dissolve

    # PLACEHOLDER
    "Gemma is labeling a drawer of screws with her label maker. The labels are red, yellow, green and blue, in rotation."
    gemma "Oh! Hi! The wiki? Love the wiki. Actually, it's not 'the' wiki, it's version four. Versions one through three are on the shelf. Don't look at the shelf."
    "You ask about the edit history of Grace's study guide."
    gemma "Easy. Let me look that up. I mean, I already know it, but let me look it up, for sourcing."
    "She pulls it up on a monitor, then raises her phone and takes a picture of the monitor, for some reason."
    gemma "Okay, so in week two the auto-merge bot found two pages with the same topic headings and combined them. Grace's study guide and— oh."
    gemma "Shen's shared notes. It merged Shen's notes into Grace's page. And it credited the whole page to Grace, because her page was older."
    gemma "So everyone saw 'Grace's notes' written in Shen's style. Three steps per problem, no wasted words. And then they saw Shen's notes and assumed she'd copied."
    gemma "It was the other way round. Actually, it wasn't anyone's way round. It was my bot. I wrote the bot. I was going to finish the conflict-check feature. I didn't finish the conflict-check feature."
    gemma "Oh no. Oh no, oh no. Source: me. I'm the source."

    menu:
        "\"Nobody meant any harm. Let's fix it together.\"" (prompt="warm"):
            $ choose("gemma", 3, "warm")
            gemma "Together. Okay. Yes. I can do that. I can restore the revisions and fix the attribution in, actually, about four minutes."
            gemma "Thank you for not yelling. I would have yelled at me. I'd have cited myself, too."
        "\"Your bot wrecked Shen's reputation for weeks.\"" (prompt="honest"):
            $ choose("gemma", -2, "honest")
            gemma "I know. I know. You're right. Sorry, I'm going to go stare at the shelf of dead prototypes for a minute."
            gemma "...I'll fix it. I'll actually finish something. Starting with this."

    gemma "Here. I screenshotted the whole edit history, with timestamps. Color-coded. Show Shen. She'll want the primary source."

    $ gs = sim_fav.advance_step(gs, "shen", CAST["shen"]["favor"]["steps"])
    "(Now tell Shen what you found.)"

    hide gemma
    with dissolve
    return


label shen_favor_report:
    show shen neutral at center
    with dissolve

    # PLACEHOLDER
    "You show Shen the screenshots. She reads every timestamp. Twice."
    shen "An auto-merge bot. Older page wins attribution. Mine got folded into hers."
    shen "Wait. Let me reconsider. So Grace didn't copy me either. Nobody copied anybody. A script did a merge."
    shen "That's almost elegant. I hate that it's almost elegant."
    shen "Okay. How do I correct it? I want it fixed. I don't want it to look like I'm attacking Grace or Gemma."

    menu:
        "\"Post the edit history. Let the facts speak.\"" (prompt="concise"):
            $ choose("shen", 3, "concise")
            shen "Primary source. No commentary. Yes. People can check it themselves."
            shen "That's the fair way. It's also the short way. My favorite kind."
        "\"Ask Gemma to fix the credit, and tell Grace first.\"" (prompt="practical"):
            $ choose("shen", 4, "practical")
            shen "Tell Grace first. Hm. She'd hate finding out from a post. I would too."
            shen "...Fine. I'll tell her. She'll probably say 'great' four times. I'll count."

    "By evening, the wiki page has two names on it, and the edit summary just says {i}fixed attribution, sorry, G.{/i}"

    $ gs = sim_fav.advance_step(gs, "shen", CAST["shen"]["favor"]["steps"])
    $ bump("shen", sim_aff.scale_gain(10, CAST["shen"]["difficulty"]), "favor_done")
    $ grant("first_favor")
    call minor_clue("shen", "earned")
    shen "You did that fairly. No shortcuts. I noticed."
    shen "Thank you. That's the whole sentence. It doesn't need more."

    hide shen
    with dissolve
    return
