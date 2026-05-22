# Goal

Refactor the battle input system and improve the battle UI responsiveness and game feel.

The current gameplay feels laggy and visually unappealing.

The objective is to make the game feel closer to a real game instead of a prototype tool.

---

# Context

Current stack:
- Python
- pygame
- modular architecture
- state-driven game flow

Current systems:
- BattleState
- Question system
- Monster HP
- Basic answer input

Problems:
- keyboard input feels laggy
- UI feedback is weak
- game loop and input handling are tightly coupled
- battle screen lacks visual hierarchy

---

# Requirements

## Input System

Create a dedicated input handling layer.

Requirements:
- InputBuffer class
- non-blocking text input
- proper backspace handling
- enter key submit event
- decouple pygame events from battle logic
- battle state should not directly process raw keyboard input

Suggested structure:
- systems/input/
- ui/widgets/input_box.py

---

## UI Improvements

Improve visual quality with lightweight effects.

Requirements:
- semi-transparent UI panel
- text shadow rendering
- animated HP bar
- damage flash effect
- answer feedback text:
  - Correct
  - Wrong
- improve spacing and alignment

Do NOT add heavy assets yet.

Use simple shapes/colors/effects only.

---

## Architecture Rules

Must follow modular architecture.

Do NOT:
- place rendering logic inside game logic
- mix battle logic with pygame event polling
- create massive files
- hardcode future content

Keep:
- systems separated
- UI reusable
- state machine clean

---

# Expected Result

After refactor:
- input feels responsive
- battle loop is smoother
- UI looks more game-like
- architecture becomes cleaner
- future animation system can be added easily

---

# Files Likely Affected

- states/battle_state.py
- systems/input/
- ui/
- core/

