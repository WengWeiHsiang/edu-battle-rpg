from __future__ import annotations

from dataclasses import dataclass, field

from entities.enemy import Enemy
from entities.player import Player


@dataclass
class WorldSession:
    player: Player = field(default_factory=lambda: Player(x=100, y=260))
    enemies: list[Enemy] = field(default_factory=list)
    pending_encounter: dict[str, int | str] | None = None

    def __post_init__(self) -> None:
        if not self.enemies:
            self.enemies = [
                Enemy(enemy_id="slime-a", name="Slime", x=320, y=170, max_hp=24, attack=5),
                Enemy(enemy_id="bat-b", name="Bat", x=560, y=230, max_hp=20, attack=6),
                Enemy(enemy_id="mush-c", name="Mush", x=700, y=140, max_hp=28, attack=4),
            ]

    def begin_encounter(self, enemy: Enemy) -> None:
        self.pending_encounter = enemy.to_battle_data()

    def consume_encounter(self) -> dict[str, int | str] | None:
        data = self.pending_encounter
        self.pending_encounter = None
        return data

    def resolve_battle(self, winner: str) -> None:
        if winner == "player":
            active_id = None
            if self.pending_encounter:
                active_id = self.pending_encounter.get("id")
            if active_id:
                self.enemies = [enemy for enemy in self.enemies if enemy.enemy_id != active_id]

    def remove_enemy_by_id(self, enemy_id: str) -> None:
        self.enemies = [enemy for enemy in self.enemies if enemy.enemy_id != enemy_id]
