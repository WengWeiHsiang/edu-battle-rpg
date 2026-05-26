from __future__ import annotations

import math

import pygame

from ui.layout import BattleLayout
from ui.theme import BATTLE_BG


class BattlePanel:
    ENEMY_PATTERN = [
        "...oooooo...",
        "..o111111o..",
        ".o11122111o.",
        ".o11222211o.",
        ".o11222211o.",
        ".o11111111o.",
        "..o11ww11o..",
        "...oooooo...",
    ]
    PLAYER_PATTERN = [
        "....bbbb....",
        "...b1111b...",
        "..b122221b..",
        ".b12222221b.",
        ".b12233221b.",
        ".b12222221b.",
        "..b111111b..",
        "...b1ww1b...",
        "...b1111b...",
    ]

    ENEMY_PALETTE = {"o": (35, 42, 54), "1": (114, 207, 131), "2": (66, 152, 94), "w": (244, 246, 250)}
    PLAYER_PALETTE = {"b": (30, 36, 48), "1": (242, 169, 98), "2": (228, 120, 87), "3": (163, 81, 62), "w": (245, 247, 250)}

    def draw(
        self,
        surface: pygame.Surface,
        layout: BattleLayout,
        width: int,
        height: int,
        flash: dict[str, float],
        enemy_float_phase: float,
    ) -> None:
        surface.fill(BATTLE_BG["base"])
        pygame.draw.rect(surface, BATTLE_BG["enemy_zone"], layout.enemy_zone)
        pygame.draw.rect(surface, BATTLE_BG["question_zone"], layout.question_zone)
        pygame.draw.rect(surface, BATTLE_BG["answer_zone"], layout.answer_zone)

        pygame.draw.ellipse(surface, BATTLE_BG["enemy_platform"], layout.enemy_platform)

        enemy_px = max(7, int(width * 0.010))
        enemy_shadow = pygame.Rect(
            layout.enemy_platform.centerx - int(enemy_px * 5.5),
            layout.enemy_platform.y - int(enemy_px * 0.2),
            int(enemy_px * 11),
            int(enemy_px * 2),
        )
        pygame.draw.ellipse(surface, BATTLE_BG["enemy_shadow"], enemy_shadow)
        float_offset = int(math.sin(enemy_float_phase * 2.0) * max(2, int(height * 0.008)))
        enemy_sprite_pos = (layout.enemy_sprite_pos[0], layout.enemy_sprite_pos[1] - float_offset)
        self._draw_sprite(surface, enemy_sprite_pos, enemy_px, self.ENEMY_PALETTE, self.ENEMY_PATTERN, flash["enemy"])

    def _draw_sprite(
        self,
        surface: pygame.Surface,
        top_left: tuple[int, int],
        pixel: int,
        palette: dict[str, tuple[int, int, int]],
        pattern: list[str],
        flash_t: float,
    ) -> None:
        for y, row in enumerate(pattern):
            for x, code in enumerate(row):
                if code == ".":
                    continue
                rect = pygame.Rect(top_left[0] + x * pixel, top_left[1] + y * pixel, pixel, pixel)
                pygame.draw.rect(surface, palette.get(code, (0, 0, 0)), rect)

        if flash_t > 0:
            width = len(pattern[0]) * pixel
            height = len(pattern) * pixel
            alpha = int(120 * (flash_t / 0.22))
            flash = pygame.Surface((width, height), pygame.SRCALPHA)
            flash.fill((255, 255, 255, alpha))
            surface.blit(flash, top_left)
