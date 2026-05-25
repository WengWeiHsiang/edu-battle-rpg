# Goal

Implement progressive educational difficulty scaling.

Enemy behavior should remain simple and stationary.

Game difficulty should increase through harder questions instead of harder movement mechanics.

---

# Core Design

The game loop should focus on:
- snake survival
- quiz battles
- educational progression

Enemies should:
- remain stationary
- act as encounter objects
- not require advanced AI

Question difficulty should scale over time.

---

# Difficulty Scaling System

Create a modular difficulty system.

Suggested structure:

systems/
    difficulty/
        difficulty_manager.py
        math_scaling.py
        english_scaling.py

---

# Math Difficulty Progression

## Early Game

Simple arithmetic:
- addition
- subtraction

Examples:
- 3 + 5
- 7 - 2

---

## Mid Game

Intermediate arithmetic:
- multiplication
- division
- larger numbers

Examples:
- 12 × 8
- 144 ÷ 12

---

## Late Game

Advanced questions:
- fractions
- equations
- word problems

Examples:
- solve for x
- percentage questions

---

# Difficulty Rules

Difficulty should scale using:
- elapsed time
- score
- combo
- enemies defeated

Do NOT hardcode progression directly inside battle_state.py.

---

# Enemy System

Enemies should:
- remain stationary
- spawn randomly
- act as quiz encounter triggers

No advanced pathfinding required.

---

# Architecture Rules

Keep:
- reusable question generators
- separated scaling logic
- future support for categories

Do NOT:
- tightly couple question generation to UI
- hardcode all questions in one file

---

# Future Support

The system should support:
- English questions
- Science questions
- AI-generated questions
- difficulty presets
- multiplayer balancing

---

# Expected Result

As gameplay progresses:
- questions become harder
- gameplay remains readable
- challenge increases naturally
- educational progression feels rewarding