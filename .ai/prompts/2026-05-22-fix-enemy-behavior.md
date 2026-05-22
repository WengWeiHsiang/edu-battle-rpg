# Goal

Fix enemy behavior to match the intended gameplay design.

Current implementation is incorrect.

Enemies currently:
- move around the map
- behave like active AI enemies
- do not respawn correctly

This is NOT the intended gameplay.

---

# Correct Design

Enemies are stationary encounter objects.

They should function like:
- encounter nodes
- battle triggers
- collectible danger objects

NOT moving AI enemies.

---

# Required Enemy Behavior

## Stationary

Enemies must:
- remain fixed in position
- never roam
- never chase player
- never use movement AI

Remove:
- roaming logic
- velocity updates
- random movement
- pathfinding

---

# Encounter Behavior

When snake collides with enemy:
- trigger battle screen
- temporarily remove enemy from world

After battle:
- if enemy defeated:
    remove enemy
    start respawn timer
- if player loses:
    enemy may remain removed or respawn later

---

# Respawn Rules

The world should maintain a minimum number of enemies.

Requirements:
- defeated enemies respawn after delay
- random spawn positions
- avoid spawning on player
- avoid overlapping enemies

Suggested:
- minimum enemies: 3
- respawn delay: 2~5 seconds

---

# Enemy Manager

Create or refactor an enemy manager.

Responsibilities:
- maintain active enemy list
- handle spawn timers
- remove defeated enemies
- respawn enemies

Suggested structure:

systems/
    enemy_spawn/
    enemy_manager.py

---

# Architecture Rules

Keep:
- modular enemy systems
- clear enemy lifecycle
- separated spawn logic

Do NOT:
- hardcode enemy creation in battle state
- mix movement logic into stationary enemies
- create enemy AI systems

---

# Expected Result

After implementation:
- enemies remain stationary
- enemies correctly trigger battles
- defeated enemies respawn
- world always contains enemies
- gameplay matches snake exploration design