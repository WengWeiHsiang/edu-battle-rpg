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
        self.total_questions = 1
        self.answered_questions = 0
        self.correct_answers = 0
        self.wrong_answers = 0
        self.max_failures = 1

    def reset(
        self,
        enemy_data: dict[str, int | str] | None = None,
        *,
        total_questions: int = 1,
        max_failures: int = 1,
        player_hp: int = 4,
    ) -> None:
        player_hp = max(1, player_hp)
        self.player = Combatant(name="Hero", max_hp=player_hp, attack=1)
        if enemy_data:
            self.enemy = Combatant(
                name=str(enemy_data.get("name", "Slime")),
                max_hp=int(enemy_data.get("max_hp", 24)),
                attack=int(enemy_data.get("attack", 5)),
            )
        else:
            self.enemy = Combatant(name="Slime", max_hp=24, attack=5)
        self.turn_owner = "player"
        self.last_result = None
        self.total_questions = max(1, total_questions)
        self.answered_questions = 0
        self.correct_answers = 0
        self.wrong_answers = 0
        self.max_failures = max(1, max_failures)

    def apply_quiz_answer(self, is_correct: bool) -> TurnResult:
        if self.turn_owner != "player":
            raise RuntimeError("Quiz answer can only be applied on player turn")

        self.answered_questions += 1
        if is_correct:
            self.correct_answers += 1
            base = max(1, self.enemy.max_hp // self.total_questions)
            damage = self.enemy.take_damage(base)
            result = TurnResult("player", "enemy", damage, "Correct answer")
            self.turn_owner = "player"
        else:
            self.wrong_answers += 1
            damage = self.player.take_damage(1)
            result = TurnResult("enemy", "player", damage, "Wrong answer")
            self.turn_owner = "player"

        self.last_result = result
        if self.answered_questions >= self.total_questions and self.enemy.is_alive:
            self.enemy.hp = 0 if self.correct_answers > self.wrong_answers else self.enemy.hp
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
        if not self.player.is_alive or not self.enemy.is_alive:
            return True
        if self.wrong_answers >= self.max_failures:
            return True
        return self.answered_questions >= self.total_questions

    def winner(self) -> str | None:
        if self.wrong_answers >= self.max_failures:
            return "enemy"
        if self.answered_questions >= self.total_questions:
            return "player" if self.correct_answers > self.wrong_answers else "enemy"
        if self.player.is_alive and not self.enemy.is_alive:
            return "player"
        if self.enemy.is_alive and not self.player.is_alive:
            return "enemy"
        return None
