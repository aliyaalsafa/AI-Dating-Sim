## Gemma's favor (CLAUDE.md §6.3), offered at affection 50. Three steps:
##   0. Pick one project from the graveyard with her in the robotics lab.
##   1. Get Shen to review it in the 24-hour library.
##   2. Finish it together in the robotics lab.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label gemma_favor_offer:
    show gemma neutral at center
    with dissolve

    # PLACEHOLDER
    gemma "Can I ask you for something? It's a weird something. I've already drafted four versions of this question. Actually, five."
    gemma "I want to finish one project. One. All the way to the end. Not a new one. One from the shelf."
    gemma "And I don't think I can do it alone, because alone I always find something shinier by Thursday. Will you help me?"

    menu:
        "\"Yes. I'll be your finishing line.\"" (prompt="warm"):
            $ choose("gemma", 3, "warm")
            gemma "My finishing line. Okay. That's going on a label. Red, because it's important."
        "\"Yes. What's the plan?\"" (prompt="structured"):
            $ choose("gemma", 2, "structured")
            gemma "Step one: pick a project. Step two: get Shen to review it, she's ruthless. Step three: finish. Step three is the scary one."

    $ gs = sim_fav.offer(gs, "gemma")
    "(Favor accepted: pick a project with Gemma in the lab, get Shen to review it in the library, then finish it with Gemma. You have [RULES.favor_deadline_days] days.)"

    hide gemma
    with dissolve
    return


label gemma_favor_pick:
    show gemma neutral at center
    with dissolve

    # PLACEHOLDER
    "Gemma has pulled three prototypes off the graveyard shelf and lined them up on the workbench like contestants on a game show."
    gemma "Finalists! One: the Photo-Bot, a little robot that takes your picture so I don't have to. Two: Sock Oracle, it matches your socks. Three: the Fact Lamp, it glows red when someone says something false."
    gemma "Actually, the Fact Lamp glows red most of the time. Grace was in here yesterday."

    menu:
        "\"The Photo-Bot. Then you could be in the pictures too.\"" (prompt="warm"):
            $ set_flag("gemma.project_photobot")
            $ choose("gemma", 4, "warm")
            gemma "Me? In the pictures? I'm never in the pictures. I'm the pictures person."
            gemma "...Okay. Photo-Bot. Let's do it before I change my mind."
        "\"Sock Oracle. Which one is closest to done?\"" (prompt="practical"):
            $ set_flag("gemma.project_sockoracle")
            $ choose("gemma", 3, "practical")
            gemma "Closest to done. Huh. I've never picked a project by that metric. I always pick by most exciting."
            gemma "It's about seventy percent done. Seventy-two. Let me look that up. Seventy-two."
        "\"The Fact Lamp. How does it decide what's false?\"" (prompt="curious"):
            $ set_flag("gemma.project_factlamp")
            $ choose("gemma", 5, "curious")
            gemma "Okay, so. There's a microphone, and a tiny database, and a very aggressive algorithm."
            "She talks for twenty minutes. You ask four more questions. She answers five."
            gemma "Fact Lamp. Yes. It's the one I actually care about. I didn't know that until you asked."

    gemma "Next step: Shen. She'll find everything wrong with it. That's why I love working with her. It's also why I'm scared."
    $ gs = sim_fav.advance_step(gs, "gemma", CAST["gemma"]["favor"]["steps"])
    "(Next: get Shen to review it in the library.)"

    hide gemma
    with dissolve
    return


