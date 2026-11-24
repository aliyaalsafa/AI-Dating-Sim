## Glue between Ren'Py and the pure-Python rules in game/sim/.
## Every helper replaces `gs` with a new state object, which keeps rollback and
## saves correct (see game/sim/state.py).

init -2 python:

    import sim
    from sim import achievements as sim_ach
    from sim import affection as sim_aff
    from sim import calendar as sim_cal
    from sim import endings as sim_end
    from sim import events as sim_ev
    from sim import favors as sim_fav
    from sim import gifts as sim_gifts
    from sim import state as sim_state
    from sim.rules import DEFAULT_RULES as RULES, SLOTS
    from sim.styles import STYLES

    SLOT_LABELS = {"morning": "Morning", "afternoon": "Afternoon", "evening": "Evening"}

    # Choice badges (CLAUDE.md §6.2). Glyphs verified present in DejaVu Sans.
    STYLE_BADGES = {
        "structured": ("☰", "#3f7cc4"),
        "honest":     ("◆", "#2e8b57"),
        "irreverent": ("☄", "#d9480f"),
        "concise":    ("▸", "#1f3a68"),
        "curious":    ("?", "#7b4dff"),
        "warm":       ("☀", "#e8a400"),
        "practical":  ("⚙", "#6b6b6b"),
        "pry":        ("◎", "#b0306a"),
    }

    def slot_label():
        return SLOT_LABELS[SLOTS[store.gs.slot]]

    def recap_totals():
        totals = {}
        for cid, d, _reason in store.gs.day_log:
            totals[cid] = totals.get(cid, 0) + d
        return totals

    def cname(cid):
        return CAST_NAMES[cid]["name"]

    def notify_delta(cid, delta):
        if delta:
            sfx("affection_up" if delta > 0 else "affection_down")
            renpy.notify("%s  %s%d ♥" % (cname(cid), "+" if delta > 0 else "", delta))

    def choose(cid, base, style=None):
        """Apply a tagged dialogue choice. Sets `last_delta` for reactions."""
        before = store.gs.chars[cid].affection
        store.gs = sim_aff.apply_choice(store.gs, CAST, cid, base, style, RULES)
        store.last_delta = store.gs.chars[cid].affection - before
        notify_delta(cid, store.last_delta)

    def bump(cid, delta, reason=""):
        before = store.gs.chars[cid].affection
        store.gs = sim_aff.add_affection(store.gs, cid, delta, reason, RULES)
        store.last_delta = store.gs.chars[cid].affection - before
        notify_delta(cid, store.last_delta)

    def hit_dealbreaker(cid):
        before = store.gs.chars[cid].affection
        store.gs = sim_aff.dealbreaker(store.gs, CAST, cid, RULES)
        store.last_delta = store.gs.chars[cid].affection - before
        store.gs = sim_state.reveal(store.gs, cid, "dislikes")
        notify_delta(cid, store.last_delta)

    def has_flag(flag):
        return flag in store.gs.flags

    def set_flag(flag):
        store.gs = sim_state.set_flag(store.gs, flag)

    def reveal(cid, key):
        store.gs = sim_state.reveal(store.gs, cid, key)

    def post(text):
        """Add an @x_unfiltered post to the phone feed."""
        s = sim_state.evolve(store.gs)
        s.feed.append({"day": s.day, "text": text})
        store.gs = s

    def buy_gift(gid):
        store.gs = sim_gifts.buy(store.gs, SHOP, gid)
        renpy.notify("Bought: " + SHOP[gid]["name"])

    def grant(aid):
        if aid not in persistent.achievements:
            persistent.achievements.add(aid)
            achievement.grant(aid)
            sfx("achievement")
            renpy.notify("Achievement: " + ACHIEVEMENTS[aid]["name"])

    def check_achievements():
        """Grant every state-derived achievement that now holds (game/sim/achievements.py)."""
        for aid in sorted(sim_ach.earned(store.gs, CAST.keys(), persistent.endings_seen)):
            if aid in ACHIEVEMENTS:
                grant(aid)

    def endings_progress():
        return sim_ach.endings_progress(CAST.keys(), persistent.endings_seen)

    for _aid in ACHIEVEMENTS:
        achievement.register(_aid)

    def location_bg(lid):
        loc = LOCATIONS[lid]
        return placeholder_bg(loc["name"], loc["color"], loc.get("text_color", "#3a164099"))

default gs = None
default last_delta = 0
default persistent.show_style_icons = True
default persistent.achievements = set()
default persistent.endings_seen = set()

screen style_badge(ps):
    frame:
        background Solid(STYLE_BADGES[ps][1])
        padding (14, 4)
        yalign 0.5
        text "%s %s" % (STYLE_BADGES[ps][0], ps) size 24 color "#ffffff" bold True
