from __future__ import annotations

import pygame

from states.base_state import BaseState
from ui.battle_view import BattleView


class BattleState(BaseState):
    def __init__(self, game: "Game") -> None:
        super().__init__(game)
        self.view = BattleView()
        self.current_question = None
        self.battle = game.services.battle
        self.quiz = game.services.quiz
        self.difficulty = game.services.difficulty
        self.encounter_profiles = game.services.encounter_profiles
        self.world = game.services.world
        self.encounter_enemy_id: str | None = None
        self.encounter_attack: int = 4
        self.encounter_grade: str = "Elementary Easy"
        self.resolved = False

    def on_enter(self) -> None:
        super().on_enter()
        encounter_data = self.game.services.world.consume_encounter()
        self.encounter_enemy_id = str(encounter_data.get("id")) if encounter_data else None
        self.encounter_attack = int(encounter_data.get("attack", 4)) if encounter_data else 4
        enemy_name = str(encounter_data.get("name", "Slime")) if encounter_data else "Slime"
        profile = self.encounter_profiles.build(enemy_name, self.world.snake.length)
        self.encounter_grade = profile.grade_label
        self.battle.reset(
            encounter_data,
            total_questions=profile.question_count,
            max_failures=profile.max_failures,
            player_hp=self.world.snake.length,
        )
        self.resolved = False
        self.view.on_enter(self.battle.player, self.battle.enemy)
        base_difficulty = self.difficulty.current_level(
            encounter_attack=self.encounter_attack,
            combo_multiplier=self.world.combo_tracker.multiplier,
            snake_length=self.world.snake.length,
        )
        difficulty = max(1, base_difficulty + profile.difficulty_offset)
        self.current_question = self.quiz.generate_question(difficulty=difficulty)

    def on_exit(self) -> None:
        super().on_exit()

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            self.push_state("pause")
            return

        if self.resolved or self.current_question is None:
            return

        if event.type == pygame.MOUSEMOTION:
            self.view.set_mouse_position(self.game.screen.get_size(), event.pos)
            return

        selected_index: int | None = None
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            selected_index = self.view.option_at(self.game.screen.get_size(), event.pos)
        elif event.type == pygame.KEYDOWN:
            selected_index = self._choice_index_from_key(event.key)
        else:
            return

        if selected_index is None:
            return

        self.view.set_selected_option(selected_index)
        is_correct = self.quiz.validate_choice(self.current_question, selected_index)
        self.difficulty.observe_answer(is_correct)
        self.battle.apply_quiz_answer(is_correct)
        self.world.apply_battle_answer(is_correct)
        self.battle.player.hp = min(self.battle.player.hp, self.world.snake.length)
        self.view.show_feedback(is_correct)
        self.view.show_answer_result(selected_index, self.current_question.correct_index)
        self.view.play_damage_flash("enemy" if is_correct else "player")

        if self.world.is_game_over:
            self.battle.player.hp = 0

        if self.battle.is_finished():
            self.current_question = None
            self.resolved = True
            battle_won = self.battle.winner() == "player"
            self.game.services.world.apply_battle_result(self.encounter_enemy_id, battle_won)
            return

        difficulty = self.difficulty.current_level(
            encounter_attack=self.encounter_attack,
            combo_multiplier=self.world.combo_tracker.multiplier,
            snake_length=self.world.snake.length,
        )
        self.current_question = self.quiz.generate_question(difficulty=difficulty)

    def update(self, dt: float) -> None:
        self.view.update(dt, self.battle.player, self.battle.enemy)
        if self.resolved:
            self.transition_to("world")

    def render(self, surface: pygame.Surface) -> None:
        self.view.draw(
            surface=surface,
            player=self.battle.player,
            enemy=self.battle.enemy,
            turn_owner="player",
            question_text=self.current_question.prompt if self.current_question else "",
            options=self.current_question.options if self.current_question else tuple(),
            last_note=(
                f"{self.encounter_grade} Lv{self.current_question.difficulty}"
                if self.current_question
                else "Battle resolved, returning to world"
            ),
            battle_progress=f"{self.battle.answered_questions}/{self.battle.total_questions}",
            failures_left=max(0, self.battle.max_failures - self.battle.wrong_answers),
            enemy_cooldown=0.0
        )

    @staticmethod
    def _choice_index_from_key(key: int) -> int | None:
        key_to_index = {
            pygame.K_1: 0,
            pygame.K_2: 1,
            pygame.K_3: 2,
            pygame.K_4: 3,
            pygame.K_KP1: 0,
            pygame.K_KP2: 1,
            pygame.K_KP3: 2,
            pygame.K_KP4: 3,
        }
        return key_to_index.get(key)
