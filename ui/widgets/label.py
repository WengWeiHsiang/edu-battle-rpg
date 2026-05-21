from __future__ import annotations

import pygame


class Label:
    def __init__(self, font_name: str = "consolas", font_size: int = 20, bold: bool = False) -> None:
        self.font = pygame.font.SysFont(font_name, font_size, bold=bold)

    def draw(self, surface: pygame.Surface, text: str, color: tuple[int, int, int], pos: tuple[int, int]) -> None:
        surface.blit(self.font.render(text, True, color), pos)
