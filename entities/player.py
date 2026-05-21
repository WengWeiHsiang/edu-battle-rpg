from __future__ import annotations

from dataclasses import dataclass

import pygame


@dataclass
class Player:
    x: float
    y: float
    speed: float = 180.0
    size: int = 20

    def move(self, dx: float, dy: float, dt: float, bounds: pygame.Rect) -> None:
        self.x += dx * self.speed * dt
        self.y += dy * self.speed * dt
        self.x = max(bounds.left, min(bounds.right - self.size, self.x))
        self.y = max(bounds.top, min(bounds.bottom - self.size, self.y))

    @property
    def rect(self) -> pygame.Rect:
        return pygame.Rect(int(self.x), int(self.y), self.size, self.size)
