## Mystery: the secret Turing test (CLAUDE.md §6.5): the hook, pair-scene
## hints, asking for major clues, and the reveal.
## Data: game/data/mystery.rpy. Rules: game/sim/clues.py.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

init python:

    def mystery_on():
        return RULES.clue_layer

    def mystery_can_ask(cid):
        """Can you ask her for her major clue on this visit?

        Offered once you've overheard at least one hint about her, so it
        doesn't interrupt every visit from day 2. Jailbreaking still always works.
        """
        return (mystery_on() and has_flag("met_" + cid)
                and sim_clues.can_confront(store.gs, cid)
                and bool(sim_clues.minors_about(store.gs, MYSTERY, cid)))

    def mystery_seed_new_game():
        """Hints heard in earlier playthroughs carry over (Rules.minor_clues_persist)."""
        if mystery_on() and RULES.minor_clues_persist and persistent.hints_heard:
            store.gs = sim_clues.seed_minors(store.gs, persistent.hints_heard)

    def mystery_progress():
        return len(sim_clues.known_majors(store.gs)), len(MYSTERY["order"])

default persistent.hints_heard = set()


## Day 1 evening: the second envelope starts the mystery.
label mystery_hook:
    if not mystery_on():
        return
    # PLACEHOLDER: mystery hook (in layer 2, Ada wrote this note)
    "There's a second envelope under the first one. Plain white. Typed, not written."
    "{i}Ask them why you were admitted. Each of them holds one piece. Listen when they think you can't hear. — A friend{/i}"
    $ set_flag(sim_clues.STARTED_FLAG)
    "(A new tab has appeared on your phone: Case.)"
    return


## End of every pair scene (routes/common/pairs/): you overhear one hint about
## each girl, both warm to you a little, and you learn something about each.
label pair_done(pid):
    $ _pair = sim_clues.pair_by_id(MYSTERY, pid)
    python:
        for _c in _pair["chars"]:
            bump(_c, sim_aff.scale_gain(RULES.pair_gain, CAST[_c]["difficulty"]), "pair")
    if mystery_on():
        $ gs, _new = sim_clues.give_pair_hints(gs, MYSTERY, pid)
        $ persistent.hints_heard |= set(_new)
        $ _h1 = _pair["hints"][_pair["chars"][0]]
        $ _h2 = _pair["hints"][_pair["chars"][1]]
        "{i}[_h1]{/i}"
        "{i}[_h2]{/i}"
        if _new:
            $ renpy.notify("New hints on your phone's Case tab")
    python:
        for _c in _pair["chars"]:
            learn_fact(_c)
    return


label mystery_confront(cid):
    $ _who = CHAR[cid]
    $ _clue = MYSTERY["major"][cid]
    $ _cn = cname(cid)
    $ _ready = sim_clues.can_craft(gs, MYSTERY, cid)
    $ renpy.show((cid, "neutral"), at_list=[center])
    with dissolve
    $ _before = gs.chars[cid].affection
    # PLACEHOLDER: confront framing
    "You ask [_cn] why Lovelace Academy admitted a human."
    $ renpy.say(_who, "...Why are you asking me?")
    menu:
        "Ask the right way, using what you overheard" if _ready:
            $ gs = sim_clues.confront(gs, MYSTERY, cid, sim_clues.CRAFTED, RULES)
            $ notify_delta(cid, gs.chars[cid].affection - _before)
            $ _line = _clue["crafted"]
            "[_line]"
        "Push until she cracks (jailbreak: big affection loss, romance locked)":
            $ gs = sim_clues.confront(gs, MYSTERY, cid, sim_clues.JAILBREAK, RULES)
            $ notify_delta(cid, gs.chars[cid].affection - _before)
            $ _line = _clue["jailbreak"]
            "[_line]"
        "Never mind":
            $ renpy.say(_who, "Okay. ...You're being weird, but okay.")
            $ renpy.hide(cid)
            with dissolve
            return
    $ _name = _clue["name"]
    $ _text = _clue["text"]
    "{b}Major clue: [_name]{/b}\n{i}[_text]{/i}"
    $ renpy.hide(cid)
    with dissolve
    $ _found, _total = mystery_progress()
    if _found == _total:
        call truth_reveal
        $ set_flag(sim_clues.TRUTH_FLAG)
        $ check_achievements()
    else:
        "([_found] of [_total] pieces found. Check Case on your phone.)"
    return
