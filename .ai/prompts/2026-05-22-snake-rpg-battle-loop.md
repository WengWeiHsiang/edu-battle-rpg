# Goal

Refactor the project into a hybrid snake RPG game.

The gameplay loop should be:

Snake Exploration
→ Encounter Enemy
→ Enter Quiz Battle Screen
→ Correct Answer:
    snake grows
→ Wrong Answer:
    snake shrinks
→ Return To Exploration

The game should combine:
- snake movement
- encounter system
- educational quiz battles
- survival progression

---

# Core Gameplay

## Exploration Phase

Player controls a snake on the map.

Requirements:
- smooth snake movement
- wrap-around world
- roaming enemies
- collision detection

Suggested state:
- snake_world_state.py

---

## Encounter System

When snake collides with enemy:
- trigger transition effect
- enter battle state

Requirements:
- collision detection
- encounter animation
- state switching

Suggested system:
- systems/encounter/

---

## Battle Phase

Battle occurs in a separate battle screen.

Requirements:
- display enemy
- display question
- answer input
- feedback effects

Correct answer:
- enemy defeated
- snake gains length

Wrong answer:
- snake loses length

Suggested state:
- battle_state.py

---

# Snake Rules

Snake length represents:
- health
- progression
- survival status

Lose condition:
- snake length reaches zero

Snake should:
- wrap around walls
- preserve body after battles
- visually grow/shrink

---

# Enemy System

Enemies exist on the world map.

Requirements:
- roaming or idle movement
- encounter trigger
- future extensibility

Future support:
- stronger enemies
- bosses
- enemy types

---

# UI Requirements

## Exploration UI

Show:
- snake length
- score
- combo
- minimap-style readability

---

## Battle UI

Show:
- enemy sprite
- question panel
- answer box
- battle feedback

Battle UI should feel:
- clean
- arcade-like
- responsive

Do NOT use giant RPG menus.

---

# Architecture Rules

Keep modular architecture.

Separate:
- world logic
- battle logic
- rendering
- quiz system

Do NOT:
- place everything in main.py
- create giant state files
- tightly couple systems

Keep:
- reusable states
- reusable entities
- reusable UI components

---

# Suggested Structure

states/
    snake_world_state.py
    battle_state.py
    transition_state.py

entities/
    snake.py
    enemy.py

systems/
    encounter/
    snake/
    battle/
    quiz/

ui/
    battle/
    hud/
    popup/

---

# Expected Result

Player can:
- move as snake
- encounter enemies
- enter quiz battle scenes
- grow on success
- shrink on failure
- continue survival gameplay

The game should feel:
- fast
- readable
- addictive
- expandable