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
