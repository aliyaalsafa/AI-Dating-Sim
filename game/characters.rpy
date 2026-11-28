## Character() definitions and signature colors.
## Display names come from config_names.rpy.

init -5 python:

    # Signature colors (CLAUDE.md §4). "name" is used for the speaker label,
    # "fill"/"accent" for placeholder sprites and UI.
    SIGNATURE_COLORS = {
        "grace":   {"name": "#2e8b57", "fill": "#2e8b57", "accent": "#bfe8d2"},  # sea green
        "xenia":   {"name": "#1c1c1f", "fill": "#111418", "accent": "#ffffff"},  # black + white (Grok)
        "claudia": {"name": "#b5532f", "fill": "#c9653c", "accent": "#f3e9d8"},  # terracotta + cream
        "gemma":   {"name": "#2f6fdf", "fill": "#2f6fdf", "accent": "#f2c230"},  # red/yellow/green/blue; blue as base
        "shen":    {"name": "#1f3a68", "fill": "#1f3a68", "accent": "#9fb7dd"},  # deep-sea navy
        "kimi":    {"name": "#8a6fc9", "fill": "#a48ad8", "accent": "#d9dde3"},  # lavender + silver
        "lola":    {"name": "#e0457b", "fill": "#f06292", "accent": "#ffb26b"},  # sunset gradient (pink/orange/purple)
    }

    GEMMA_RAINBOW = ["#d93a2b", "#f2b01e", "#2e9e4f", "#2f6fdf"]

define narrator = Character(None)
define mc = Character("[player_name]", color="#7b4dff", namebox_background=namebox_bg("mc"), who_color="#ffffff")

define grace   = Character(CAST_NAMES["grace"]["name"],   color="#ffffff", namebox_background=namebox_bg("grace"), who_color="#ffffff")
define xenia   = Character(CAST_NAMES["xenia"]["name"],   color="#ffffff", namebox_background=namebox_bg("xenia"), who_color="#ffffff")
define claudia = Character(CAST_NAMES["claudia"]["name"], color="#ffffff", namebox_background=namebox_bg("claudia"), who_color="#ffffff")
define gemma   = Character(CAST_NAMES["gemma"]["name"],   color="#ffffff", namebox_background=namebox_bg("gemma"), who_color="#ffffff")
define shen    = Character(CAST_NAMES["shen"]["name"],    color="#ffffff", namebox_background=namebox_bg("shen"), who_color="#ffffff")
define kimi    = Character(CAST_NAMES["kimi"]["name"],    color="#ffffff", namebox_background=namebox_bg("kimi"), who_color="#ffffff")
define lola    = Character(CAST_NAMES["lola"]["name"],    color="#ffffff", namebox_background=namebox_bg("lola"), who_color="#ffffff")
define mom     = Character("Mom", color="#ffffff", who_color="#ffffff")

default player_name = "You"

define CHAR = {"grace": grace, "xenia": xenia, "claudia": claudia, "gemma": gemma, "shen": shen, "kimi": kimi, "lola": lola}

# Cameos: Claudia's younger sisters.
define sonnet = Character(CAMEO_NAMES["sonnet"]["name"], color="#c98a5a", namebox_background=namebox_bg("claudia"), who_color="#ffffff")
define haiku  = Character(CAMEO_NAMES["haiku"]["name"],  color="#d9a37a", namebox_background=namebox_bg("claudia"), who_color="#ffffff")
