from __future__ import annotations

from dataclasses import dataclass

from entities.combatant import Combatant


@dataclass
class TurnResult:
    actor: str
    target: str
    damage: int
    note: str


class BattleController:
    def __init__(self) -> None:
        self.player = Combatant(name="Hero", max_hp=30, attack=7)
        self.enemy = Combatant(name="Slime", max_hp=24, attack=5)
        self.turn_owner = "player"
        self.last_result: TurnResult | None = None

    def reset(self) -> None:
        self.player = Combatant(name="Hero", max_hp=30, attack=7)
        self.enemy = Combatant(name="Slime", max_hp=24, attack=5)
        self.turn_owner = "player"
        self.last_result = None

    def apply_quiz_answer(self, is_correct: bool) -> TurnResult:
        if self.turn_owner != "player":
            raise RuntimeError("Quiz answer can only be applied on player turn")

        if is_correct:
            damage = self.enemy.take_damage(self.player.attack)
            result = TurnResult("player", "enemy", damage, "Correct answer")
        else:
            damage = self.player.take_damage(self.enemy.attack)
            result = TurnResult("enemy", "player", damage, "Wrong answer")

        self.last_result = result
        self.turn_owner = "enemy" if self.enemy.is_alive and self.player.is_alive else self.turn_owner
        return result

    def run_enemy_turn(self) -> TurnResult:
        if self.turn_owner != "enemy":
            raise RuntimeError("Enemy turn can only run on enemy turn")

        damage = self.player.take_damage(self.enemy.attack)
        result = TurnResult("enemy", "player", damage, "Enemy attacked")
        self.last_result = result
        if self.player.is_alive and self.enemy.is_alive:
            self.turn_owner = "player"
        return result

    def is_finished(self) -> bool:
        return not self.player.is_alive or not self.enemy.is_alive

    def winner(self) -> str | None:
        if self.player.is_alive and not self.enemy.is_alive:
            return "player"
        if self.enemy.is_alive and not self.player.is_alive:
            return "enemy"
        return None
