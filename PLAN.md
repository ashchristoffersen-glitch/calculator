# Kids Calculator — Build Plan

A fun, colorful calculator web app for a 6-year-old to use on an iPad.
Includes a **Calculator** and a **Game Mode** (missing-number equations).

---

## Goal

A simple, playful calculator that a young child can use and enjoy, PLUS a fun
game mode for practicing math with missing-number equations. It runs as a web
page (opens in Safari on the iPad — no app store, no install). There are two
parts: the **Calculator** and the **Game Mode**. Build the calculator first,
then the game.

## Who it's for

A 6-year-old child, used on an iPad in the Safari browser. Design for little
fingers and a fun, encouraging feel.

---

## Core requirements (must-have)

1. **Operations:** addition (+), subtraction (−), multiplication (×), division (÷) only.
2. **No** scientific functions. **No** percentage (%) button.
3. **Show the whole calculation on screen.** As the child types, the full
   expression stays visible, e.g. `12 + 7` shows on screen together.
   - Do NOT clear or hide the first number when the second number is entered
     (unlike many calculators that blank the screen). The running expression
     must remain visible until `=` is pressed.
4. When `=` is pressed, show the result clearly (e.g. `12 + 7 = 19`).
5. A **clear button** (C or AC) to start over.
6. Works well with **touch** on an iPad (taps, not just mouse clicks).

## Fun & engaging requirements

- **Theme:** colorful and playful — bright, cheerful colors. No specific
  character theme (not animals/space/etc.), just vibrant and friendly.
- **Big kid-friendly buttons:** extra-large buttons sized for little fingers.
- **Button animations:** buttons bounce/wiggle when tapped so it feels alive.
- **Sound effects:** a cheerful beep/boop when buttons are pressed, and a happy
  sound when `=` is pressed.
- **Celebration on answer:** confetti or sparkles pop up when `=` is pressed.

## Technical notes for the builder (Devin)

- Build as a **single self-contained web page** (`index.html`) with HTML, CSS,
  and JavaScript. Keep it simple — no build tools, no frameworks required.
- Must run by simply opening the file in a browser (and on iPad Safari).
- Make it **responsive** so it fills the iPad screen nicely in both portrait
  and landscape.
- Prevent iPad annoyances: disable text selection/zoom-on-double-tap on buttons,
  and stop the screen from scrolling/bouncing during use.
- Sounds can be generated in-browser (e.g. Web Audio API) or small audio files —
  builder's choice, but keep it lightweight.

---

## Build plan with checkpoints

Devin should STOP at each checkpoint, share the current `index.html`, and wait
for the parent to try it on the iPad and approve before continuing.

