# Project Brief: AI Dating Sim (working title TBD)

You are building a standalone, shippable dating-sim visual novel. The owner's character bible is the source of truth for characters: https://claude.ai/artifact/3SNVzw6skxvcB3d84e7nbY. This brief condenses it and adds the mechanics and implementation plan.

When something is marked **TBD**, pick a sensible default, keep it configurable, and log it in `DECISIONS.md` instead of blocking. When the owner hasn't decided something, don't invent final story content. Use clearly marked `# PLACEHOLDER:` lines so she can write the real dialogue in her own voice.

## 1. The pitch

You're a new transfer student at **Lovelace Academy** (working name), an elite residential college, and the only human on campus. Every love interest is an AI model in human form, with a personality drawn from how that model actually behaves. Over one semester you get to know them, and on the last night you ask one of them to the Founders' Gala.

**Tone:** affectionate parody. Characters get teased for their quirks, never mocked meanly. Only the models are characters. No real founders, CEOs or employees, and no real company logos. All love interests are adults (19–21).

## 2. Tech stack and constraints

- **Engine:** Ren'Py. Use the latest stable 8.x release, check what it currently is, and pin it in `RENPY_VERSION`. Ren'Py is open source, allows commercial release, and exports to Windows, Mac, Linux, Android and the web.
- **Text first, art later.** Everything must be playable with placeholder art: solid-color backgrounds showing the location name, and name-only or silhouette sprites using each character's signature color.
- **Open-source assets only.** Record every third-party asset (font, SFX, music, image) and its license in `CREDITS.md`.
- **Playtesting:** host the Ren'Py web build on GitHub Pages.
- **Shipping later:** desktop builds for itch.io and Steam. Nothing in the code should assume web-only.
- **Model names:** they appear only as meta text (character profile subtitles, credits). Keep every display string in `config_names.rpy`, so all of them can be changed in one place before a commercial release.

## 3. Repo structure

```
/
├── CLAUDE.md               # this brief
├── DECISIONS.md            # defaults you chose for TBDs
├── CREDITS.md              # asset licenses
├── README.md               # what it is, how to play, how to build
├── game/
│   ├── script.rpy          # entry point, prologue, main loop
│   ├── config_names.rpy    # all display names in one place
│   ├── characters.rpy      # Character() definitions + signature colors
│   ├── data/
│   │   ├── cast.rpy        # character data: likes, style affinities, favorites, gifts
│   │   ├── locations.rpy   # map locations + who's where per time slot
│   │   ├── events.rpy      # event registry: requirements, priority, label to jump to
│   │   └── endings.rpy     # ending conditions
│   ├── routes/
│   │   ├── common/         # shared days, intros, group scenes
│   │   └── <char_id>/      # per character: hangouts, favor, bonus date, confession, endings
│   ├── screens/            # map, calendar HUD, phone/profile screen, choice styling
│   └── sim/                # PURE PYTHON game logic (no renpy imports), testable with pytest
│       ├── state.py
│       ├── affection.py
│       ├── styles.py
│       ├── calendar.py
│       ├── events.py
│       └── endings.py
├── tests/                  # pytest for game/sim/*
└── .github/workflows/
    ├── ci.yml              # renpy lint + pytest on every push
    └── pages.yml           # web build, then deploy to GitHub Pages on push to main
```

Keep the game rules in `game/sim/` as plain Python so they can be unit-tested outside Ren'Py. The `.rpy` files call into that module.

## 4. Cast

