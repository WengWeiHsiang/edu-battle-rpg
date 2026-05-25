from __future__ import annotations

import pygame

from entities.combatant import Combatant
from ui.layout import BattleLayoutBuilder
from ui.panels import BattlePanel, QuestionPanel, StatusPanel


class BattleView:
    def __init__(self) -> None:
        self._hp_display = {"player": 1.0, "enemy": 1.0}
        self._flash = {"player": 0.0, "enemy": 0.0}
        self._feedback_text = ""
        self._feedback_timer = 0.0
        self._enemy_float_phase = 0.0
        self._layout_builder = BattleLayoutBuilder()

        self._battle_panel = BattlePanel()
        self._status_panel = StatusPanel()
        self._question_panel = QuestionPanel()
        self._last_layout = None
        self._option_count = 0

    def on_enter(self, player: Combatant, enemy: Combatant) -> None:
        self._hp_display["player"] = player.hp / player.max_hp
        self._hp_display["enemy"] = enemy.hp / enemy.max_hp
        self._flash["player"] = 0.0
        self._flash["enemy"] = 0.0
        self._feedback_text = ""
        self._feedback_timer = 0.0
        self._enemy_float_phase = 0.0

    def show_feedback(self, is_correct: bool) -> None:
        self._feedback_text = "Correct!" if is_correct else "Wrong!"
        self._feedback_timer = 1.0

    def show_answer_result(self, selected_index: int, correct_index: int) -> None:
        self._question_panel.show_result(selected_index, correct_index)

    def play_damage_flash(self, target: str) -> None:
        if target in self._flash:
            self._flash[target] = 0.22

    def update(self, dt: float, player: Combatant, enemy: Combatant) -> None:
        self._animate_hp("player", player, dt)
        self._animate_hp("enemy", enemy, dt)
        self._flash["player"] = max(0.0, self._flash["player"] - dt)
        self._flash["enemy"] = max(0.0, self._flash["enemy"] - dt)
        self._feedback_timer = max(0.0, self._feedback_timer - dt)
        self._enemy_float_phase += dt
        self._question_panel.update(dt)

    def _animate_hp(self, key: str, combatant: Combatant, dt: float) -> None:
        target = combatant.hp / combatant.max_hp
        current = self._hp_display[key]
        self._hp_display[key] = current + (target - current) * min(1.0, dt * 8.0)

    def draw(
        self,
        surface: pygame.Surface,
        player: Combatant,
        enemy: Combatant,
        turn_owner: str,
        question_text: str,
        options: tuple[str, ...],
        last_note: str,
        battle_progress: str,
        failures_left: int,
        enemy_cooldown: float,
    ) -> None:
        width, height = surface.get_size()
        layout = self._layout_builder.build((width, height))
        self._last_layout = layout
        self._option_count = len(options)

        self._battle_panel.draw(surface, layout, width, height, self._flash, self._enemy_float_phase)
        self._status_panel.draw(surface, layout, player, enemy, self._hp_display)

        message = self._feedback_text if self._feedback_timer > 0 else last_note
        if turn_owner == "enemy":
            message = f"Enemy turn ({enemy_cooldown:.1f}s)"
        elif not message:
            message = "Choose 1-4 to answer."

        self._question_panel.draw(
            surface,
            layout,
            message,
            question_text,
            options,
            battle_progress,
            failures_left,
        )

    def set_mouse_position(self, surface_size: tuple[int, int], mouse_pos: tuple[int, int]) -> None:
        layout = self._layout_builder.build(surface_size)
        hovered = self._question_panel.option_at(layout, mouse_pos, self._option_count)
        self._question_panel.set_hover(hovered)

    def option_at(self, surface_size: tuple[int, int], mouse_pos: tuple[int, int]) -> int | None:
        layout = self._layout_builder.build(surface_size)
        return self._question_panel.option_at(layout, mouse_pos, self._option_count)

    def set_selected_option(self, option_index: int) -> None:
        self._question_panel.set_selected(option_index)
