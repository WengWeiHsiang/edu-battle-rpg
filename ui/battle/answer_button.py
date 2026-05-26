from __future__ import annotations

import pygame


class AnswerButton:
    def __init__(self, font: pygame.font.Font) -> None:
        self._font = font

    def draw(self, surface: pygame.Surface, rect: pygame.Rect, text: str, state: str) -> None:
        palette = {
            "idle": ((228, 236, 249), (64, 83, 117), (18, 24, 38)),
            "hover": ((246, 248, 255), (96, 129, 176), (18, 24, 38)),
            "selected": ((232, 243, 255), (52, 132, 206), (14, 21, 34)),
            "correct": ((209, 246, 219), (56, 155, 87), (13, 34, 21)),
            "wrong": ((255, 218, 218), (187, 68, 68), (44, 18, 18)),
        }
        fill, border, text_color = palette.get(state, palette["idle"])

        shadow = rect.move(0, 3)
        pygame.draw.rect(surface, (10, 14, 22, 110), shadow, border_radius=12)
        pygame.draw.rect(surface, fill, rect, border_radius=12)
        pygame.draw.rect(surface, border, rect, width=3, border_radius=12)

        text = self._fit_text(text, rect.width - 24)
        rendered = self._font.render(text, True, text_color)
        text_pos = (rect.x + 16, rect.centery - rendered.get_height() // 2)
        surface.blit(rendered, text_pos)

    def _fit_text(self, text: str, max_width: int) -> str:
        if self._font.size(text)[0] <= max_width:
            return text
        suffix = "..."
        for i in range(len(text), 0, -1):
            candidate = text[:i].rstrip() + suffix
            if self._font.size(candidate)[0] <= max_width:
                return candidate
        return suffix
