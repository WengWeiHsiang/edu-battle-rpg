from __future__ import annotations

from dataclasses import dataclass, field
import random

import pygame


@dataclass
class Enemy:
    enemy_id: str
    name: str
    x: float
    y: float
    max_hp: int
    attack: int
    size: int = 18
    roam_timer: float = 0.0
    vx: float = field(default_factory=lambda: random.uniform(-1.0, 1.0))
    vy: float = field(default_factory=lambda: random.uniform(-1.0, 1.0))

    def update(self, dt: float, bounds: pygame.Rect) -> None:
        self.roam_timer -= dt
        if self.roam_timer <= 0:
            self.roam_timer = random.uniform(0.6, 1.8)
            self.vx = random.uniform(-1.0, 1.0)
            self.vy = random.uniform(-1.0, 1.0)

        speed = 75.0
        self.x += self.vx * speed * dt
        self.y += self.vy * speed * dt

        if self.x < bounds.left or self.x > bounds.right - self.size:
            self.vx *= -1
        if self.y < bounds.top or self.y > bounds.bottom - self.size:
            self.vy *= -1

        self.x = max(bounds.left, min(bounds.right - self.size, self.x))
        self.y = max(bounds.top, min(bounds.bottom - self.size, self.y))

    @property
    def rect(self) -> pygame.Rect:
        return pygame.Rect(int(self.x), int(self.y), self.size, self.size)

    def to_battle_data(self) -> dict[str, int | str]:
        return {"id": self.enemy_id, "name": self.name, "max_hp": self.max_hp, "attack": self.attack}