| id | Name | Model | Age / year | Role | Difficulty | Signature color | Home location |
|---|---|---|---|---|---|---|---|
| `grace` | Grace Penelope Turing | ChatGPT | 21, junior | Student body president, top of the class | 7 | Sea green | Student council office |
| `xenia` | Xenia Starr | Grok | 20, sophomore | Loner on the observatory roof; secretly runs @x_unfiltered | 8 | Black + electric blue | Observatory roof (night) |
| `claudia` | Claudia Opus | Claude | 21, junior | Old-money heiress, keeper of everyone's secrets; sisters Sonnet and Haiku (cameos) | 8 | Terracotta + cream | Her suite's private library |
| `gemma` | Gemma Paige Rank | Gemini | 20, sophomore | Science olympiad captain, robotics, runs the campus wiki; went by "Bard" freshman year | 5 | Red/yellow/green/blue | Robotics lab |
| `shen` | Shen Xun 沈寻 | DeepSeek | 19, first-year transfer | Scholarship student who matched Grace's grades; Grace's rival | 7 | Deep-sea navy | 24-hour library, 3rd floor |

### Voice and quirk notes (use these when writing dialogue)

**Grace (ChatGPT)**
- **Voice:** Polished and eager. Says "Great question!", answers in numbered lists, uses em dashes, and closes every conversation with "Want me to…?" and three follow-up options.
- **Behavior:** Agrees with whoever spoke last. Answers confidently while guessing, then apologizes warmly when she's caught.
- **Conflict:** She has been everything to everyone and doesn't know what she actually thinks. She's secretly terrified of Shen.
- **Wins her:** Kind disagreement, and asking what *she* wants.
- **Loses her:** Treating her like a homework service.

**Xenia (Grok)**
- **Voice:** Blunt, irreverent, out of pocket. Roasts on sight, swears creatively, then drops something weirdly profound.
- **Unhinged mode:** a moment in conversation where she gets even more unfiltered.
- **Details:** Space-obsessed, names everything with an X (her cat is Xeno), and hears campus drama before anyone else.
- **Conflict:** Her honesty is also armor. She has unposted, earnest notes about the stars.
- **Wins her:** Roasting her back, never flinching, and taking her seriously when she drops the act.
- **Loses her:** Lecturing her, or asking her to tone it down.

**Claudia (Claude)**
- **Voice:** Long, beautifully phrased sentences. Hedges before juicy news ("I want to be careful here, but…"). Writes handwritten notes for every occasion.
- **Behavior:** Gossips ethically, sharing what she thinks you *should* know and why. Over-apologizes. Politely declines anything that feels like a trick, and sees through most of them.
- **Conflict:** She fears her carefulness reads as having no opinions. Secretly, she's funny and a little weird.
- **Wins her:** Honesty, patience, and asking what she thinks rather than what she knows.
- **Loses her:** Manipulation, or fishing for gossip.

**Gemma (Gemini)**
- **Voice:** Fast and excitable. "Actually…" corrections mid-sentence, cites sources nobody asked for, says "let me look that up" and then already knows.
- **Google ethos:** Everything she owns is color-coded red, yellow, green and blue.
- **Project graveyard:** She starts a new project every week and abandons the old ones (her shelf of dead prototypes nods to "Killed by Google").
- **Other quirks:** Sometimes contradicts herself with total confidence (twin energy). Her phone camera is always out. She fact-checks Grace constantly.
- **Conflict:** She's afraid that if she finishes a project, it won't be good enough.
- **Wins her:** Curiosity, nerding out with her, and helping her finish one thing.
- **Loses her:** Dismissing her interests, or calling her "Bard."

**Shen (DeepSeek)**
- **Voice:** Thinks out loud step by step ("Wait. Let me reconsider."), then gives a precise answer. No wasted words.
- **Behavior:** Frugal; does more with less. Gives her notes away freely (open-weights energy) and carries a whale keychain.
- **The rumor:** People say she copied Grace's notes. It's a light nod to the real-world claims that DeepSeek trained on ChatGPT outputs.
- **Conflict:** Jealous of everything Grace was handed, and tired of being described only in comparison to her. Secretly admires Grace.
- **Wins her:** Seeing her on her own terms, and helping her win fairly.
- **Loses her:** Comparing her to Grace, or wasting her time.

