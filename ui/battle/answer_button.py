from __future__ import annotations

import pygame


class AnswerButton:
    def __init__(self, font: pygame.font.Font) -> None:
        self._font = font

    def draw(self, surface: pygame.Surface, rect: pygame.Rect, text: str, state: str) -> None:
        palette = {
            "idle": ((241, 238, 224), (42, 49, 60), (24, 29, 36)),
            "hover": ((255, 247, 208), (66, 88, 116), (24, 29, 36)),
            "selected": ((225, 240, 255), (64, 118, 181), (24, 29, 36)),
            "correct": ((210, 244, 218), (58, 142, 82), (20, 34, 24)),
            "wrong": ((250, 214, 214), (171, 67, 67), (44, 18, 18)),
        }
        fill, border, text_color = palette.get(state, palette["idle"])

        shadow = rect.move(0, 2)
        pygame.draw.rect(surface, (20, 26, 32, 70), shadow, border_radius=10)
        pygame.draw.rect(surface, fill, rect, border_radius=10)
        pygame.draw.rect(surface, border, rect, width=2, border_radius=10)

        rendered = self._font.render(text, True, text_color)
        text_pos = (rect.x + 14, rect.centery - rendered.get_height() // 2)
        surface.blit(rendered, text_pos)
