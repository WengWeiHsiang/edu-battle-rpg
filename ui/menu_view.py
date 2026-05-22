from __future__ import annotations

import pygame


class MenuView:
    def __init__(self, title: str = "Edu Snake Survivor", subtitle: str = "Press Enter to start") -> None:
        self.title = title
        self.subtitle = subtitle

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill((24, 28, 40))
        title_font = pygame.font.SysFont("consolas", 52)
        text_font = pygame.font.SysFont("consolas", 24)

        title = title_font.render(self.title, True, (240, 240, 255))
        subtitle = text_font.render(self.subtitle, True, (200, 220, 245))
        esc = text_font.render("Esc: Quit", True, (170, 190, 220))

        surface.blit(title, title.get_rect(center=(surface.get_width() // 2, 180)))
        surface.blit(subtitle, subtitle.get_rect(center=(surface.get_width() // 2, 300)))
        surface.blit(esc, esc.get_rect(center=(surface.get_width() // 2, 350)))