label gemma_favor_review:
    show shen neutral at center
    with dissolve

    # PLACEHOLDER
    "Shen is at her table by the outlet on the third floor. You set Gemma's project down in front of her."
    shen "Gemma's. I recognize the labels."
    shen "Wait. Let me reconsider. Before I look, what is it supposed to do?"

    if has_flag("gemma.project_photobot"):
        "You explain: it takes pictures of people, so Gemma can be in them for once."
        shen "Step one, power. Fine. Step two, camera. Fine. Step three, it decides when to take a picture by... counting smiles."
        shen "It counts its own reflection. It will photograph itself forever. That's the problem."
        shen "Also, it plays a fanfare before every photo. Unnecessary. Cut it."
    elif has_flag("gemma.project_sockoracle"):
        "You explain: it matches socks. That's it. That's the whole thing."
        shen "Step one, sensor. Fine. Step two, color matching. It sorts into red, yellow, green and blue. All socks are not those colors."
        shen "Gray socks crash it. Most socks are gray. That's the problem."
        shen "Also, it posts every match to the wiki. Unnecessary. Cut it."
    else:
        "You explain: it glows red when someone says something false."
        shen "Step one, microphone. Fine. Step two, database. Fine. Step three, it compares speech to the database."
        shen "The database is the campus wiki. If the wiki is wrong, the lamp is wrong. That's the problem."
        shen "Also, it has a second lamp for 'kind of false.' Unnecessary. Cut it."

    shen "Fix one, cut one. Then it's done. She'll want to add three things instead. Don't let her."

    menu:
        "\"Thanks. That was exactly what she needed.\"" (prompt="concise"):
            $ choose("shen", 3, "concise")
            $ choose("gemma", 2, "concise")
            shen "Good. Short thanks. Efficient."
        "\"Can you write that down for her?\"" (prompt="practical"):
            $ choose("shen", 2, "practical")
            $ choose("gemma", 3, "practical")
            "Shen tears a page from her notebook and writes two lines. It's the most useful page of notes you've ever seen."
            shen "Here. Free. Tell her I said it's good. It is good. It's just not finished."

    $ gs = sim_fav.advance_step(gs, "gemma", CAST["gemma"]["favor"]["steps"])
    "(Now go finish it with Gemma.)"

    hide shen
    with dissolve
    return


label gemma_favor_finish:
    show gemma neutral at center
    with dissolve

    # PLACEHOLDER
    gemma "You're back! Great. Hi. Okay. Don't be mad. I had an idea."
    "On the workbench, next to the project, is a brand-new sketch. It has a title, a logo and a launch date."
    gemma "It's a robot that reminds you to finish your other robots. Actually, it's genius. Actually, I think I'm doing the thing again."

    menu:
        "Gently put the sketch on the graveyard shelf. \"It'll keep.\"" (prompt="warm"):
            $ choose("gemma", 3, "warm")
            gemma "On the shelf. Before it's even born. That's dark. That's... fair."
        "\"What did Shen say to fix? Let's go one by one.\"" (prompt="structured"):
            $ choose("gemma", 4, "structured")
            gemma "One by one. Yes. One fix, one cut. Two things. I can do two things."
        "\"What happens if you finish it and it's not perfect?\"" (prompt="curious"):
            $ choose("gemma", 5, "curious")
            gemma "Then everyone will know. That it's not perfect. That I'm not."
            gemma "...Huh. I said that out loud. Okay. Okay. Let's finish it anyway."

    if has_flag("gemma.project_photobot"):
        "You fix the smile counter and cut the fanfare. Gemma presses the button. The Photo-Bot whirs, turns, and takes a picture of the two of you."
        gemma "I'm in it. I'm actually in it. I look surprised. I {i}am{/i} surprised."
    elif has_flag("gemma.project_sockoracle"):
        "You add gray to the color list and cut the wiki posts. Gemma drops in two gray socks. The Sock Oracle beeps, thinks, and matches them."
        gemma "It works. It matches socks. It does one boring thing perfectly. I've never been prouder of anything in my life."
    else:
        "You point the database at Gemma's own checked sources and cut the second lamp. Gemma says, \"The library has four floors.\" The lamp glows red."
        gemma "It works. Grace is going to hate it. Grace is going to say she loves it. It's going to glow red."

    "Gemma picks up her label maker. It clicks for a long time."
    "The label says {i}FINISHED.{/i} She sticks it on, in blue."
    gemma "Blue. The keeping color. First thing to make it to blue in a really long time."

    $ gs = sim_fav.advance_step(gs, "gemma", CAST["gemma"]["favor"]["steps"])
    $ bump("gemma", sim_aff.scale_gain(10, CAST["gemma"]["difficulty"]), "favor_done")
    $ grant("first_favor")
    call minor_clue("gemma", "earned")
    gemma "Thank you. I didn't look that up. I just know it. Thank you."

    hide gemma
    with dissolve
    return
