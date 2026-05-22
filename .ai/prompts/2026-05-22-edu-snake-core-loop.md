# Goal

Pivot the project from RPG battle prototype into a real-time educational snake survival game.

The game should focus on fast gameplay, quiz-based growth, and survival mechanics.

---

# Core Gameplay Loop

Move
→ collect quiz orb
→ answer question
→ correct:
    snake grows
    score increases
    combo increases
→ wrong:
    snake shrinks
    combo resets
→ survive

---

# World Rules

- snake can wrap through walls
- game never pauses completely
- gameplay should feel fast and arcade-like
- snake length represents player HP/life

Lose condition:
- snake length reaches zero

---

# Required Systems

## Snake System

Create:
- snake movement
- body growth
- body shrinking
- wrap-around world movement

Suggested structure:
- systems/snake/
- entities/snake.py

---

## Quiz Orb System

Create collectible quiz objects.

Requirements:
- random spawning
- collision detection
- trigger answer input
- support future question categories

Suggested structure:
- systems/quiz/
- entities/quiz_orb.py

---

## Quiz Input System

Create lightweight answer input UI.

Requirements:
- non-blocking input
- fast answer flow
- short feedback popup
- keyboard-friendly

Correct:
- growth
- score
- combo

Wrong:
- shrink

Do NOT use full-screen battle transitions.

---

## Combo System

Create combo scoring.

Requirements:
- consecutive correct answers increase combo
- combo multiplier affects score
- combo resets on wrong answer

Suggested structure:
- systems/combo/

---

## Enemy System

Create simple enemies in the world.

Requirements:
- roaming enemies
- collision danger
- future combat extensibility

Enemies should NOT trigger separate battle scenes.

Combat should remain real-time.

---

# UI Requirements

The game should feel:
- arcade-like
- readable
- responsive

UI should include:
- score
- combo
- snake length
- current question

Do NOT create cluttered RPG menus.

---

# Architecture Rules

Keep modular architecture.

Do NOT:
- create massive files
- mix rendering and gameplay logic
- hardcode game rules inside main loop

Keep:
- reusable systems
- reusable entities
- reusable UI widgets

---

# Expected Result

After implementation:
- player controls snake smoothly
- snake wraps around walls
- quiz system integrates into gameplay loop
- correct answers reward growth
- wrong answers punish mistakes
- gameplay feels fast and addictive

The architecture should support future:
- multiplayer
- AI-generated questions
- powerups
- bosses
- desktop pet mode
- plugin game modes