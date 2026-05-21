# Goal

Expand the game from a single battle screen into a world exploration RPG loop.

The player should be able to move around the world and trigger battles by colliding with enemies.

---

# Required Gameplay Loop

World Exploration
→ Enemy Encounter
→ Transition Effect
→ Battle Scene
→ Battle End
→ Return To World

---

# New Systems

## WorldState

Create a new world exploration state.

Responsibilities:
- player movement
- map rendering
- enemy roaming
- collision detection
- encounter triggering

Suggested file:
- states/world_state.py

---

## Player Entity

Create a reusable player entity.

Requirements:
- movement
- position
- sprite
- collision box

Suggested structure:
- entities/player.py

---

## Enemy Entity

Create world enemies.

Requirements:
- world position
- simple roaming or idle movement
- collision detection
- encounter trigger

Suggested structure:
- entities/enemy.py

---

## Battle Transition

Create a transition system between world and battle.

Examples:
- fade
- flash
- zoom
- screen wipe

Suggested structure:
- systems/transition/

Do NOT directly switch instantly.

---

## State Manager

Refactor state management to support:
- push state
- pop state
- change state

BattleState should receive:
- enemy data
- encounter context

---

# Architecture Rules

Keep modular architecture.

Do NOT:
- hardcode world logic into BattleState
- mix rendering and gameplay logic
- create giant main.py files

Keep:
- reusable systems
- separated states
- reusable entities

---

# Visual Requirements

World mode should include:
- visible player character
- enemy sprites on map
- simple background or tile map

Battle mode should remain separate from world rendering.

---

# Expected Result

Player can:
- move around the map
- collide with enemies
- enter battle scene
- finish battle
- return to world

The architecture should support future:
- NPC
- farming
- desktop pet mode
- plugin game modes