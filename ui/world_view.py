from __future__ import annotations

import pygame

from systems.world.session import WorldSession


class WorldView:
    def draw(self, surface: pygame.Surface, world: WorldSession, transition_alpha: int = 0) -> None:
        width, height = surface.get_size()
        surface.fill((16, 20, 24))

        hud_h = 72
        play_rect = pygame.Rect(20, hud_h + 12, width - 40, height - hud_h - 32)
        cell_w = play_rect.width // world.cols
        cell_h = play_rect.height // world.rows
        cell = min(cell_w, cell_h)
        grid_w = cell * world.cols
        grid_h = cell * world.rows
        grid_rect = pygame.Rect(play_rect.x, play_rect.y, grid_w, grid_h)

        pygame.draw.rect(surface, (33, 45, 52), grid_rect, border_radius=8)

        for i in range(world.cols + 1):
            x = grid_rect.x + i * cell
            pygame.draw.line(surface, (42, 56, 64), (x, grid_rect.y), (x, grid_rect.bottom), 1)
        for i in range(world.rows + 1):
            y = grid_rect.y + i * cell
            pygame.draw.line(surface, (42, 56, 64), (grid_rect.x, y), (grid_rect.right, y), 1)

        if world.orb:
            orb_rect = pygame.Rect(grid_rect.x + world.orb.x * cell, grid_rect.y + world.orb.y * cell, cell, cell)
            pygame.draw.ellipse(surface, (255, 205, 83), orb_rect.inflate(-6, -6))

        for enemy in world.enemies:
            rect = pygame.Rect(grid_rect.x + enemy.x * cell, grid_rect.y + enemy.y * cell, cell, cell)
            pygame.draw.rect(surface, (226, 94, 94), rect.inflate(-4, -4), border_radius=4)

        for idx, segment in enumerate(world.snake.segments):
            sx, sy = segment
            rect = pygame.Rect(grid_rect.x + sx * cell, grid_rect.y + sy * cell, cell, cell)
            color = (92, 221, 128) if idx == 0 else (64, 176, 98)
            pygame.draw.rect(surface, color, rect.inflate(-4, -4), border_radius=5)

        font = pygame.font.SysFont("consolas", 24)
        small = pygame.font.SysFont("consolas", 20)

        combo = world.combo_tracker.multiplier
        hud = f"Score: {world.score}    Combo x{combo}    Length: {world.snake.length}"
        surface.blit(font.render(hud, True, (236, 240, 244)), (24, 20))

        hint = "Move: WASD/Arrows  |  Hit enemy to enter quiz battle"
        surface.blit(small.render(hint, True, (206, 223, 229)), (24, height - 40))

        if world.feedback:
            note = font.render(world.feedback, True, (255, 214, 118))
            surface.blit(note, note.get_rect(center=(width // 2, hud_h + 16)))

        if transition_alpha > 0:
            overlay = pygame.Surface((width, height), pygame.SRCALPHA)
            overlay.fill((255, 255, 255, transition_alpha))
            surface.blit(overlay, (0, 0))
