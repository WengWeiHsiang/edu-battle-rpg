from __future__ import annotations

import pygame

from ui.battle import AnswerButton
from ui.layout import BattleLayout
from ui.widgets import Label


class QuestionPanel:
    def __init__(self) -> None:
        self.message_label = Label(font_size=20, bold=True)
        self.question_label = Label(font_size=34, bold=True)
        self.meta_label = Label(font_size=16)
        self.option_label = Label(font_size=22, bold=True)
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
        msg_text = self._fit_text(message, self.message_label.font, layout.message_rect.width)
        self.message_label.draw(surface, msg_text, (191, 214, 240), layout.message_rect.topleft)
        wrapped = self._wrap_text(question_text, self.question_label.font, layout.question_rect.width - 40)
        available_top = layout.message_rect.bottom + 8
        available_bottom = layout.meta_rect.y - 8
        line_height = max(30, min(40, (available_bottom - available_top) // max(1, len(wrapped))))
        for line_no, line in enumerate(wrapped):
            rendered = self.question_label.font.render(line, True, (247, 248, 255))
            x = layout.question_rect.centerx - rendered.get_width() // 2
            y = available_top + line_no * line_height
            surface.blit(rendered, (x, y))
        meta_text = self._fit_text(
            f"Round {battle_progress}  |  Misses Left {failures_left}  |  Keys 1-4",
            self.meta_label.font,
            layout.meta_rect.width,
        )
        self.meta_label.draw(
            surface,
            meta_text,
            (158, 175, 204),
            layout.meta_rect.topleft,
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
        return lines[:3]

    @staticmethod
    def _fit_text(text: str, font: pygame.font.Font, max_width: int) -> str:
        if font.size(text)[0] <= max_width:
            return text
        suffix = "..."
        for i in range(len(text), 0, -1):
            candidate = text[:i].rstrip() + suffix
            if font.size(candidate)[0] <= max_width:
                return candidate
        return suffix
