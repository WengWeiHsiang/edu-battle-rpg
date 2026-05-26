from __future__ import annotations

import pygame


class HPBar:
    def draw(
        self,
        surface: pygame.Surface,
        rect: pygame.Rect,
        ratio: float,
        colors: dict[str, tuple[int, int, int]] | None = None,
    ) -> None:
        palette = colors or {
            "bg": (30, 34, 38),
            "high": (84, 198, 91),
            "mid": (232, 187, 54),
            "low": (226, 93, 80),
        }
        pygame.draw.rect(surface, palette["bg"], rect, border_radius=6)
        clamped = max(0.0, min(1.0, ratio))
        color = palette["high"] if clamped > 0.5 else palette["mid"] if clamped > 0.2 else palette["low"]
        fill = pygame.Rect(rect.x + 2, rect.y + 2, int((rect.width - 4) * clamped), rect.height - 4)
        pygame.draw.rect(surface, color, fill, border_radius=5)
