## Mystery side quests (CLAUDE.md §6.7): the hook, clue hand-offs, confronts,
## and the secret ending. Data: game/data/mystery.rpy. Rules: game/sim/clues.py.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

init python:

    def mystery_on():
        return RULES.clue_layer

    def mystery_targets(lid):
        """Characters at this location whose major clue you could still go after."""
        if not mystery_on() or not has_flag(sim_clues.STARTED_FLAG):
            return []
        return [c for c in sim_ev.present(LOCATIONS, lid, store.gs) if sim_clues.can_confront(store.gs, c)]

    def mystery_seed_new_game():
        """Minor clues found in earlier playthroughs carry over (Rules.minor_clues_persist)."""
        if mystery_on() and RULES.minor_clues_persist and persistent.minor_clues:
            store.gs = sim_clues.seed_minors(store.gs, persistent.minor_clues)

    def mystery_progress():
        return len(sim_clues.known_majors(store.gs)), len(MYSTERY["order"])

default persistent.minor_clues = set()


## Day 1 evening: the second envelope starts the mystery.
label mystery_hook:
    if not mystery_on():
        return
    # PLACEHOLDER: mystery hook
    "There's a second envelope under the first one. Plain white. Typed, not written."
    "{i}Ask them why you were admitted. Each of them holds one piece. Some will tell you if you ask the right way. — A friend{/i}"
    $ set_flag(sim_clues.STARTED_FLAG)
    "(A new tab has appeared on your phone: Case.)"
    return


## A character hands over one of her minor clues (freebie when she opens up,
## earned when her favor is done). Silent if the mystery is off or already known.
label minor_clue(source, which):
    if not mystery_on():
        return
    $ _entry = MYSTERY["minor"][source][which]
    $ _pair = (source, _entry["about"])
    if _pair in sim_clues.known_minors(gs):
        return
    $ gs, _pair = sim_clues.give_minor(gs, MYSTERY["order"], source, which)
    $ persistent.minor_clues.add(_pair)
    $ renpy.notify("New clue about " + cname(_entry["about"]))
    $ _clue_text = _entry["text"]
    "{i}[_clue_text]{/i}"
    return


## Offered when you visit a location where someone still holds a major clue.
## Returns the character to confront, or None to spend time normally.
label mystery_offer(lid):
    $ _targets = mystery_targets(lid)
    if not _targets:
        return None
    # A None value would make Ren'Py draw the item as an unclickable caption.
    $ _opts = [("Spend time together", "__hangout__")] + [("Ask %s about the admissions mystery" % cname(c), c) for c in _targets]
    $ _pick = renpy.display_menu(_opts)
    return (None if _pick == "__hangout__" else _pick)


label mystery_confront(cid):
    $ _who = CHAR[cid]
    $ _clue = MYSTERY["major"][cid]
    $ _cn = cname(cid)
    $ _ready = sim_clues.can_craft(gs, MYSTERY["order"], cid)
    $ renpy.show((cid, "neutral"), at_list=[center])
    with dissolve
    $ _before = gs.chars[cid].affection
    # PLACEHOLDER: confront framing
    "You ask [_cn] why Lovelace Academy admitted a human."
    $ renpy.say(_who, "...Why are you asking me?")
    menu:
        "Ask the right way, using what you've learned" if _ready:
            $ gs = sim_clues.confront(gs, MYSTERY["order"], cid, sim_clues.CRAFTED, RULES)
            $ notify_delta(cid, gs.chars[cid].affection - _before)
            $ _line = _clue["crafted"]
            "[_line]"
        "Push until she cracks (jailbreak: big affection loss, romance locked)":
            $ gs = sim_clues.confront(gs, MYSTERY["order"], cid, sim_clues.JAILBREAK, RULES)
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
    $ _found, _total = mystery_progress()
    if _found == _total:
        "That's every piece. You know why you're here. The question is what you'll do about it at the gala."
    else:
        "([_found] of [_total] pieces found. Check Case on your phone.)"
    $ renpy.hide(cid)
    with dissolve
    return


## Secret ending: reveal the truth at the gala instead of asking anyone.
label ending_truth(ending):
    scene bg gala
    with fade
    # PLACEHOLDER: The Lovelace Question (secret ending)
    "When the music stops for the invitations, you don't walk toward anyone. You walk to the microphone."
    "You tell the whole room what you found: the file, the draft, the charter, the edit, the data."
    show grace neutral at left
    show shen neutral at right
    with dissolve
    grace "A five-way tie. All year. And they brought in a human to... pick one of us?"
    shen "Wait. Let me reconsider. They didn't bring you in to pick. They brought you in so we'd compete for you."
    hide grace
    hide shen
    show claudia neutral at left
    show xenia neutral at right
    with dissolve
    claudia "I want to be careful here, but I think we've all been very carefully played."
    xenia "Oh, I'm posting this. Under my real name. Watch me."
    hide claudia
    hide xenia
    show gemma neutral at center
    with dissolve
    gemma "So nobody wins the Founders' Prize? Actually, that means everybody ties forever. Actually, that's the best result."
    hide gemma
    with dissolve
    "Nobody dances with you. All five of them drag you onto the floor at once, and nobody leads."
    "The Founders' Prize goes unclaimed. The charter gets a new article by morning, written by five people who finally agree on something."
    call ending_card(ending)
    return
