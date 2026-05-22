from __future__ import annotations

import random
from dataclasses import dataclass

from entities.quiz_orb import QuizOrb


@dataclass
class QuizOrbSystem:
    cols: int
    rows: int

    def __post_init__(self) -> None:
        self._rng = random.Random()

    def spawn(self, blocked: set[tuple[int, int]]) -> QuizOrb:
        while True:
            x = self._rng.randint(0, self.cols - 1)
            y = self._rng.randint(0, self.rows - 1)
            if (x, y) not in blocked:
                return QuizOrb(x=x, y=y)

