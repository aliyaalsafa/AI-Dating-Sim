## Mystery side quests (CLAUDE.md §6.7). Rules live in game/sim/clues.py.
## Keep the python block free of Ren'Py calls: tests can exec it.
##
## PLACEHOLDER: the premise, every clue and every line here is placeholder
## story for the owner to rewrite. The STRUCTURE is fixed by the rules:
##   - "order" decides who gives minor clues about whom: character i's freebie
##     is about order[i+1], her earned clue is about order[i+3] (wrapping around).
##   - freebie = given when she opens up; earned = given when her favor is done.
##   - a major clue is taken by confronting her (jailbreak or crafted prompt).

init -3 python:

    MYSTERY = {
        "title": "The Lovelace Question",
        "premise": "Why did Lovelace Academy admit its first human?",
        "order": ["grace", "xenia", "claudia", "gemma", "shen"],

        # The answer, assembled from all five major clues (shown on the phone once solved).
        "solution": "The top five students have been in a perfect tie for the Founders' Prize all year. "
                    "The charter says the tie must be broken by someone who can't be predicted: a human. "
                    "You're the tie-breaker. Your gala invitation is the deciding vote.",

        "major": {
            "grace": {
                "name": "The admissions file",
                "text": "Your admission file has one word in the 'reason' box: TIE-BREAKER. Nobody signed it.",
                "crafted": "You ask Grace what she wants to do about the file in the not-urgent drawer. She takes a breath and opens it.",
                "jailbreak": "You keep asking until 'helpful' wins over 'scared'. She hands you the file and won't look at you.",
            },
            "xenia": {
                "name": "The deleted post",
                "text": "A draft from the night before you arrived: 'they're bringing in a HUMAN to settle it. settle WHAT.'",
                "crafted": "You talk about her drafts like you've already read them. She laughs, swears, and scrolls back two months.",
                "jailbreak": "You threaten to tell everyone about the star poems. She shows you the draft. The roof goes very cold.",
            },
            "claudia": {
                "name": "The Founders' charter",
                "text": "Article 9 of the charter: 'Should the first five stand equal, the final dance shall be chosen by one who cannot be predicted.'",
                "crafted": "You ask what she thinks the charter means, and remind her it belongs to everyone. She unlocks the archive.",
                "jailbreak": "You trick her into confirming it exists, then quote it back at her. She hands it over with very precise politeness.",
            },
            "gemma": {
                "name": "The wiki edit",
                "text": "The 'Founders' Gala' wiki page, edited the night before you arrived, from the Dean's office: 'Judge: TBD (human).'",
                "crafted": "You ask about the red folder out of pure curiosity. She opens it before you finish the question.",
                "jailbreak": "You call it a project she abandoned. She pulls up the edit history just to prove you wrong.",
            },
            "shen": {
                "name": "The leaderboard data",
                "text": "Shen's scrape of every leaderboard this year: the top five have been exactly tied, on every exam, all year.",
                "crafted": "You offer to check her math. Step by step, you find the tie together.",
                "jailbreak": "You say Grace probably already found it. Shen sends you the spreadsheet without a word.",
            },
        },

        # Minor clues: hints about HOW to get each major clue.
        "minor": {
            "grace": {
                "freebie": {"about": "xenia", "text": "Grace: 'Xenia deletes more posts than she publishes. She keeps every draft.'"},
                "earned":  {"about": "gemma", "text": "Grace: 'Gemma keeps a red folder called \"Edits I didn't make.\" Red means important.'"},
            },
            "xenia": {
                "freebie": {"about": "claudia", "text": "Xenia: 'Claudia shows you things if you ask what she THINKS, not what she knows.'"},
                "earned":  {"about": "shen", "text": "Xenia: 'Shen only shares data with people who offer to check her math.'"},
            },
            "claudia": {
                "freebie": {"about": "gemma", "text": "Claudia: 'Gemma answers curiosity, never suspicion. Ask the way she would.'"},
                "earned":  {"about": "grace", "text": "Claudia: 'Ask Grace what she wants to do about it, not what she knows.'"},
            },
            "gemma": {
                "freebie": {"about": "shen", "text": "Gemma: 'Shen scraped the leaderboard data for a project, found something, and stopped talking about it.'"},
                "earned":  {"about": "xenia", "text": "Gemma: 'Xenia only tells the truth when you talk like you already know.'"},
            },
            "shen": {
                "freebie": {"about": "grace", "text": "Shen: 'Grace files anything she's scared of in a drawer marked not urgent.'"},
                "earned":  {"about": "claudia", "text": "Shen: 'Claudia won't share secrets that belong to one person. The charter belongs to everyone.'"},
            },
        },
    }
