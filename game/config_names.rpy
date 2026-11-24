## Every player-visible name lives here, so they can all be changed in one place
## before a commercial release (see CLAUDE.md §2).
##
## Model names (ChatGPT, Grok, ...) are META TEXT ONLY: profile subtitles and
## credits. Never use them in dialogue.

init -10 python:

    SCHOOL_NAME = "Lovelace Academy"     # working name
    GALA_NAME = "Founders' Gala"

    # id -> display strings
    CAST_NAMES = {
        "grace":   {"name": "Grace",   "full": "Grace Penelope Turing", "model": "ChatGPT"},
        "xenia":   {"name": "Xenia",   "full": "Xenia Starr",           "model": "Grok"},
        "claudia": {"name": "Claudia", "full": "Claudia Opus",          "model": "Claude"},
        "gemma":   {"name": "Gemma",   "full": "Gemma Paige Rank",      "model": "Gemini"},
        "shen":    {"name": "Shen",    "full": "Shen Xun 沈寻",          "model": "DeepSeek"},
    }

    # Cameos
    CAMEO_NAMES = {
        "sonnet": {"name": "Sonnet", "model": "Claude Sonnet"},
        "haiku":  {"name": "Haiku",  "model": "Claude Haiku"},
    }

    XENIA_HANDLE = "@x_unfiltered"

## Game title (working title, TBD). Ren'Py reads this early, so it must be a
## literal string. Use `config.name` anywhere the title is needed.
define config.name = _("Lovelace Academy")
