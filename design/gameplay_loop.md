# Edu Snake Survivor

## Game Concept

A fast-paced educational arcade snake game.

Players survive by collecting quiz orbs and answering correctly.

Correct answers reward growth and power.
Wrong answers punish mistakes.

The game focuses on:
- fast gameplay
- readable UI
- addictive feedback loop
- educational reinforcement

---

# Core Gameplay Loop

Move
→ collect quiz orb
→ answer question
→ correct:
    grow
    gain score
    increase combo
→ wrong:
    shrink
    reset combo
→ survive

---

# Player Rules

- snake constantly moves
- player controls direction
- snake can wrap through walls
- snake length represents HP/life

Lose condition:
- snake length reaches zero

---

# Quiz Rules

Quiz orbs appear randomly on the map.

When collected:
- short answer prompt appears
- player types answer quickly

Correct answer:
- +1 body segment
- score increase
- combo increase

Wrong answer:
- lose body segment
- combo reset

---

# Combo System

Consecutive correct answers increase combo multiplier.

Higher combo:
- higher score
- future powerups
- possible bonus attacks

Combo resets on:
- wrong answer
- collision damage

---

# Enemy System

Enemies roam on the map.

Enemy collision may:
- damage player
- interrupt movement
- reduce snake length

Future:
- bosses
- ranged enemies
- elite enemies

Combat remains real-time.

No separate battle screen.

---

# World Rules

- wrap-around map
- increasing difficulty over time
- enemy spawn scaling
- faster gameplay progression

---

# Visual Direction

Style:
- pixel arcade
- readable UI
- clean layout
- strong gameplay feedback

Effects:
- hit flash
- combo popup
- floating score text
- screen shake

---

# Future Expansion

Planned future systems:
- multiplayer
- AI-generated questions
- desktop pet mode
- farming mode
- plugin mini-games
- online leaderboard
- co-op gameplay