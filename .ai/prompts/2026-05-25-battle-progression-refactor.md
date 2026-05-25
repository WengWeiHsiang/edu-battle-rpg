# Goal

Refactor the battle system into a multi-question educational combat system.

The game should use:
- multiple choice questions
- enemy grade scaling
- multi-question battles
- snake length as player level/HP

---

# Core Gameplay

Snake exploration
→ encounter enemy
→ enter battle
→ answer multiple questions
→ win or lose battle
→ return to exploration

---

# Battle System Refactor

Replace typed answers with multiple choice gameplay.

Requirements:
- keyboard selection
- fast response flow
- arcade pacing

Suggested controls:
- 1 / 2 / 3 / 4 keys
- optional arrow navigation

Do NOT require text typing.

---

# Multiple Choice System

Question format:

Question
+
4 answer options

Requirements:
- randomized correct answer position
- immediate feedback
- support future categories

---

# Enemy Grade System

Enemy difficulty should match school grade levels.

Example progression:

Slime:
- elementary school easy

Bat:
- elementary school advanced

Ghost:
- middle school

Wizard:
- high school

Boss:
- advanced mixed questions

---

# Multi-Question Battles

Battles should contain multiple questions.

Example:
- weak enemy: 1 question
- normal enemy: 2~3 questions
- boss: 5+ questions

Battle ends when:
- all questions answered
OR
- player fails too many times

---

# Snake Length System

Snake length represents:
- HP
- player level
- progression

Correct answers:
- increase snake length

Wrong answers:
- decrease snake length

Lose condition:
- snake length reaches zero

---

# UI Requirements

Battle UI should show:
- enemy name
- enemy grade level
- battle progress
- remaining questions
- snake HP/length
- multiple choice options

UI should feel:
- readable
- responsive
- arcade-like

---

# Architecture Rules

Keep:
- reusable question system
- separated battle logic
- modular enemy data

Do NOT:
- hardcode all questions in battle state
- tightly couple UI and gameplay logic

---

# Suggested Structures

systems/
    battle/
    question/
    difficulty/

data/
    enemies/
    question_sets/

ui/
    battle/

---

# Expected Result

Battles become:
- more engaging
- more strategic
- more educational
- better paced

The game should support future:
- English questions
- science questions
- multiplayer battles
- boss encounters
- online rankings