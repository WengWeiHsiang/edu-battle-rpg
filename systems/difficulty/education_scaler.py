from __future__ import annotations

from dataclasses import dataclass


@dataclass
class DifficultySnapshot:
    level: int
    correct_streak: int
    wrong_streak: int


@dataclass
class EducationalDifficultyScaler:
    min_level: int = 1
    max_level: int = 8
    base_level: int = 1

    def __post_init__(self) -> None:
        self._level = self.base_level
        self._correct_streak = 0
        self._wrong_streak = 0

    def current_level(self, encounter_attack: int, combo_multiplier: int, snake_length: int) -> int:
        attack_bonus = max(0, (encounter_attack - 4) // 2)
        combo_bonus = max(0, combo_multiplier - 1)
        length_bonus = max(0, (snake_length - 4) // 3)
        raw = self._level + attack_bonus + combo_bonus + length_bonus
        return max(self.min_level, min(self.max_level, raw))

    def observe_answer(self, is_correct: bool) -> None:
        if is_correct:
            self._correct_streak += 1
            self._wrong_streak = 0
            if self._correct_streak >= 2:
                self._level = min(self.max_level, self._level + 1)
                self._correct_streak = 0
        else:
            self._wrong_streak += 1
            self._correct_streak = 0
            if self._wrong_streak >= 2:
                self._level = max(self.min_level, self._level - 1)
                self._wrong_streak = 0

    def snapshot(self) -> DifficultySnapshot:
        return DifficultySnapshot(
            level=self._level,
            correct_streak=self._correct_streak,
            wrong_streak=self._wrong_streak,
        )

    def reset(self) -> None:
        self._level = self.base_level
        self._correct_streak = 0
        self._wrong_streak = 0