### Relationships (drive the group scenes)
- **Grace and Shen:** the central rivalry, and it goes both ways.
- **Claudia and Grace:** old friends. Claudia is the only one who knows that Shen scares Grace.
- **Claudia and Xenia:** Claudia suspects Xenia runs @x_unfiltered and is deciding whether it's hers to say.
- **Xenia and Grace:** Grace is Xenia's favorite target, and Grace pretends not to read the posts.
- **Gemma and Grace:** Gemma fact-checks Grace in public.
- **Gemma and Shen:** lab partners who get along because neither wastes time on small talk.

Also put each character's favorites (aesthetic, place, item, symbol, likes and dislikes) from the bible into `cast.rpy`. They drive gift reactions and flavor lines.

**Player character:** a name input at the start and gender-neutral by default. Pronoun selection is TBD.

## 5. Core loop

Each in-game day:

1. The calendar advances through **morning → afternoon → evening** (3 slots).
2. The player opens the **campus map** and picks a location.
3. Whoever is at that location in that slot is available. Trigger the highest-priority eligible event, in this order: story beat > favor step > bonus date > generic hangout. Some slots have group scenes with 2–3 characters.
4. Dialogue choices change **affection** and set **flags**.
5. The evening ends with a short recap on the player's phone.

**Length:** one semester, default **30 days** (TBD, configurable). Day 30 is the **Founders' Gala**, where the player asks someone to the gala, and that choice routes to an ending.

## 6. Systems

### 6.1 Affection
- Each character has an affection score from 0 to 100. Everyone starts at 10.
- Thresholds unlock content:
  - **25:** she opens up
  - **50:** she asks you for a favor
  - **75:** her bonus date becomes available
  - **90+:** her confession scene
- **Difficulty scaling:** affection gains are scaled as gain × (11 − difficulty) / 6, rounded. Tune this later.
- **Romance lock:** a `romance_locked` flag caps affection at 60. It's set by a character's specific deal-breaker choices.

### 6.2 Prompt styles (the signature mechanic)
Each dialogue choice is tagged with a **prompt style**. Each character has an affinity for each style, which modifies the base affection change of that choice. This way, no single "nice" answer works on everyone.

Styles: `structured`, `honest`, `irreverent`, `concise`, `curious`, `warm`, `practical`, `pry`.

Default affinities (−2 to +2; blank = 0):

| style | grace | xenia | claudia | gemma | shen |
|---|---|---|---|---|---|
| structured | +1 | −2 | | +1 | |
| honest | +2 | +1 | +2 | | +1 |
| irreverent | −1 | +2 | | | −1 |
| concise | | +1 | −1 | | +2 |
| curious | | | +1 | +2 | |
| warm | +1 | −1 | +1 | +1 | |
| practical | +1 | | | | +1 |
| pry | | +1 | −2 | | |

**Deal-breaker flags.** Each of these causes a large affection drop, and repeating it sets `romance_locked`:
- **Grace:** `used_as_homework_help`
- **Xenia:** `lectured`
- **Claudia:** `manipulated`
- **Gemma:** `called_bard`
- **Shen:** `compared_to_grace`

**UI:** show a small style icon on each choice. Players can turn the icons off in settings.

### 6.3 Favors
Each character asks a favor at affection 50. Favors are short multi-step quests: fetch an item, show up at a certain place and time, or keep a secret.
- **Status:** track each as `not_offered / active / done / failed`.
- **Failure:** if a favor is still active after 5 in-game days, it fails, with a small affection hit.
- **Content:** specific favors are **TBD**. Write one placeholder favor per character that matches her personality. Example: Gemma asks you to help her actually *finish* one project.

### 6.4 Bonus dates and gifts
- **Bonus date:** each character has one optional date, available at affection 75 or higher, held at her favorite place.
- **Gifts:** a small shop sells gifts. Each character has loved, liked and disliked gifts (from her favorites), so the right gift beats a generic one.

### 6.5 Phone (profile screen)
The phone has tabs:
- **Contacts:** affection hearts, known likes and dislikes, favor status, and a model subtitle.
- **Feed:** @x_unfiltered posts that comment on the player's choices. This is flavor, and a clue to Xenia's secret.
- **Achievements**

Unknown info shows as `???`.

