from __future__ import annotations

from dataclasses import dataclass, field


Direction = tuple[int, int]


@dataclass
class Snake:
    segments: list[tuple[int, int]]
    direction: Direction = (1, 0)
    pending_growth: int = 0
    min_length: int = 1
    _queued_direction: Direction | None = field(default=None, init=False)

    @classmethod
    def create(cls, x: int, y: int, length: int = 4) -> "Snake":
        body = [(x - i, y) for i in range(length)]
        return cls(segments=body)

    @property
    def head(self) -> tuple[int, int]:
        return self.segments[0]

    @property
    def length(self) -> int:
        return len(self.segments)

    def set_direction(self, direction: Direction) -> None:
        if direction == (0, 0):
            return
        if direction[0] == -self.direction[0] and direction[1] == -self.direction[1]:
            return
        self._queued_direction = direction

    def step(self, cols: int, rows: int) -> None:
        if self._queued_direction is not None:
            self.direction = self._queued_direction
            self._queued_direction = None

        hx, hy = self.head
        dx, dy = self.direction
        next_head = ((hx + dx) % cols, (hy + dy) % rows)
        self.segments.insert(0, next_head)

        if self.pending_growth > 0:
            self.pending_growth -= 1
        else:
            self.segments.pop()

    def grow(self, amount: int = 1) -> None:
        self.pending_growth += max(0, amount)

    def shrink(self, amount: int = 1) -> None:
        for _ in range(max(0, amount)):
            if len(self.segments) > self.min_length:
                self.segments.pop()

