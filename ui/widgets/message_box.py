from __future__ import annotations

import pygame


class MessageBox:
    def draw(self, surface: pygame.Surface, rect: pygame.Rect) -> None:
        panel = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        pygame.draw.rect(panel, (247, 246, 233, 245), panel.get_rect(), border_radius=2)
        pygame.draw.rect(panel, (38, 42, 50), panel.get_rect(), width=4, border_radius=2)
        surface.blit(panel, rect.topleft)
