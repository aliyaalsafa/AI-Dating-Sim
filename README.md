# Lovelace Academy (working title)

A dating-sim visual novel. You're the only human at an elite college where every love interest is an AI model in human form. Get to know them over one semester, then ask one to the Founders' Gala.

Built with [Ren'Py](https://www.renpy.org) (version pinned in `RENPY_VERSION`). The full design brief is in [CLAUDE.md](CLAUDE.md).

## Play

- **Web:** the GitHub Pages build (deployed automatically from `main`).
- **Locally:** open the project in the Ren'Py launcher, or run `~/renpy-sdk/renpy-8.6.1-sdk/renpy.sh .` from the repo root.

## Develop

```bash
scripts/fetch_renpy.sh --web            # download + verify the pinned SDK into ~/renpy-sdk
python3 -m venv .venv && .venv/bin/pip install -r requirements-dev.txt
```

| Task | Command |
| --- | --- |
| Run the game | `~/renpy-sdk/renpy-8.6.1-sdk/renpy.sh .` |
| Lint | `~/renpy-sdk/renpy-8.6.1-sdk/renpy.sh . lint --error-code` |
| Unit tests (`game/sim`) | `.venv/bin/pytest -q` |
| Web build | `~/renpy-sdk/renpy-8.6.1-sdk/renpy.sh ~/renpy-sdk/renpy-8.6.1-sdk/launcher web_build . --destination web-build` |

Run lint and tests before every commit. CI (`.github/workflows/ci.yml`) runs both on every push; `pages.yml` builds and deploys the web version on pushes to `main`.

## Layout

- `game/` — the Ren'Py project. Game rules live in `game/sim/` as plain Python with no Ren'Py imports, so they can be unit-tested.
- `tests/` — pytest for `game/sim/`.
- `ASSETS.md` — how to drop in real art, music and sound effects (file names only, no code).
- `DECISIONS.md` — defaults chosen where the brief said TBD.
- `CREDITS.md` — every third-party asset and its license.
