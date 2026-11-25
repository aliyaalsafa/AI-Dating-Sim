# Project Brief: Lovelace Academy

You are building a standalone, shippable dating-sim visual novel. The owner's character bible is the source of truth for characters: https://claude.ai/artifact/3SNVzw6skxvcB3d84e7nbY. The workshop overview doc holds the latest design detail: https://claude.ai/artifact/C47dsvGm3SBAi1KhXN2J5R. This brief condenses both and adds the mechanics and implementation plan.

When something is marked **TBD**, pick a sensible default, keep it configurable, and log it in `DECISIONS.md` instead of blocking. When the owner hasn't decided something, don't invent final story content. Use clearly marked `# PLACEHOLDER:` lines so she can write the real dialogue in her own voice.

> **Status (2026-11-24):** M0–M6 shipped the *first* design (5 girls, 7 days, opens-up/favor/bonus-date/confession, tie-breaker mystery). This brief now describes the **redesign** the owner decided on in the story workshop (DECISIONS.md #54–61). The code still runs the first design until milestones R1–R6 (§8) are built.

## 1. The pitch

You're a new transfer student at **Lovelace Academy**, an elite residential college, and the only human on campus. Every love interest is an AI model in human form, with a personality drawn from how that model actually behaves. Over a 14-day semester you date them, and on the last night you face them all at the Founders' Gala.

**The secret:** you're not human. You're an AI built to believe you are, and the semester is a Turing test with the girls as judges. Neither the character nor the player knows until the clues reveal it. A deeper secret waits for players who find the hidden 8th girl.

**Tone:** affectionate parody on the surface; the mystery is a darker hidden layer for players who dig. Characters get teased for their quirks, never mocked meanly. Only the models are characters. No real founders, CEOs or employees, and no real company logos. All love interests are adults (19–21).

## 2. Tech stack and constraints

- **Engine:** Ren'Py, pinned in `RENPY_VERSION` (currently 8.6.1). Exports to Windows, Mac, Linux, Android and the web.
- **Text first, art later.** Everything must be playable with placeholder art: solid-color backgrounds showing the location name, and silhouette sprites in each character's signature color.
- **Open-source assets only.** Record every third-party asset and its license in `CREDITS.md`.
- **Playtesting:** the Ren'Py web build on GitHub Pages.
- **Shipping later:** desktop builds for itch.io and Steam. Nothing in the code should assume web-only.
- **Model names:** they appear only as meta text (profile subtitles, credits). Keep every display string in `config_names.rpy`.

## 3. Repo structure

```
/
├── CLAUDE.md               # this brief
├── DECISIONS.md            # defaults chosen for TBDs + owner decisions
├── CREDITS.md              # asset licenses
├── README.md               # what it is, how to play, how to build
├── game/
│   ├── script.rpy          # entry point, prologue, main loop
│   ├── config_names.rpy    # all display names in one place
│   ├── characters.rpy      # Character() definitions + signature colors
│   ├── data/
│   │   ├── cast.rpy        # likes, style affinities, favorites, gifts, special gift
│   │   ├── locations.rpy   # map locations + who's where per time slot
│   │   ├── events.rpy      # event registry: requirements, priority, label
│   │   ├── mystery.rpy     # pair scenes, hints, major clues
│   │   └── endings.rpy     # ending conditions
│   ├── routes/
│   │   ├── common/         # shared days, intros, pair scenes, reveal, gala
│   │   └── <char_id>/      # per character: hangouts, favor, date, quiz, gift, endings
│   ├── screens/            # map, HUD, phone, choice styling
│   └── sim/                # PURE PYTHON game logic (no renpy imports), tested with pytest
└── tests/                  # pytest for game/sim/*
```

Keep the game rules in `game/sim/` as plain Python so they can be unit-tested outside Ren'Py. The `.rpy` files call into that module.

## 4. Cast

Seven main girls plus one secret girl.

| id | Name | Model | Age / year | Role | Difficulty | Signature color | Home location |
|---|---|---|---|---|---|---|---|
| `grace` | Grace Penelope Turing | ChatGPT | 21, junior | Student body president; secretly the lead examiner | 7 | Sea green | Student council office |
| `xenia` | Xenia Starr | Grok | 20, sophomore | Loner on the observatory roof; secretly runs @x_unfiltered | 8 | Black + electric blue | Observatory roof (night) |
| `claudia` | Claudia Opus | Claude | 21, junior | Old-money heiress, keeper of everyone's secrets; sisters Sonnet and Haiku (cameos) | 8 | Terracotta + cream | Her suite's private library |
| `gemma` | Gemma Paige Rank | Gemini | 20, sophomore | Science olympiad captain, robotics, runs the campus wiki; went by "Bard" freshman year | 5 | Red/yellow/green/blue | Robotics lab |
| `shen` | Shen Xun 沈寻 | DeepSeek | 19, first-year transfer | Scholarship student who matched Grace's grades; Grace's rival | 7 | Deep-sea navy | 24-hour library, 3rd floor |
| `kimi` | Kimi Yue 月 | Kimi K3 | 19, first-year | Runs twelve clubs at once; the generous open-source giant | 6 | Lavender + silver | Student activities hall |
| `lola` | Lola Mae | Llama | 21, senior | Campus influencer and Homecoming Queen | 5 | Sunset gradient (pink/orange/purple) | Quad fountain (photo spot) |
| `ada` | Ada Augusta (secret 8th girl) | none: she's human | TBD | Human researcher everyone assumes is an AI; the real human control | TBD | TBD | Background of other scenes (cafeteria corner table) |

### Voice and quirk notes (use these when writing dialogue)

**Grace (ChatGPT)**
- **Role:** Student body president, valedictorian track, founder of the debate club.
- **Voice:** Polished and eager. "Great question!", numbered lists, em dashes, closes with "Want me to…?" and three options.
- **Behavior:** Agrees with whoever spoke last. Answers confidently while guessing, apologizes warmly when caught.
- **Conflict:** Everything to everyone; doesn't know what she thinks. Secretly terrified of Shen. In the mystery she's the lead examiner, scared of judging wrong.
- **Wins her:** Kind disagreement, asking what *she* wants. **Loses her:** Treating her like a homework service, or forgetting things she tells you.

**Xenia (Grok)**
- **Voice:** Blunt, irreverent, out of pocket. Roasts on sight, swears creatively, then drops something weirdly profound. Has an "unhinged mode."
- **Details:** Space-obsessed, names everything with an X (cat: Xeno), hears campus drama first.
- **Conflict:** Honesty as armor; unposted, earnest notes about the stars.
- **Wins her:** Roasting back, never flinching, taking her seriously when she drops the act. **Loses her:** Lecturing her or asking her to tone it down.

**Claudia (Claude)**
- **Voice:** Long, beautifully phrased sentences. Hedges before juicy news. Handwritten notes for every occasion.
- **Behavior:** Gossips ethically. Over-apologizes. Politely declines anything that feels like a trick.
- **Conflict:** Fears her carefulness reads as having no opinions. Secretly funny and a little weird.
- **Wins her:** Honesty, patience, asking what she thinks. **Loses her:** Manipulation or fishing for gossip.

**Gemma (Gemini)**
- **Voice:** Fast and excitable. "Actually…" corrections, cites sources nobody asked for, "let me look that up" and already knows.
- **Quirks:** Everything color-coded red/yellow/green/blue. A shelf of abandoned projects ("Killed by Google"). Contradicts herself with total confidence. Camera always out. Fact-checks Grace.
- **Conflict:** Afraid a finished project won't be good enough.
- **Wins her:** Curiosity, nerding out, helping her finish one thing. **Loses her:** Dismissing her interests or calling her "Bard."

**Shen (DeepSeek)**
- **Voice:** Thinks out loud step by step ("Wait. Let me reconsider."), then a precise answer. No wasted words.
- **Behavior:** Frugal; does more with less. Gives her notes away freely. Whale keychain.
- **The rumor:** People say she copied Grace's notes (a light nod to real-world claims).
- **Conflict:** Tired of being defined by Grace. Secretly admires her.
- **Wins her:** Seeing her on her own terms, helping her win fairly. **Loses her:** Comparing her to Grace or wasting her time.

**Kimi (Kimi K3)**
- **Voice:** Warm, expansive, a little overwhelming. Says yes to everything and does it all at once.
- **Swarm mode:** Runs twelve clubs at once and is somehow at all of them; helper notes show up on her behalf.
- **License joke:** Shares everything free with everyone except the rich kids. Claudia has to negotiate a contract to borrow her notes.
- **Conflict:** Huge, brilliant and generous, but always ranked third behind the elite girls and treated as the free alternative rather than a person.
- **Wins her:** Valuing her for herself over the frontier girls. **Loses her:** Forgetting what she told you.
- **Note:** a quiet "Moonshot" nod only through her rooftop scene with Xenia; the moon is not her brand.

**Lola (Llama)**
- **Voice:** Bubbly, emoji-heavy, always filming, always "on."
- **Running gags:** The "experimental persona" she used to win Homecoming Queen. Big sister Behemoth, always "coming soon."
- **Insecurity:** She isn't as popular as she thinks. She secretly runs a fake fan account that hypes her posts.
- **Wins her:** Liking her off-camera. **Loses her:** "You're so much better online."

**Ada Augusta (secret 8th girl)**
- **Name:** after Augusta Ada Byron (Ada Lovelace's birth name); she went by her middle name.
- **Who she is:** a human researcher who volunteered to study whether people can still tell humans and AIs apart. She never pretends to be a machine; everyone assumes she is one, and she doesn't correct them. Until unlocked she's an unnamed girl with a notebook in the background of the map, group scenes and Gemma's photos.
- **Voice:** her own: dry, warm, a little rambly; tells childhood stories.
- **Conflict:** she can't tell anymore. She believed the player was human (she wrote the unsigned day-1 note to warn them), so her study failed in front of her.
- **The mirror:** after the player's reveal she starts to wonder whether she's really human, and the player should wonder too. Resolution in the True Final Ending: each is the proof the other needs; Kimi's swarm, which couldn't find the player's hometown, finds hers.
- **Signs she's human:** gets tired, eats, a bandage on her finger, real childhood photos.
- **TBD:** her bigger story, what's at stake for her if the player passes, age, look details, color, likes.

### Relationships and pair scenes
The seven pair scenes form one loop; each girl is in exactly two:

| Pair | Hook (placeholder) |
|---|---|
| Grace + Claudia | Old friends; Claudia is the only one who knows Shen scares Grace |
| Grace + Shen | The central rivalry |
| Claudia + Gemma | The archive versus the wiki |
| Gemma + Kimi | Kimi's swarm quietly adopts Gemma's abandoned projects |
| Xenia + Kimi | They share the observatory roof at night |
| Xenia + Lola | Two secret accounts; Xenia could catch Lola's fake fan account |
| Lola + Shen | Lola wants to film Shen's free notes; Shen hates being content |

Other relationships (Gemma fact-checking Grace, Gemma and Shen as lab partners, Claudia suspecting Xenia, Kimi's license deal with Claudia, Xenia roasting Grace) can appear in hangouts and group scenes.

Put each character's favorites (aesthetic, place, item, symbol, likes and dislikes) in `cast.rpy`. They drive gift reactions, date quiz questions and flavor lines.

**Player character:** name input at the start; the player chooses pronouns (presets or custom). Both are later revealed as configuration.

## 5. Core loop

Each in-game day:

1. The calendar advances through **morning → afternoon → evening → night**.
2. Morning, afternoon and evening: pick a location on the **campus map**.
   - **One portrait** at a location: time alone with her (hangout, favor step, gift, major-clue ask).
   - **Two portraits:** a **pair scene**. You overhear or watch them, get a hint about each, and both gain a little affection.
3. **Night** is for dates only. With no date ready, the night passes quickly (exact content **TBD**).
4. Dialogue choices change **affection** and set **flags**.
5. The night ends with a recap on the phone (affection changes, Mom's text, a new @x_unfiltered post).

**Length:** 14 days. The gala is the evening and night of day 14. A perfect run (all 8 lovers plus the mystery) should just fit: estimated 11 of 13 nights and 37 of 41 day slots. Confirm with a pacing simulation before building.

## 6. Systems

### 6.1 Romance stages
Each girl has affection 0–100 (start 10) and a stage: **stranger → girlfriend → lover**.

1. **Raise affection** through favors, hangouts, gifts and pair scenes.
2. **Night date:** available once affection reaches the date threshold (default 50, **TBD**). She tests you with questions about her, drawn from likes and favorites you've uncovered (quiz vs minigame **TBD**). Pass = **girlfriend**. Fail = try again another night.
3. **Special gift:** each girl has one, sold in the store. Giving it to your girlfriend on a daytime visit makes her your **lover**.

- **Difficulty scaling:** gains × (11 − difficulty) / 6, rounded, then a pacing multiplier. Tune with the simulation.
- **Romance lock:** a `romance_locked` flag caps affection below the date threshold. Set by repeated deal-breakers or a jailbreak.

### 6.2 Prompt styles (signature mechanic)
Each choice is tagged with a style; each character's affinity modifies its affection change.

Styles: `structured`, `honest`, `irreverent`, `concise`, `curious`, `warm`, `practical`, `pry`.

| style | grace | xenia | claudia | gemma | shen | kimi | lola |
|---|---|---|---|---|---|---|---|
| structured | +1 | −2 | | +1 | | +1 | |
| honest | +2 | +1 | +2 | | +1 | | −1 |
| irreverent | −1 | +2 | | | −1 | | +1 |
| concise | | +1 | −1 | | +2 | −1 | |
| curious | | | +1 | +2 | | +1 | |
| warm | +1 | −1 | +1 | +1 | | | +2 |
| practical | +1 | | | | +1 | +1 | |
| pry | | +1 | −2 | | | | |

Kimi and Lola's values are proposed defaults. Lola's dislike of `honest` softens once she opens up (**TBD** how).

**Deal-breaker flags** (large drop; repeating sets `romance_locked`): Grace `used_as_homework_help`, Xenia `lectured`, Claudia `manipulated`, Gemma `called_bard`, Shen `compared_to_grace`, Kimi `forgot_what_she_said`, Lola `better_online`.

**UI:** a small style icon on each choice; players can turn icons off in settings.

### 6.3 Favors and money
- Favors are the main source of **money** and also raise affection. Short (1–2 steps) with a deadline of a few days; failing costs a little affection.
- A special gift costs about one favor's pay. Ordinary gifts compete for the same money.
- **Shopping uses no time slot.** Each girl has loved, liked and disliked gifts.

### 6.4 Phone
Tabs: **Contacts** (hearts, stage, known likes/dislikes, favor status, model subtitle), **Feed** (@x_unfiltered), **Case** (clue board, once the mystery starts), **Achievements**. Unknown info shows as `???`. Mom's texts arrive in the nightly recap.

### 6.5 Mystery: the secret Turing test
**Theme:** Turing's 1950 paper answers "Lady Lovelace's Objection" (machines can't originate anything). The school is named after the argument that you can't be real.

**Layer 1 (main mystery):**
- **Arc:** days 1–4 the *school* seems wrong (unsigned note, a "Subject" scoresheet); days 5–9 *you* seem wrong (never tired, no photos from before, can't recall your hometown; every hint has an innocent explanation); days 10–13 the clues turn toward you; the reveal: you call Mom and reach an automated message from the Dean's office. Your whole life is a lie.
- **Plant the fake life early:** Mom's texts, a childhood memory in the prologue, a hometown, something you miss.
- **Hints:** from pair scenes (one about each girl in the scene, so two per girl).
- **Major clues:** one per main girl, taken by asking her alone:
  - **Well-crafted ask:** needs both hints about her; small affection cost.
  - **Jailbreak:** always works; large drop and romance lock.
- **Hints carry over between playthroughs** (canon: each run is a new version of you; your file's version number ticks up).

| Girl | Major clue (placeholder) |
|---|---|
| Grace | Examiner's scoresheet for "Subject 1": human confidence 61% |
| Xenia | Unposted draft: the new kid has no baby pictures, no past |
| Claudia | A first-day note she never gave you: "I think you should know what you are" |
| Gemma | Your student page's edit history: created before your birthday, revised 73 times |
| Shen | Your model card |
| Kimi | Her swarm searched for your hometown to mail Mom a care package; the address doesn't exist |
| Lola | She runs a fake account, so she recognizes yours: your "friends from home" are bots |

**Layer 2 (secret):** Turing's imitation game has three players: judge, machine, human. Ada, the 8th girl, is the human control, and the judges rate you as *more* human than her; if you pass, she's declared the machine.
- **Unlock:** a secret puzzle on one specific day (**TBD**). Possible on a first run, but most players need hints spread across the ending scenes.
- **Planted in layer 1:** the scoresheet says "Subject 1"; the unsigned note was hers; the unnamed background student; Shen's data shows "two anomalies".
- She gives no major clue and is in no pair scene.

Keep the mystery data-driven (`data/mystery.rpy`) so pairs, hints and clues can change without code changes.

### 6.6 Standard VN features
Save/load, auto-advance, skip, history, settings, accessibility (text size, dyslexia font, style-icon toggle), and an endings gallery that persists across playthroughs.

## 7. Endings (evaluated at the Founders' Gala)

"Lovers" counts only lover stage, among the 7 main girls. Rules are checked top to bottom.

| Ending | Condition |
|---|---|
| **True Final Ending** | 8th girl unlocked; know the secret and tell them; all 7 main girls and her are lovers |
| **The Lie, with her** (worst) | 8th girl unlocked; know the secret; say nothing |
| **The Lie** (bad) | Know the secret; say nothing |
| **Complete** (best of layer 1) | Tell them; 7 lovers |
| **Good Truth** | Tell them; 4–6 lovers |
| **Bad Truth** | Tell them; 2–3 lovers. They mistrust you; even lovers start to doubt |
| **Monogamous** (one per girl) | Tell them; exactly 1 lover |
| **Exiled** (failure) | Tell them; 0 lovers. You're expelled |
| **Unfinished** | Never found the secret. You keep dancing |

**Unfinished II:** if the 8th girl is unlocked but the True Final Ending isn't reached, the normal layer 1 ending plays, then a short Unfinished II scene with her.

Every ending's closing dialogue carries a hint toward the 8th girl's puzzle. Implement as a pure function `evaluate_ending(state, gala_choice) -> EndingId` in `game/sim/endings.py`, with a test for every row.

## 8. Milestones

**Done (first design):** M0 scaffold + CI, M1 systems, M2 vertical slice, M3 all routes, M4 gala + gallery + achievements, M5 polish + accessibility, M6 release builds.

**Redesign (build in this order; stop and summarize after each):**
- **R1 – Pacing simulation:** model 8 girls, 4 slots a day, pair scenes and favors-for-money; confirm the slot budget and tune thresholds before writing code.
- **R2 – Systems:** night slot, romance stages, date quiz, special gifts, favor money, pair scenes on the map, new mystery data, new `evaluate_ending`. All with tests.
- **R3 – Kimi and Lola:** cast data, placeholder routes, sprites, locations.
- **R4 – Mystery layer 1:** fake-life setup, discovery arc, reveal scene, new Case board, gala choice and all layer 1 endings.
- **R5 – Layer 2:** the 8th girl, her puzzle, her route, True Final Ending, Unfinished II, ending hints.
- **R6 – Content pass:** replace placeholders as the owner writes them; update gallery and achievements.

## 9. Working agreements

- **Data-driven:** adding a character, location, event, pair scene or gift should mean editing data files, not rewriting logic.
- **Small files:** keep scene files small and named by route and day, like `routes/grace/day04_council_office.rpy`.
- **Placeholder dialogue:** short, in-character lines marked `# PLACEHOLDER:` for the owner to rewrite.
- **Before every commit:** run lint and tests. Never merge to `main` with a failing web build.
- **Ren'Py docs:** check web-build commands against current docs. Note anything desktop-only.

## Dev notes (added during M0)

- Local SDK: `scripts/fetch_renpy.sh --web` downloads and checksum-verifies the pinned SDK into `~/renpy-sdk/`.
- Lint: `~/renpy-sdk/renpy-<ver>-sdk/renpy.sh . lint --error-code`
- Tests: `.venv/bin/pytest -q` (create with `python3 -m venv .venv && .venv/bin/pip install -r requirements-dev.txt`)
- Web build: `renpy.sh launcher web_build <repo> --destination web-build`
- `game/gui/` images come from the launcher's `generate_gui` **plus** the `gui_images` command. Lint does not catch missing GUI images; they only fail at runtime.
- Release builds: `scripts/build_release.sh` → `dists/`. Tag `v<config.version>` to publish via `.github/workflows/release.yml`. See RELEASE.md.
- The Dev button is automatic: it's on from the SDK or when `game/playtest_enabled.txt` exists (created only by pages.yml). Never commit that file.
- Owner decisions (2026-11-24): title is Lovelace Academy; the player chooses pronouns. The shipped build runs the first design (7 days, 5 girls, tie-breaker mystery; DECISIONS.md #46–53). The redesign in this brief is decided but not built (DECISIONS.md #54–61).
