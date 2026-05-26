# Goal

Refactor and polish the battle UI system.

Current problems:
- duplicate player/enemy labels still appear below HP bars
- Hero and enemy panels look too similar
- leftover legacy rendering logic still exists
- battle UI lacks clear visual hierarchy
- UI still feels prototype-like

The battle screen should feel:
- polished
- readable
- arcade-like
- visually distinct

---

# Required Fixes

## Remove Duplicate Label Rendering

Current issues:
- "Hero" still appears below player HP bar
- "Middle School Lv..." still appears below enemy HP bar

These labels are already rendered inside the info cards.

Find and remove:
- old draw_text calls
- duplicate label rendering
- legacy battle UI text rendering

Requirements:
- render labels only once
- keep titles inside info cards only
- remove obsolete rendering logic

---

# Refactor Battle Panel Themes

Player and enemy cards should use clearly different visual themes.

---

# Hero Panel Theme

Style:
- warm colors
- orange/gold accents
- brighter friendly appearance

Suggested:
- warm background
- orange border
- warm HP bar

---

# Enemy Panel Theme

Style:
- dangerous/cool colors
- green/purple/red accents

Suggested:
- darker enemy panel
- stronger border contrast
- enemy-specific visual identity

---

# UI Layout Requirements

Battle UI should:
- maintain clean spacing
- avoid overlapping text
- keep consistent padding
- improve readability

Information priority:
1. Question
2. Answer buttons
3. Enemy/player state

Avoid:
- debug-style rendering
- duplicated information
- flat monochrome appearance

---

# Architecture Rules

Create reusable theme constants.

Suggested:
ui/theme.py

Example:
- HERO_PANEL_COLORS
- ENEMY_PANEL_COLORS
- BORDER_COLORS
- HP_BAR_COLORS

Avoid:
- duplicated RGB values
- repeated rendering logic
- legacy UI code

---

# Cleanup Requirements

Remove obsolete:
- battle rendering code
- duplicate label systems
- unused UI drawing paths

The battle UI should have a single clean rendering flow.

---

# Expected Result

Battle screen should:
- no longer show duplicate labels
- clearly distinguish player and enemy
- feel visually polished
- improve gameplay readability
- maintain modular UI architecture