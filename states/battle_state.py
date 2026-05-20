from __future__ import annotations

import pygame

from states.base_state import BaseState
from ui.battle_view import BattleView
from ui.text_input import TextInputBuffer


class BattleState(BaseState):
    def __init__(self, game: "Game") -> None:
        super().__init__(game)
        self.view = BattleView()
        self.answer_input = TextInputBuffer()
        self.current_question = None
        self.battle = game.services.battle
        self.quiz = game.services.quiz
        self.enemy_cooldown = 0.0

    def on_enter(self) -> None:
        super().on_enter()
        self.answer_input.clear()
        self.enemy_cooldown = 0.0
        if not self.battle.is_finished() and self.current_question is None and self.battle.turn_owner == "player":
            self.current_question = self.quiz.generate_question()

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_p:
            self.transition_to("pause")
            return

        if self.battle.turn_owner != "player" or self.current_question is None:
            return

        if event.key == pygame.K_RETURN:
            is_correct = self.quiz.validate_answer(self.current_question, self.answer_input.text)
            self.battle.apply_quiz_answer(is_correct)
            self.answer_input.clear()
            if self.battle.turn_owner == "enemy" and not self.battle.is_finished():
                self.enemy_cooldown = 0.6
            if self.battle.turn_owner == "player" and not self.battle.is_finished():
                self.current_question = self.quiz.generate_question()
            return

        self.answer_input.handle_key(event)

    def update(self, dt: float) -> None:
        if self.battle.is_finished():
            winner = self.battle.winner()
            if winner == "player":
                self.transition_to("reward")
            else:
                self.transition_to("game_over")
            return

        if self.battle.turn_owner == "enemy":
            self.enemy_cooldown -= dt
            if self.enemy_cooldown <= 0:
                self.battle.run_enemy_turn()
                if not self.battle.is_finished():
                    self.current_question = self.quiz.generate_question()

    def render(self, surface: pygame.Surface) -> None:
        self.view.draw(
            surface=surface,
            player=self.battle.player,
            enemy=self.battle.enemy,
            turn_owner=self.battle.turn_owner,
            question_text=self.current_question.prompt if self.current_question else "",
            answer_text=self.answer_input.text,
            last_note=self.battle.last_result.note if self.battle.last_result else "",
        )