### Checkpoint 1 — Working calculator (no styling yet)
- Build the calculator logic: +, −, ×, ÷, and `=`.
- The full expression stays on screen as numbers are typed (requirement #3).
- Clear button works.
- Plain/basic appearance is fine at this stage.
- ✅ **Check:** Parent confirms the math works and the expression stays visible.

### Checkpoint 2 — Colorful, kid-friendly look
- Apply the bright, playful color theme.
- Make buttons extra-large and easy to tap on iPad.
- Make it responsive (portrait + landscape).
- ✅ **Check:** Parent confirms it looks fun and is easy to tap on the iPad.

### Checkpoint 3 — Animations & sounds
- Add button bounce/wiggle animations on tap.
- Add cheerful button-press sounds and a happy `=` sound.
- ✅ **Check:** Parent confirms it feels lively and the sounds are pleasant
  (and not annoying / too loud).

### Checkpoint 4 — Celebration
- Add confetti/sparkles when `=` is pressed.
- Final polish and a pass for iPad touch behavior.
- ✅ **Check:** Parent confirms the full experience is fun and works on the iPad.

> The calculator is now done. The next checkpoints build the **Game Mode**.

### Checkpoint 5 — Game logic (one mode, plain look)
- Add a way to switch from the Calculator to the Game.
- Build the **Plus** mode only: generate missing-number addition equations,
  let the child type the answer, and check it (correct/wrong).
- Vary the missing-number position (first / middle / result).
- Use a default level for now. Plain appearance is fine.
- ✅ **Check:** Parent confirms the addition questions work and answers check
  correctly.

### Checkpoint 6 — All 5 modes + level rules
- Add the other modes: **Minus, Times, Divide, Mixed**.
- Apply the math safety rules: subtraction never negative, division always even,
  whole numbers only.
- ✅ **Check:** Parent confirms all 5 modes generate sensible, correct questions.

### Checkpoint 7 — Settings & difficulty levels
- Add the **Settings** screen with the 1–10 level control.
- Wire the level into the number ranges (per the level table).
- Remember the chosen level between sessions (local storage).
- ✅ **Check:** Parent confirms changing the level makes questions easier/harder
  and the setting sticks.

### Checkpoint 8 — Game fun & rewards
- Apply the colorful/playful style and big buttons to the game.
- Add celebration + happy sound on correct, gentle "try again" on wrong.
- Add score/stars and a streak counter, plus encouraging messages.
- Add **badges & achievements**: award pop-ups, saved badges, and a
  badge/trophy area to revisit (see "Gamification" above).
- Final iPad touch polish.
- ✅ **Check:** Parent confirms the game is fun, rewarding, and works on the iPad.

---

## Game Mode

A math-practice game where the child solves equations with a **missing number**
and **types in the answer**.

### How it works

- The game shows an equation with one number missing, e.g. `547 + ___ = 652`.
- The child **types the missing number** (using an on-screen number pad) and
  submits to check.
- The missing number can be in **different positions** to keep it interesting:
  - missing middle number: `547 + ___ = 652`
  - missing first number: `___ + 105 = 652`
  - missing result: `547 + 105 = ___`
- After each answer, give immediate feedback (correct → celebrate; wrong →
  gentle "try again", let him retry).
- Aim it at a capable 6-year-old — equations can be genuinely challenging
  (multi-digit), not just `6 + 2`. The difficulty is controlled by the Level
  (see below).

### The 5 game modes

A mode-select screen lets the child pick one of:

1. **Plus** — all addition (`+`) questions
2. **Minus** — all subtraction (`−`) questions
3. **Times** — all multiplication (`×`) questions
4. **Divide** — all division (`÷`) questions
5. **Mixed** — a random mix of all four

### Difficulty levels (1–10)

- There are **10 levels**. The level controls how big the numbers get.
- The level is changed in a **Settings** screen (e.g. a slider or +/− stepper
  from 1 to 10). The chosen level should be remembered between sessions
  (save it in the browser's local storage).
- **Any level can be freely chosen at any time.** The child does NOT have to
  finish or "complete" one level to access another — he can jump straight to any
  level (e.g. from 2 to 7, or back down) whenever he likes. There is no locking
  or unlocking of levels.
- Suggested scaling for the level (Devin may fine-tune, but keep this spirit —
  Level 1 easy, Level 10 hard):

  | Level | + and − number range | × and ÷ number range |
  |-------|----------------------|----------------------|
  | 1     | 1–10                 | factors 1–5          |
  | 2     | 1–20                 | factors 1–10         |
  | 3     | 1–50                 | factors 1–12         |
  | 4     | 1–100                | 2-digit × 1-digit    |
  | 5     | 1–200                | 2-digit × 1-digit    |
  | 6     | 1–500                | 2-digit × 2-digit    |
  | 7     | 1–1,000              | 2-digit × 2-digit    |
  | 8     | 1–2,000              | 3-digit × 1-digit    |
  | 9     | 1–5,000              | 3-digit × 2-digit    |
  | 10    | 1–10,000             | 3-digit × 2-digit    |

### Important math rules (must follow)

- **Subtraction never goes negative.** Always arrange so the result is ≥ 0
  (e.g. bigger number minus smaller number).
- **Division always comes out even** (no remainders/decimals). Generate division
  questions as the reverse of a multiplication so the answer is a whole number.
- All answers are **whole numbers** (no decimals in the game).

### Rewards & feedback (fun factor)

- Correct answer → **celebration** (confetti/sparkles) + a happy sound, and an
  encouraging message ("Great job!", "You got it!").
- Wrong answer → gentle, friendly message ("Try again!") and let him retry — no
  scary red X or harsh sounds.
- Show a **score / star count** for correct answers and a **streak counter**
  ("3 in a row!") to keep him motivated.
- A "Next question" button (or auto-advance after the celebration).

### Gamification — badges & achievements

- The child earns **badges/achievements** for accomplishments, shown as a
  pop-up award with a celebration when unlocked.
- Suggested badges (Devin may add more in the same spirit):
  - **Streak badges** — e.g. "5 in a Row!", "10 in a Row!"
  - **Mode mastery** — e.g. "Addition Master", "Subtraction Star",
    "Times Champion", "Division Hero" for getting many right in a mode.
  - **Level badges** — e.g. "Level 5 Champion" for doing well at a level.
  - **Milestones** — e.g. "10 Correct", "50 Correct", "100 Correct".
- Earned badges are **saved** (local storage) and shown in a simple
  **badge/trophy area** the child can revisit to see what he's collected.
- Keep it positive: badges are only ever earned, never lost.

### Navigation

- A clear way to switch between **Calculator** and **Game** (e.g. a button or
  tab at the top), and to reach **Settings**.
- Buttons big and easy to tap on the iPad, same colorful/playful style as the
  calculator.

---

## Out of scope (for now)

- Percentage, scientific functions, memory buttons.
- Anything beyond +, −, ×, ÷ in the calculator.
- Decimals/fractions in the game (whole numbers only).

---

## Definition of done

**Calculator:**
- Checkpoints 1–4 approved by the parent.
- The whole calculation is always visible while typing.
- Colorful, big buttons, animations, happy sounds, celebration on the answer.

**Game Mode:**
- Checkpoints 5–8 approved by the parent.
- All 5 modes work (Plus, Minus, Times, Divide, Mixed).
- Missing-number equations with typed answers; missing number appears in
  different positions.
- 10 difficulty levels adjustable in Settings; the level is remembered.
- Math rules hold: no negative subtraction, even division, whole numbers only.
- Rewards work: celebration + sound, score/stars, streak, encouraging messages.
- Badges & achievements are earned, saved, and viewable in a badge/trophy area.

**Both:**
- Run smoothly on the iPad in Safari, with easy navigation between Calculator,
  Game, and Settings.