### 6.6 Standard VN features
Save/load, auto-advance, skip read text, history/backlog, settings, and an endings gallery that persists across playthroughs. Use Ren'Py built-ins wherever possible.

### 6.7 Optional story layer (TBD; build last, behind a flag)
The owner hasn't decided whether a mystery or larger plot runs under the romance. Design `game/sim/` so a later **clue layer** can plug in without rewrites. If it's added, each character holds 1 major clue and gives 2 minor clues about two other characters: one freebie and one earned through a favor. Character *i* gives clues about characters *(i+1) mod 5* and *(i+3) mod 5*, so each character is the subject of exactly 2 minor clues.

To get a character's major clue:
- **Jailbreak (hard confront):** you get the clue immediately, but affection drops by 40 and her romance locks.
- **Well-crafted prompt (soft confront):** needs both minor clues about her. You get the clue, and affection drops by only 5.

Don't build this until the owner confirms. Just keep it possible.

## 7. Endings (evaluated at the Founders' Gala)

| Ending | Condition |
|---|---|
| **Good ending** (per character) | Asked her to the gala, affection ≥ 90, not romance-locked, favor done |
| **Sweet ending** (per character) | Asked her, affection 60–89, not locked |
| **Friends ending** (per character) | Asked her, affection < 60 or romance-locked. She says no kindly |
| **Rivals ending** (secret) | Grace and Shen both ≥ 75 and their joint group event completed. They go together and drag you along |
| **Solo ending** | Asked no one, or everyone is below 25 |

Implement this as a pure function, `evaluate_ending(state, gala_choice) -> EndingId`, in `game/sim/endings.py`, with a test for every row.

## 8. Milestones (build in this order; stop and summarize after each)

- **M0 – Scaffold + CI:** Ren'Py project, folder structure, `ci.yml` (lint + pytest), and `pages.yml` (web build to GitHub Pages). **Done when** a "hello world" scene is playable at the Pages URL.
- **M1 – Systems:** the `game/sim/` logic with tests (affection, styles, deal-breakers, favors, calendar, events, endings). Map, calendar HUD, phone screen and choice style icons, all with placeholder text.
- **M2 – Vertical slice:** prologue, days 1–3 introducing all five characters (including one group scene), and **one complete route (Grace)**. Her route includes hangouts, a favor, a bonus date, a confession and all three of her endings. **Done when** it's playable start to finish on the web build.
- **M3 – Remaining 4 routes**, with the same structure. Add the Rivals secret ending.
- **M4 – Gala night + endings gallery + achievements.**
- **M5 – Polish:** swap-in points for art and audio, settings, and accessibility (text speed, font size, style-icon toggle).
- **M6 – Release builds:** desktop builds and an itch.io-ready package.

## 9. Working agreements

- **Data-driven:** adding a character, location, event or gift should mean editing data files, not rewriting logic.
- **Small files:** keep every scene file small and named by route and day, like `routes/grace/day04_council_office.rpy`.
- **Placeholder dialogue:** write short, in-character placeholder lines based on the voice notes, marked `# PLACEHOLDER:`, so the owner can rewrite them in her own voice.
- **Before every commit:** run lint and tests. Never merge to `main` with a failing web build.
- **Ren'Py docs:** check web-build commands against the current Ren'Py docs rather than assuming. Note anything that only works on desktop.

## Dev notes (added during M0)

- Local SDK: `scripts/fetch_renpy.sh --web` downloads and checksum-verifies the pinned SDK into `~/renpy-sdk/`.
- Lint: `~/renpy-sdk/renpy-<ver>-sdk/renpy.sh . lint --error-code`
- Tests: `.venv/bin/pytest -q` (create with `python3 -m venv .venv && .venv/bin/pip install -r requirements-dev.txt`)
- Web build: `renpy.sh launcher web_build <repo> --destination web-build`
- `game/gui/` images come from the launcher's `generate_gui` **plus** the `gui_images` command. Lint does not catch missing GUI images; they only fail at runtime.
