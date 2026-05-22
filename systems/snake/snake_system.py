from __future__ import annotations

from dataclasses import dataclass

from entities.snake import Snake


@dataclass
class SnakeSystem:
    cols: int
    rows: int
    speed: float = 9.0

    def __post_init__(self) -> None:
        self._move_timer = 0.0

    def update(self, snake: Snake, dt: float) -> bool:
        self._move_timer += dt
        moved = False
        step_interval = 1.0 / self.speed
        while self._move_timer >= step_interval:
            self._move_timer -= step_interval
            snake.step(self.cols, self.rows)
            moved = True
        return moved

