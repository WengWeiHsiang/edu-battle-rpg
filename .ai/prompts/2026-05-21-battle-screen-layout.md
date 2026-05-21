# Goal

Refactor the battle screen layout and UI composition.

Current screen feels like a prototype/debug tool instead of a game.

---

# Problems

- layout feels scattered
- textbox dominates the screen
- no visual hierarchy
- enemy sprite too small
- panels feel disconnected
- too much empty space

---

# Requirements

## Layout

Use a structured battle layout:

Top:
- enemy area

Middle:
- player status

Bottom:
- question and answer area

Do NOT place UI with arbitrary scattered coordinates.

---

## UI Style

Use a consistent pixel RPG style:
- pixel borders
- darker outlines
- consistent padding
- limited color palette

---

## Input Box

Refactor answer input UI:
- smaller centered input box
- improve readability
- improve spacing

---

## Enemy Presentation

Improve enemy display:
- larger sprite scale
- shadow beneath enemy
- idle movement or floating effect

---

## Architecture

Keep:
- modular UI
- reusable panels/widgets
- rendering separated from battle logic

Do NOT:
- hardcode giant render functions
- place all rendering in BattleState

---

# Expected Result

- cleaner battle screen
- stronger visual focus
- better game feel
- easier future UI expansion