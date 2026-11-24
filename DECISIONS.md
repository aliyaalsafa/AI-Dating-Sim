# Decisions

Defaults chosen for anything the brief marks TBD or leaves open. Each is configurable; change freely.

| # | Topic | Decision | Where | Date |
|---|---|---|---|---|
| 1 | Ren'Py version | **8.6.1.** renpy.org's "latest" page points to 8.6.1. An 8.6.2 folder exists on the download server but isn't announced yet, so it's not treated as stable. | `RENPY_VERSION` | 2026-11-23 |
| 2 | Game title | "Lovelace Academy" (same as the school's working name) until the owner picks one. | `game/config_names.rpy` (`config.name`) | 2026-11-23 |
| 3 | Resolution | 1920×1080, light theme, pink accent `#ff5fa2`, cream background `#fff6fb`. | `game/gui.rpy` | 2026-11-23 |
| 4 | Gemma's speaker color | Her signature is four colors; the name label uses the blue (`#2f6fdf`). `GEMMA_RAINBOW` is defined for UI flourishes. | `game/characters.rpy` | 2026-11-23 |
| 5 | Player name fallback | Empty name input becomes "You". Pronouns not yet implemented (TBD per brief). | `game/script.rpy` | 2026-11-23 |
| 6 | Dev Python version | CI runs pytest on Python 3.12 to match the interpreter bundled with Ren'Py 8.6. | `.github/workflows/*.yml` | 2026-11-23 |
| 7 | Old Vite scaffold | Removed. Ren'Py replaces it entirely. | — | 2026-11-23 |
| 8 | State updates | Every `game/sim` function returns a new state instead of mutating. Ren'Py only rolls back store variables, so `$ gs = sim...(gs, ...)` keeps rollback and saves correct. | `game/sim/state.py` | 2026-11-23 |
| 9 | Style formula | `delta = base + affinity × 2`, then the difficulty scaling. Losses are not scaled. Weight is `Rules.affinity_weight`. | `game/sim/rules.py` | 2026-11-23 |
| 10 | Deal-breakers | −15 each time; the 2nd offense sets `romance_locked`. | `Rules.dealbreaker_*` | 2026-11-23 |
| 11 | Favor deadline | A favor fails once more than 5 days have passed since it was offered (−5 affection). | `Rules.favor_*` | 2026-11-23 |
| 12 | Gifts | One gift per character per day. Loved +8, liked +4, neutral +1, disliked −4 (gains scaled by difficulty). Start with 100 cash; there's no way to earn more yet (TBD). | `Rules.gift_*`, `data/gifts.rpy` | 2026-11-23 |
| 13 | Schedules | Who's where depends only on the time slot, the same every day. Per-day schedules can be added later. | `data/locations.rpy` | 2026-11-23 |
| 14 | Visiting uses time | Every map visit, including the store, uses one time slot. | `script.rpy` | 2026-11-23 |
| 15 | Rivals ending | Triggers only when the player asks Grace or Shen, and takes priority over their good endings. | `game/sim/endings.py` | 2026-11-23 |
| 16 | Good ending without favor | Affection ≥ 90 but favor not done gives the Sweet ending. | `game/sim/endings.py` | 2026-11-23 |
| 17 | Phone reveals | Unmet characters show as ???. Likes are revealed at affection 25 or by a liked gift; dislikes by a disliked gift or a deal-breaker. | `routes/common/hangouts.rpy`, `game/sim/gifts.py` | 2026-11-23 |
| 18 | CJK text | WenQuanYi Micro Hei (bundled with Ren'Py) is the fallback font for Chinese characters, e.g. Shen's 沈寻. | `game/fonts.rpy` | 2026-11-23 |
| 19 | Placeholder hangouts | M1 uses one generic hangout for everyone, with lines in a Python dict spoken via `renpy.say`. Ren'Py's translation tools can't see those lines; real route scenes (M2+) use normal say statements. | `routes/common/hangouts.rpy` | 2026-11-23 |
