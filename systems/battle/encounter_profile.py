from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class EncounterProfile:
    grade_label: str
    difficulty_offset: int
    question_count: int
    max_failures: int


class EncounterProfileService:
    def __init__(self, profile_path: str | None = None) -> None:
        root = Path(__file__).resolve().parents[2]
        self._profile_path = Path(
            profile_path) if profile_path else root / "data" / "enemies" / "grade_profiles.json"
        self._profiles = self._load_profiles()

    def build(self, enemy_name: str, snake_length: int) -> EncounterProfile:
        default = self._profiles.get("default", {})
        raw = self._profiles.get(enemy_name, default)

        question_min, question_max = self._parse_question_range(
            raw.get("question_count", [1, 1]))
        length_bonus = max(0, (snake_length - 4) // 4)
        question_count = min(question_max, question_min + length_bonus)

        return EncounterProfile(
            grade_label=str(
                raw.get("grade", default.get("grade", "Elementary Easy"))),
            difficulty_offset=int(
                raw.get("difficulty_offset", default.get("difficulty_offset", 0))),
            question_count=max(1, question_count),
            max_failures=max(
                1, int(raw.get("max_failures", default.get("max_failures", 1)))),
        )

    def _load_profiles(self) -> dict[str, dict]:
        with self._profile_path.open("r", encoding="utf-8-sig") as fh:
            data = json.load(fh)
        if not isinstance(data, dict):
            raise ValueError("grade profile data must be an object")
        return data

    @staticmethod
    def _parse_question_range(value: object) -> tuple[int, int]:
        if isinstance(value, list) and len(value) == 2:
            lo = int(value[0])
            hi = int(value[1])
            return (min(lo, hi), max(lo, hi))
        n = int(value) if value is not None else 1
        return (max(1, n), max(1, n))
