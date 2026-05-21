from __future__ import annotations

import pygame

from entities.enemy import Enemy
from entities.player import Player


class WorldView:
    def draw(
        self,
        surface: pygame.Surface,
        player: Player,
        enemies: list[Enemy],
        encounter_hint: str,
        transition_alpha: int,
    ) -> None:
        width, height = surface.get_size()
        surface.fill((62, 137, 73))
        pygame.draw.rect(surface, (74, 156, 86), pygame.Rect(40, 40, width - 80, height - 80), border_radius=10)

        for enemy in enemies:
            pygame.draw.rect(surface, (143, 60, 72), enemy.rect, border_radius=4)
            eye_y = enemy.rect.y + 6
            pygame.draw.rect(surface, (240, 236, 232), pygame.Rect(enemy.rect.x + 4, eye_y, 3, 3))
            pygame.draw.rect(surface, (240, 236, 232), pygame.Rect(enemy.rect.x + enemy.rect.width - 7, eye_y, 3, 3))

        pygame.draw.rect(surface, (66, 89, 180), player.rect, border_radius=4)

        font = pygame.font.SysFont("consolas", 22)
        hint = font.render(encounter_hint, True, (240, 248, 231))
        surface.blit(hint, (44, 14))

        if transition_alpha > 0:
            overlay = pygame.Surface((width, height), pygame.SRCALPHA)
            overlay.fill((255, 255, 255, transition_alpha))
            surface.blit(overlay, (0, 0))
