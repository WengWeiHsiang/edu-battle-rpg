# Goal

Refactor the battle screen UI into a focused educational arcade combat interface.

Current issues:
- too much empty space
- weak visual hierarchy
- oversized HP bars
- question area feels cramped
- answer area lacks focus
- battle screen does not feel polished

The battle UI should prioritize:
- question readability
- answer interaction
- fast gameplay feedback

---

# New Layout Requirements

Battle screen should use 3 major zones:

1. Enemy Zone
2. Question Zone
3. Answer Zone

---

# Enemy Zone

Reduce vertical size.

Display:
- enemy sprite
- enemy name
- small HP bar
- enemy grade level

Do NOT let enemy UI dominate screen space.

---

# Question Zone

Question should become primary visual focus.

Requirements:
- centered layout
- large readable text
- strong spacing
- clean typography

The question should immediately attract player attention.

---

# Answer Zone

Use 2x2 answer grid.

Requirements:
- large clickable buttons
- equal sizing
- clean spacing
- hover feedback
- keyboard shortcuts

Buttons should feel:
- arcade-like
- responsive
- touch friendly

---

# Visual Hierarchy

Priority should be:

1. Question
2. Answers
3. Enemy
4. HP info

---

# UI Style

Target feel:
- arcade
- educational
- modern
- clean
- responsive

Avoid:
- giant empty sky
- debug UI
- oversized status bars
- text-wall appearance

---

# Feedback Effects

Correct answer:
- green flash
- button highlight
- combo popup
- smooth transition

Wrong answer:
- red flash
- shake effect
- HP reduction feedback

---

# Suggested Structure

ui/
    battle/
        battle_layout.py
        question_panel.py
        answer_grid.py
        battle_feedback.py

---

# Expected Result

Battle screen should feel:
- focused
- readable
- satisfying
- game-like
- polished

The player should immediately understand:
- the question
- the choices
- the battle state