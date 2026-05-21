from __future__ import annotations

import pygame


class InputBox:
    def __init__(self, rect: pygame.Rect) -> None:
        self.rect = rect
        self.bg_color = (234, 236, 221, 245)
        self.border_color = (42, 46, 54)
        self.text_color = (30, 34, 42)
        self.placeholder_color = (107, 113, 124)

    def draw(
        self,
        surface: pygame.Surface,
        font: pygame.font.Font,
        text: str,
        placeholder: str = "Type answer and press Enter",
    ) -> None:
        panel = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        pygame.draw.rect(panel, self.bg_color, panel.get_rect(), border_radius=2)
        pygame.draw.rect(panel, self.border_color, panel.get_rect(), width=3, border_radius=2)
        surface.blit(panel, self.rect.topleft)

        display_text = text if text else placeholder
        color = self.text_color if text else self.placeholder_color
        text_surface = font.render(display_text, True, color)
        text_rect = text_surface.get_rect(midleft=(self.rect.x + 14, self.rect.centery))
        surface.blit(text_surface, text_rect)
