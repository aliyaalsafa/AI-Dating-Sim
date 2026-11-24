# Releasing

How to turn `main` into downloadable builds (CLAUDE.md §8 M6).

## What gets built

`scripts/build_release.sh` (locally) or the **Release builds** workflow (CI)
produces these in `dists/`:

| File | Platform | itch.io channel |
| --- | --- | --- |
| `AIDatingSim-<ver>-win.zip` | Windows 64-bit | `win` |
| `AIDatingSim-<ver>-mac.zip` | macOS `.app` (Intel + Apple Silicon), unsigned | `osx` |
| `AIDatingSim-<ver>-linux.tar.bz2` | Linux x86_64 | `linux` |
| `AIDatingSim-<ver>-web.zip` | HTML5 (upload as "playable in browser") | `html5` |
| `SHA256SUMS.txt` | checksums | — |

Each desktop package is about 25–45 MB; the web zip is about 20 MB.

Release builds differ from the GitHub Pages playtest build:

- **No Dev button.** It only appears when running from the SDK, or when
  `game/playtest_enabled.txt` exists. Only `pages.yml` creates that file; it is
  gitignored, and the build script refuses to run if it's present.
- **Scripts are compiled and archived** (`game/scripts.rpa`). `.rpy` source,
  tests, docs and repo tooling are excluded (see `build.classify` in
  `game/options.rpy`).

## Checklist

1. **Version.** Bump `config.version` in `game/options.rpy` (currently `0.1.0`).
2. **Names.** Review `game/config_names.rpy`: game title (still a working
   name), school, gala. For a commercial release, decide whether to keep the
   model-name subtitles; `SHOW_MODEL_SUBTITLES = False` hides all of them.
3. **Placeholders.** `grep -rn "PLACEHOLDER" game/routes` lists dialogue still
   waiting for the owner's rewrite.
4. **Credits.** Every third-party asset is in `CREDITS.md`, and the About
   screen text (`gui.about` in `options.rpy`) is current.
5. **Icons (TBD).** Builds use Ren'Py's default app icon. To brand them, add
   `icon.ico` (Windows) and `icon.icns` (macOS) to the repo root, and replace
   `game/gui/window_icon.png`.
6. **Check.** `.venv/bin/pytest -q`, lint, then `scripts/build_release.sh` and
   open one build.
7. **Tag.** `git tag v0.1.0 && git push origin v0.1.0`. The tag must equal
   `v` + `config.version`, or the workflow stops. CI builds everything and
   attaches it to a GitHub Release.

## itch.io

1. Create the project at https://itch.io/game/new. Kind: **Downloadable**, or
   **HTML** if you also want it playable in the browser. Page copy draft:
   [ITCH.md](ITCH.md).
2. Automatic uploads from CI (optional):
   - Get an API key from https://itch.io/user/settings/api-keys.
   - In the GitHub repo settings, add secret `BUTLER_API_KEY` and variable
     `ITCH_PROJECT` (e.g. `your-name/lovelace-academy`).
   - The next tagged release pushes all four packages with `butler`. Without
     these settings, the itch step is skipped.
3. Manual upload instead: drag the files from the GitHub Release (or `dists/`)
   onto the itch.io edit page. Mark `-web.zip` as "This file will be played in
   the browser" and set the viewport to 1280×720 with fullscreen allowed.

## Platform notes

- **macOS:** the app is not signed or notarized, so first launch needs
  right-click → Open. Signing needs an Apple Developer account
  (`renpy.sh launcher distribute --macapp <signed.app>` accepts a signed app).
  `.dmg` packages need macOS tools, so CI builds the `.zip` only.
- **Windows:** unsigned, so SmartScreen may warn on first launch.
- **Steam (later):** Ren'Py has a `steam` package and Steamworks support. That
  needs an app ID, achievements mirrored in Steamworks (the IDs are in
  `game/data/achievements.rpy` and are already registered with Ren'Py's
  `achievement` API), and a `steam_appid.txt`. Not set up yet.
- **Saves** live in the OS's Ren'Py save folder under `AIDatingSim-1795488577`
  (`config.save_directory`). Don't change that after release, or players lose
  their saves.
