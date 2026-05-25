# Goal

Refactor the battle UI into a clean multiple-choice interface.

Current issues:
- answer layout overflows
- keyboard input is unreliable
- UI feels like debug text
- options are difficult to interact with

The battle screen should feel like a polished arcade quiz battle system.

---

# Required Changes

## Replace Text List Options

Current:
1. answer
2. answer

Replace with:
- clickable answer buttons
- proper spacing
- centered layout
- readable typography

---

# Input System

Support BOTH:
- mouse click
- keyboard shortcuts (1~4)

Mouse should be primary interaction.

Keyboard remains optional for fast players.

---

# Button Requirements

Each answer option should:
- have hover effect
- have selected effect
- support click detection
- animate feedback

Suggested states:
- idle
- hover
- correct
- wrong

---

# Layout Rules

Battle UI must:
- avoid text overflow
- scale properly with screen size
- keep consistent margins
- separate question area from answer area

---

# Suggested Battle Layout

Top:
- enemy info
- HP bars

Middle:
- enemy sprite
- battle visuals

Bottom:
- question panel
- multiple choice buttons

---

# UI Style

Target feel:
- arcade
- educational
- polished
- readable

Avoid:
- debug-text appearance
- giant text walls
- cramped layouts

---

# Suggested Structure

ui/
    battle/
        answer_button.py
        battle_layout.py
        question_panel.py

systems/
    input/
        mouse_input.py

---

# Expected Result

Players can:
- click answers smoothly
- use keyboard shortcuts
- clearly read battle UI
- interact without layout bugs

Battle flow should feel:
- responsive
- modern
- game-like