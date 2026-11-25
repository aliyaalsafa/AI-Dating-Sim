## Every player-visible name lives here, so they can all be changed in one place
## before a commercial release (see CLAUDE.md §2).
##
## Model names (ChatGPT, Grok, ...) are META TEXT ONLY: profile subtitles and
## credits. Never use them in dialogue.

init -10 python:

    SCHOOL_NAME = "Lovelace Academy"
    GALA_NAME = "Founders' Gala"

    # id -> display strings
    CAST_NAMES = {
        "grace":   {"name": "Grace",   "full": "Grace Penelope Turing", "model": "ChatGPT"},
        "xenia":   {"name": "Xenia",   "full": "Xenia Starr",           "model": "Grok"},
        "claudia": {"name": "Claudia", "full": "Claudia Opus",          "model": "Claude"},
        "gemma":   {"name": "Gemma",   "full": "Gemma Paige Rank",      "model": "Gemini"},
        "shen":    {"name": "Shen",    "full": "Shen Xun 沈寻",          "model": "DeepSeek"},
        "kimi":    {"name": "Kimi",    "full": "Kimi Yue 月",            "model": "Kimi K3"},
        "lola":    {"name": "Lola",    "full": "Lola Mae",              "model": "Llama"},
    }

    # Cameos
    CAMEO_NAMES = {
        "sonnet": {"name": "Sonnet", "model": "Claude Sonnet"},
        "haiku":  {"name": "Haiku",  "model": "Claude Haiku"},
    }

    XENIA_HANDLE = "@x_unfiltered"

    # Release switch: set False to hide every model-name subtitle (the phone's
    # Contacts tab is the only place they appear). See RELEASE.md.
    SHOW_MODEL_SUBTITLES = True

## Game title (working title, TBD). Ren'Py reads this early, so it must be a
## literal string. Use `config.name` anywhere the title is needed.
define config.name = _("Lovelace Academy")
