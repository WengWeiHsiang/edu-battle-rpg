from __future__ import annotations

import pygame


class TextInputBuffer:
    def __init__(self) -> None:
        self.text = ""

    def clear(self) -> None:
        self.text = ""

    def handle_key(self, event: pygame.event.Event) -> None:
        if event.key == pygame.K_BACKSPACE:
            self.text = self.text[:-1]
            return

        if event.unicode and event.unicode.isprintable() and event.key != pygame.K_RETURN:
            self.text += event.unicode
