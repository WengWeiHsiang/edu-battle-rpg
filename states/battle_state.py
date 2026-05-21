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
        self.enemy_cooldown = 0.0
        self.encounter_enemy_id: str | None = None

    def on_enter(self) -> None:
        super().on_enter()
        pygame.key.start_text_input()
        encounter_data = self.game.services.world.consume_encounter()
        self.encounter_enemy_id = str(encounter_data.get("id")) if encounter_data else None
        self.battle.reset(encounter_data)
        self.answer_input.clear()
        self.enemy_cooldown = 0.0
        self.view.on_enter(self.battle.player, self.battle.enemy)
        self.current_question = None
        if not self.battle.is_finished() and self.current_question is None and self.battle.turn_owner == "player":
            self.current_question = self.quiz.generate_question()

    def on_exit(self) -> None:
        pygame.key.stop_text_input()
        super().on_exit()

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            self.push_state("pause")
            return

        if event.type not in (pygame.KEYDOWN, pygame.TEXTINPUT):
            return

        if self.battle.turn_owner != "player" or self.current_question is None:
            return

        self.answer_input.feed_event(event)
        submitted = self.answer_input.pop_submit()
        if submitted is not None:
            is_correct = self.quiz.validate_answer(self.current_question, submitted.text)
            self.battle.apply_quiz_answer(is_correct)
            self.view.show_feedback(is_correct)
            self.view.play_damage_flash("enemy" if is_correct else "player")
            self.answer_input.clear()
            if self.battle.turn_owner == "enemy" and not self.battle.is_finished():
                self.enemy_cooldown = 0.6
            if self.battle.turn_owner == "player" and not self.battle.is_finished():
                self.current_question = self.quiz.generate_question()

    def update(self, dt: float) -> None:
        self.view.update(dt, self.battle.player, self.battle.enemy)
        if self.battle.is_finished():
            winner = self.battle.winner()
            if winner == "player" and self.encounter_enemy_id:
                self.game.services.world.remove_enemy_by_id(self.encounter_enemy_id)
            if winner == "enemy":
                self.battle.player.hp = max(1, self.battle.player.max_hp // 2)
            self.transition_to("world")
            return

        if self.battle.turn_owner == "enemy":
            self.enemy_cooldown -= dt
            if self.enemy_cooldown <= 0:
                self.battle.run_enemy_turn()
                self.view.play_damage_flash("player")
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
            enemy_cooldown=max(0.0, self.enemy_cooldown),
        )
