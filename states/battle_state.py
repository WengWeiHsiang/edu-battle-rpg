from __future__ import annotations

import pygame

from states.base_state import BaseState
from systems.input import InputBuffer
from ui.battle_view import BattleView


class BattleState(BaseState):
    def __init__(self, game: "Game") -> None:
        super().__init__(game)
        self.view = BattleView()
        self.answer_input = InputBuffer(max_length=32)
        self.current_question = None
        self.battle = game.services.battle
        self.quiz = game.services.quiz
        self.difficulty = game.services.difficulty
        self.world = game.services.world
        self.encounter_enemy_id: str | None = None
        self.encounter_attack: int = 4
        self.resolved = False

    def on_enter(self) -> None:
        super().on_enter()
        pygame.key.start_text_input()
        encounter_data = self.game.services.world.consume_encounter()
        self.encounter_enemy_id = str(encounter_data.get("id")) if encounter_data else None
        self.encounter_attack = int(encounter_data.get("attack", 4)) if encounter_data else 4
        self.battle.reset(encounter_data)
        self.answer_input.clear()
        self.resolved = False
        self.view.on_enter(self.battle.player, self.battle.enemy)
        difficulty = self.difficulty.current_level(
            encounter_attack=self.encounter_attack,
            combo_multiplier=self.world.combo_tracker.multiplier,
            snake_length=self.world.snake.length,
        )
        self.current_question = self.quiz.generate_question(difficulty=difficulty)

    def on_exit(self) -> None:
        pygame.key.stop_text_input()
        super().on_exit()

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            self.push_state("pause")
            return

        if event.type not in (pygame.KEYDOWN, pygame.TEXTINPUT):
            return

        if self.resolved or self.current_question is None:
            return

        self.answer_input.feed_event(event)
        submitted = self.answer_input.pop_submit()
        if submitted is not None:
            is_correct = self.quiz.validate_answer(self.current_question, submitted.text)
            self.difficulty.observe_answer(is_correct)
            self.view.show_feedback(is_correct)
            self.view.play_damage_flash("enemy" if is_correct else "player")
            self.game.services.world.apply_battle_result(self.encounter_enemy_id, is_correct)
            if is_correct:
                self.battle.enemy.hp = 0
            else:
                self.battle.player.hp = max(0, self.battle.player.hp - self.battle.enemy.attack)
            self.answer_input.clear()
            self.current_question = None
            self.resolved = True

    def update(self, dt: float) -> None:
        self.view.update(dt, self.battle.player, self.battle.enemy)
        if self.resolved:
            self.transition_to("world")

    def render(self, surface: pygame.Surface) -> None:
        self.view.draw(
            surface=surface,
            player=self.battle.player,
            enemy=self.battle.enemy,
            turn_owner="enemy" if self.resolved and self.battle.enemy.is_alive else "player",
            question_text=self.current_question.prompt if self.current_question else "",
            answer_text=self.answer_input.text,
            last_note=(
                f"Difficulty Lv{self.current_question.difficulty}"
                if self.current_question
                else "Answer to defeat enemy and return to map"
            ),
            enemy_cooldown=0.0,
        )
