from __future__ import annotations

from dataclasses import dataclass

import pygame


@dataclass
class InputSnapshot:
    text: str


class InputBuffer:
    def __init__(self, max_length: int = 32) -> None:
        self._text = ""
        self._max_length = max_length
        self._submitted: InputSnapshot | None = None

    @property
    def text(self) -> str:
        return self._text

    def clear(self) -> None:
        self._text = ""
        self._submitted = None

    def feed_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            self._text = self._text[:-1]
            return

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self._submitted = InputSnapshot(text=self._text.strip())
            return

        if event.type == pygame.TEXTINPUT and event.text and len(self._text) < self._max_length:
            available = self._max_length - len(self._text)
            self._text += event.text[:available]

    def pop_submit(self) -> InputSnapshot | None:
        submitted = self._submitted
        self._submitted = None
        return submitted
