# Math4kids

Manim animations that explain, for kids, why powers turn adding into multiplying
and why logs turn multiplying back into adding (and why that is what "bits of
information" means).

Every chapter is narrated: the text is spoken by Google Translate text-to-speech
via `manim-voiceover`, so rendering needs an internet connection (the generated
speech is cached under `media/voiceovers/`). Animations run at a quarter speed
(`SLOWDOWN` in `scenes/theme.py`) and the full video holds a 10 second pause
between chapters (`CHAPTER_PAUSE`).

## Setup

System packages (Ubuntu):

```bash
sudo apt-get install -y ffmpeg build-essential python3-dev \
  libcairo2-dev libpango1.0-dev pkg-config \
  texlive texlive-latex-extra texlive-fonts-extra texlive-science dvisvgm
```

Python environment:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

## Rendering

Render one chapter (`-ql` draft, `-qh` final):

```bash
.venv/bin/manim -ql scenes/scene_01_doubling_box.py MagicDoublingBox
```

Render the whole story as a single video:

```bash
.venv/bin/manim -qh scenes/full_video.py PowersAndLogs
```

Videos land in `media/videos/...`, with an `.srt` subtitle file of the narration
next to each one.

For a file to share and play in QuickTime (H.264 + AAC, faststart):

```bash
./export_quicktime.sh PowersAndLogs.mov
```

A rendered copy (1080p60, ~16.5 min) is committed at
[`renders/PowersAndLogs.mov`](renders/PowersAndLogs.mov).

## Chapters

| File | Scene | Content |
| --- | --- | --- |
| `scenes/scene_00_intro.py` | `Intro` | title, the identity we are heading for |
| `scenes/scene_01_doubling_box.py` | `MagicDoublingBox` | 1 candy, 3 presses -> 8, 2 presses -> 4 |
| `scenes/scene_02_adding_presses.py` | `AddingPresses` | 3 presses then 2 more, 8 x 4 = 32, 2^(3+2) = 2^3 x 2^2 |
| `scenes/scene_02_adding_presses.py` | `AllTheTwos` | (2x2x2)x(2x2) = 2x2x2x2x2 |
| `scenes/scene_03_logs_undo.py` | `LogIsTheUndoButton` | the log as the undo button, 5 = 3 + 2 |
| `scenes/scene_03_logs_undo.py` | `WhyHartleyUsedLogs` | combining messages: possibilities multiply, bits add |
| `scenes/scene_06_messages.py` | `WhatPossibilitiesMean` | 8 doors vs 4 weathers: what "possibilities" counts, log 1 = 0 |
| `scenes/scene_06_messages.py` | `BitsAndCodes` | door codes 000..111, weather codes 00..11, k bits label 2^k |
| `scenes/scene_06_messages.py` | `SendingBothMessages` | both notes: 8 x 4 = 32 combos, 010 + 10 = 01010, the caveat |
| `scenes/scene_04_what_is_a_log.py` | `WhatIsALog` | "how many times do I multiply by 2?" |
| `scenes/scene_04_what_is_a_log.py` | `CuttingInHalf` | pizza 16 -> 8 -> 4 -> 2 -> 1 |
| `scenes/scene_05_guessing_game.py` | `GuessingGame` | yes/no questions over 16, 32, 1024 numbers |
| `scenes/scene_05_guessing_game.py` | `LogsAndDigits` | base-10 digit intuition |
| `scenes/scene_00_intro.py` | `Outro` | the two sides side by side |
| `scenes/full_video.py` | `PowersAndLogs` | all chapters in order |

Shared pieces live in `scenes/theme.py` (colors, text helpers, candies, the
`DoublingBox`, and the narrated `StoryScene` base class) and `scenes/pizza.py`.

To change the pacing, edit `SLOWDOWN` and `CHAPTER_PAUSE` in `scenes/theme.py`.
Narration lines are the `self.say("...")` blocks inside each chapter.
