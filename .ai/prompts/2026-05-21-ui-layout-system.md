# Goal

Refactor the UI architecture into reusable layout panels and widgets.

The current battle screen layout is messy and difficult to scale.

---

# Requirements

Create:
- reusable UI panels
- reusable widgets
- basic layout system

Suggested structure:

ui/
  panels/
  widgets/
  layout/

---

# UI Components

Required widgets:
- Label
- InputBox
- HPBar
- MessageBox

Required panels:
- BattlePanel
- QuestionPanel
- StatusPanel

---

# Layout Rules

Do NOT hardcode scattered x/y values everywhere.

Use:
- anchors
- containers
- relative positioning

---

# Architecture Rules

- rendering separated from game logic
- reusable UI
- no massive files
- prepare for future plugin game modes

---

# Expected Result

- cleaner battle screen
- reusable UI
- easier future feature expansion
- improved visual hierarchy