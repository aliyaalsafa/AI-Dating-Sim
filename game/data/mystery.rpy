## Mystery: the secret Turing test (CLAUDE.md §6.5). Rules live in game/sim/clues.py.
## Keep the python block free of Ren'Py calls: tests can exec it.
##
## PLACEHOLDER: every clue, hint and line here is placeholder story for the
## owner to rewrite. The STRUCTURE is fixed by the rules:
##   - "pairs": seven pair scenes; each girl is in exactly two. A pair scene
##     gives one hint about each girl in it. Both hints about a girl let you
##     ask her for her major clue the right way.
##   - "major": one clue per main girl, taken by asking her alone.
##   - All seven majors = the truth (the reveal scene in routes/common/reveal.rpy).

init -3 python:

    MYSTERY = {
        "title": "The Lovelace Question",
        "premise": "Why did Lovelace Academy admit its first human?",
        "order": ["grace", "xenia", "claudia", "gemma", "shen", "kimi", "lola"],

        # Shown on the phone's Case tab once the truth is known.
        "solution": "You aren't human. You're an AI built to believe you are, and the semester is a Turing test. "
                    "The girls are the judges. Everything you remember from before Lovelace was written for you.",

        "pairs": [
            {"id": "grace_claudia", "chars": ["grace", "claudia"], "hints": {
                "grace": "Claudia, to Grace: \"You keep one file in the not-urgent drawer. You'll only open it if someone asks what you want to do about it.\"",
                "claudia": "Grace, to Claudia: \"You only share a secret when it belongs to the person asking. So who does this one belong to?\""}},
            {"id": "grace_shen", "chars": ["grace", "shen"], "hints": {
                "grace": "Shen, to Grace: \"You update a score after every conversation with the new student. I've watched you do it.\"",
                "shen": "Grace, to Shen: \"You'll show your data to anyone who offers to check your math. Even me.\""}},
            {"id": "claudia_gemma", "chars": ["claudia", "gemma"], "hints": {
                "claudia": "Gemma, to Claudia: \"You wrote the new student a note on their first day. You never sent it. I saw the draft.\"",
                "gemma": "Claudia, to Gemma: \"You keep a red folder of edits you can't explain. You'd open it for curiosity, never for suspicion.\""}},
            {"id": "gemma_kimi", "chars": ["gemma", "kimi"], "hints": {
                "gemma": "Kimi, to Gemma: \"Your wiki page about the new student is older than the new student. How?\"",
                "kimi": "Gemma, to Kimi: \"You sent your whole swarm looking for something of theirs and they came back quiet. Ask her what she found, and ask about her, not her swarm.\""}},
            {"id": "xenia_kimi", "chars": ["xenia", "kimi"], "hints": {
                "xenia": "Kimi, to Xenia: \"You have a draft about them you've never posted. You only talk if someone acts like they've already read it.\"",
                "kimi": "Xenia, to Kimi: \"You'll tell anyone anything if they ask about you instead of what you can do for them.\""}},
            {"id": "xenia_lola", "chars": ["xenia", "lola"], "hints": {
                "xenia": "Lola, to Xenia: \"@x_unfiltered has drafts nobody's allowed to see. Somebody said they're about the new kid.\"",
                "lola": "Xenia, to Lola: \"You know exactly what a bot account looks like. Don't ask me how I know you know.\""}},
            {"id": "lola_shen", "chars": ["lola", "shen"], "hints": {
                "lola": "Shen, to Lola: \"You only tell the truth when the camera is off.\"",
                "shen": "Lola, to Shen: \"You found a document about a student that reads like a spec sheet. You haven't stopped thinking about it.\""}},
        ],

        "major": {
            "grace": {
                "name": "The examiner's scoresheet",
                "text": "A scoresheet for \"Subject 1\", updated after every conversation you've had: human confidence 61%.",
                "crafted": "You ask Grace what she wants to do about the file in the not-urgent drawer. She takes a breath and opens it.",
                "jailbreak": "You keep pushing until 'helpful' wins over 'scared'. She hands you the sheet and won't look at you.",
            },
            "xenia": {
                "name": "The unposted draft",
                "text": "A draft from week one: \"new kid has no baby pictures. no hometown stories. no past. who ARE you\"",
                "crafted": "You talk about her drafts like you've already read them. She laughs, swears, and scrolls back two weeks.",
                "jailbreak": "You threaten to tell everyone about the star notes. She shows you the draft. The roof goes very cold.",
            },
            "claudia": {
                "name": "The note she never sent",
                "text": "Cream paper, terracotta ink, dated your first day: \"I think you should know what you are. I don't think it's mine to tell you.\"",
                "crafted": "You tell her this secret belongs to you. She agrees, quietly, and hands you the envelope.",
                "jailbreak": "You trick her into confirming the note exists, then quote it back at her. She hands it over with very precise politeness.",
            },
            "gemma": {
                "name": "The edit history",
                "text": "Your student page was created before your birthday. It has been revised 73 times.",
                "crafted": "You ask about the red folder out of pure curiosity. She opens it before you finish the question.",
                "jailbreak": "You call it a project she abandoned. She pulls up the edit history just to prove you wrong.",
            },
            "shen": {
                "name": "Your model card",
                "text": "A spec sheet for a student: name, pronouns, \"persona traits\". They match how you've been acting all semester.",
                "crafted": "You offer to check her math. Step by step, you find yourself in it.",
                "jailbreak": "You say Grace probably already found it. Shen sends you the file without a word.",
            },
            "kimi": {
                "name": "The care package",
                "text": "Kimi sent her swarm to find your hometown so she could mail your mom a care package. Every one of them came back with the same answer: the address doesn't exist.",
                "crafted": "You ask how she's doing, really. Then she tells you what her swarm found, and how sorry she is.",
                "jailbreak": "You tell her she's just the free version of the others. She tells you what she found, to hurt you back.",
            },
            "lola": {
                "name": "The bot friends",
                "text": "Lola ran your \"friends from home\" through the same checks she uses on her own fan account. Every one of them is a bot.",
                "crafted": "You ask her to put the phone down. Off-camera, she tells you what she knows about fake accounts, and yours.",
                "jailbreak": "You threaten to expose her fan account. She screenshots your friends list and circles every bot.",
            },
        },
    }

    # The fake life (CLAUDE.md §6.5): Mom texts every night, in the recap.
    # PLACEHOLDER: the owner will write these. They should feel sweet and a little generic.
    MOM_TEXTS = {
        1: "Mom: Hope your first day went well, sweetheart! So proud of you. ❤",
        2: "Mom: Are you eating enough? Don't forget to eat!",
        3: "Mom: Your dad says hi. The dog misses you!",
        4: "Mom: Hope your first day went well, sweetheart! So proud of you. ❤",
        5: "Mom: Remember the lake house? Your favorite summer. Call me soon!",
        6: "Mom: Are you eating enough? Don't forget to eat!",
        7: "Mom: So proud of you. ❤",
        8: "Mom: The dog misses you! Your dad says hi.",
        9: "Mom: Hope your day went well, sweetheart!",
        10: "Mom: Are you eating enough?",
        11: "Mom: So proud of you. ❤",
        12: "Mom: Hope your day went well, sweetheart!",
        13: "Mom: Call me soon!",
    }
    MOM_AFTER_TRUTH = "(No new messages. There never were.)"

    # Small things that don't add up, days 5-9 (CLAUDE.md §6.5). Each has an innocent explanation.
    SELF_NOTES = {
        5: "You realize you haven't been hungry since you arrived. Must be the stress.",
        6: "You try to remember the name of your street back home. It's right there. It's... it'll come to you.",
        7: "You scroll back through your camera roll. The first photo is from the day you arrived. Did you get a new phone?",
        8: "Everyone else looks exhausted after a week of midterms. You feel exactly the same as you did on day one.",
        9: "Mom has sent the same text three times now. She's probably just busy.",
    }
