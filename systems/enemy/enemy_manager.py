from __future__ import annotations

import random
from dataclasses import dataclass


@dataclass(frozen=True)
class StationaryEnemy:
    enemy_id: str
    name: str
    x: int
    y: int
    max_hp: int
    attack: int


@dataclass
class RespawnTicket:
    delay: float


class EnemyManager:
    def __init__(self, cols: int, rows: int, min_enemies: int = 3) -> None:
        self.cols = cols
        self.rows = rows
        self.min_enemies = min_enemies
        self._rng = random.Random()
        self._id_seq = 0
        self.active_enemies: list[StationaryEnemy] = []
        self._respawn_tickets: list[RespawnTicket] = []

    def reset(self, blocked: set[tuple[int, int]]) -> None:
        self.active_enemies = []
        self._respawn_tickets = []
        while len(self.active_enemies) < self.min_enemies:
            self.active_enemies.append(self._spawn_one(blocked | self._occupied_positions()))

    def update(self, dt: float, blocked: set[tuple[int, int]]) -> None:
        next_tickets: list[RespawnTicket] = []
        for ticket in self._respawn_tickets:
            ticket.delay -= dt
            if ticket.delay <= 0 and len(self.active_enemies) < self.min_enemies:
                self.active_enemies.append(self._spawn_one(blocked | self._occupied_positions()))
            elif ticket.delay > 0:
                next_tickets.append(ticket)
        self._respawn_tickets = next_tickets

        while len(self.active_enemies) + len(self._respawn_tickets) < self.min_enemies:
            self._respawn_tickets.append(RespawnTicket(delay=self._rng.uniform(2.0, 5.0)))

    def find_collision(self, head: tuple[int, int]) -> StationaryEnemy | None:
        for enemy in self.active_enemies:
            if (enemy.x, enemy.y) == head:
                return enemy
        return None

    def remove_for_battle(self, enemy_id: str) -> StationaryEnemy | None:
        for idx, enemy in enumerate(self.active_enemies):
            if enemy.enemy_id == enemy_id:
                return self.active_enemies.pop(idx)
        return None

    def schedule_respawn(self) -> None:
        self._respawn_tickets.append(RespawnTicket(delay=self._rng.uniform(2.0, 5.0)))

    def _spawn_one(self, blocked: set[tuple[int, int]]) -> StationaryEnemy:
        for _ in range(200):
            x = self._rng.randint(0, self.cols - 1)
            y = self._rng.randint(0, self.rows - 1)
            if (x, y) not in blocked:
                return StationaryEnemy(
                    enemy_id=self._next_enemy_id(),
                    name=self._rng.choice(["Slime", "Bat", "Mush"]),
                    x=x,
                    y=y,
                    max_hp=self._rng.choice([18, 20, 22, 24]),
                    attack=self._rng.choice([4, 5, 6]),
                )
        return StationaryEnemy(
            enemy_id=self._next_enemy_id(),
            name="Slime",
            x=0,
            y=0,
            max_hp=18,
            attack=4,
        )

    def _occupied_positions(self) -> set[tuple[int, int]]:
        return {(enemy.x, enemy.y) for enemy in self.active_enemies}

    def _next_enemy_id(self) -> str:
        self._id_seq += 1
        return f"enemy-{self._id_seq}"

