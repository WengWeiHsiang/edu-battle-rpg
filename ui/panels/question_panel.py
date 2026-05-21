from __future__ import annotations

import pygame

from ui.layout import BattleLayout
from ui.widgets import InputBox, Label, MessageBox


class QuestionPanel:
    def __init__(self) -> None:
        self.message_label = Label(font_size=20)
        self.question_label = Label(font_size=20)
        self.message_box = MessageBox()
        self.input_box = InputBox(pygame.Rect(0, 0, 0, 0))

    def draw(
        self,
        surface: pygame.Surface,
        layout: BattleLayout,
        message: str,
        question_text: str,
        answer_text: str,
    ) -> None:
        self.message_box.draw(surface, layout.dialogue_rect)
        self.message_label.draw(surface, message, (28, 34, 42), layout.message_rect.topleft)
        self.question_label.draw(surface, f"Q: {question_text}", (28, 34, 42), layout.question_rect.topleft)
        self.input_box.rect = layout.input_rect
        self.input_box.draw(surface, self.message_label.font, answer_text, "Type answer and press Enter")
