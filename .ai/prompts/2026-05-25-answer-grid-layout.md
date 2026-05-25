# Goal

Refactor the battle answer UI into a 2x2 grid layout.

Current vertical answer list causes:
- layout overflow
- excessive height usage
- poor readability
- weak game feel

The answer system should feel like a polished arcade battle interface.

---

# Required Layout

Replace vertical answer list:

1.
2.
3.
4.

with a 2x2 answer grid:

[1] [2]
[3] [4]

---

# Layout Rules

Requirements:
- equal button sizes
- proper spacing
- centered alignment
- responsive scaling

Buttons should:
- avoid overflow
- fit battle panel
- remain readable

---

# Interaction

Support:
- mouse click
- keyboard shortcuts 1~4

Hover effects required.

---

# Suggested Layout

Battle Panel:

Question Area
↓
2x2 Answer Grid

---

# Visual Style

Buttons should feel:
- arcade-like
- responsive
- clean
- modern

Avoid:
- HTML form appearance
- giant text walls
- uneven spacing

---

# Technical Requirements

Create reusable UI component.

Suggested structure:

ui/
    battle/
        answer_grid.py
        answer_button.py

Avoid hardcoding positions directly in battle_state.py.

---

# Expected Result

Battle UI becomes:
- cleaner
- easier to read
- easier to click
- visually balanced
- more game-like