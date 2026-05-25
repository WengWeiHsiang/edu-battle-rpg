from __future__ import annotations

import pygame

from ui.battle import AnswerButton
from ui.layout import BattleLayout
from ui.widgets import Label, MessageBox


class QuestionPanel:
    def __init__(self) -> None:
        self.message_label = Label(font_size=20)
        self.question_label = Label(font_size=20)
        self.meta_label = Label(font_size=16)
        self.option_label = Label(font_size=18)
        self.message_box = MessageBox()
        self.answer_button = AnswerButton(self.option_label.font)
        self.hover_index: int | None = None
        self.selected_index: int | None = None
        self.correct_index: int | None = None
        self.feedback_timer: float = 0.0

    def draw(
        self,
        surface: pygame.Surface,
        layout: BattleLayout,
        message: str,
        question_text: str,
        options: tuple[str, ...],
        battle_progress: str,
        failures_left: int,
    ) -> None:
        self.message_box.draw(surface, layout.dialogue_rect)
        self.message_label.draw(surface, message, (28, 34, 42), layout.message_rect.topleft)
        for line_no, line in enumerate(self._wrap_text(f"Q: {question_text}", self.question_label.font, layout.question_rect.width)):
            self.question_label.draw(surface, line, (28, 34, 42), (layout.question_rect.x, layout.question_rect.y + line_no * 22))
        self.meta_label.draw(
            surface,
            f"Progress {battle_progress} | Failures Left {failures_left} | Click or press 1-4",
            (52, 60, 72),
            (layout.question_rect.x, layout.question_rect.bottom + 12),
        )
        for idx, option in enumerate(options[:4]):
            state = "idle"
            if self.feedback_timer > 0 and self.correct_index is not None:
                if idx == self.correct_index:
                    state = "correct"
                elif self.selected_index == idx:
                    state = "wrong"
            elif self.selected_index == idx:
                state = "selected"
            elif self.hover_index == idx:
                state = "hover"
            self.answer_button.draw(surface, layout.option_rects[idx], f"{idx + 1}. {option}", state)

    def update(self, dt: float) -> None:
        self.feedback_timer = max(0.0, self.feedback_timer - dt)
        if self.feedback_timer == 0:
            self.selected_index = None
            self.correct_index = None

    def set_hover(self, option_index: int | None) -> None:
        self.hover_index = option_index

    def set_selected(self, option_index: int) -> None:
        self.selected_index = option_index

    def show_result(self, selected_index: int, correct_index: int) -> None:
        self.selected_index = selected_index
        self.correct_index = correct_index
        self.feedback_timer = 0.55

    @staticmethod
    def option_at(layout: BattleLayout, mouse_pos: tuple[int, int], option_count: int) -> int | None:
        for idx, rect in enumerate(layout.option_rects[: max(0, min(4, option_count))]):
            if rect.collidepoint(mouse_pos):
                return idx
        return None

    @staticmethod
    def _wrap_text(text: str, font: pygame.font.Font, max_width: int) -> list[str]:
        words = text.split()
        if not words:
            return [""]
        lines: list[str] = []
        current = words[0]
        for word in words[1:]:
            candidate = f"{current} {word}"
            if font.size(candidate)[0] <= max_width:
                current = candidate
            else:
                lines.append(current)
                current = word
        lines.append(current)
        return lines[:2]
