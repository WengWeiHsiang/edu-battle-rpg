from __future__ import annotations

import pygame


class HPBar:
    def draw(self, surface: pygame.Surface, rect: pygame.Rect, ratio: float) -> None:
        pygame.draw.rect(surface, (30, 34, 38), rect, border_radius=6)
        clamped = max(0.0, min(1.0, ratio))
        color = (84, 198, 91) if clamped > 0.5 else (232, 187, 54) if clamped > 0.2 else (226, 93, 80)
        fill = pygame.Rect(rect.x + 2, rect.y + 2, int((rect.width - 4) * clamped), rect.height - 4)
        pygame.draw.rect(surface, color, fill, border_radius=5)
