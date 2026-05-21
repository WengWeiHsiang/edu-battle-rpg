from __future__ import annotations

from dataclasses import dataclass

import pygame


@dataclass(frozen=True)
class BattleLayout:
    enemy_area: pygame.Rect
    middle_area: pygame.Rect
    bottom_area: pygame.Rect
    enemy_platform: pygame.Rect
    player_platform: pygame.Rect
    enemy_sprite_pos: tuple[int, int]
    player_sprite_pos: tuple[int, int]
    enemy_hp_rect: pygame.Rect
    player_hp_rect: pygame.Rect
    dialogue_rect: pygame.Rect
    message_rect: pygame.Rect
    question_rect: pygame.Rect
    input_rect: pygame.Rect


class BattleLayoutBuilder:
    def build(self, surface_size: tuple[int, int]) -> BattleLayout:
        width, height = surface_size

        padding = max(16, int(width * 0.02))
        enemy_h = int(height * 0.44)
        middle_h = int(height * 0.22)
        bottom_h = height - enemy_h - middle_h

        enemy_area = pygame.Rect(0, 0, width, enemy_h)
        middle_area = pygame.Rect(0, enemy_h, width, middle_h)
        bottom_area = pygame.Rect(0, enemy_h + middle_h, width, bottom_h)

        dialogue_rect = pygame.Rect(
            padding,
            bottom_area.y + max(8, int(bottom_area.height * 0.08)),
            width - (padding * 2),
            bottom_area.height - max(16, int(bottom_area.height * 0.14)),
        )

        enemy_platform = pygame.Rect(int(width * 0.56), int(enemy_area.bottom - enemy_area.height * 0.26), int(width * 0.30), int(height * 0.09))
        player_platform = pygame.Rect(int(width * 0.08), int(middle_area.y + middle_area.height * 0.38), int(width * 0.34), int(height * 0.10))

        enemy_hp_rect = pygame.Rect(int(width * 0.53), int(height * 0.06), int(width * 0.40), 74)
        player_hp_rect = pygame.Rect(int(width * 0.06), int(middle_area.y + middle_area.height * 0.10), int(width * 0.42), 74)

        message_rect = pygame.Rect(dialogue_rect.x + 18, dialogue_rect.y + 10, dialogue_rect.width - 36, 24)
        question_rect = pygame.Rect(dialogue_rect.x + 18, dialogue_rect.y + 36, dialogue_rect.width - 36, 24)

        input_width = min(int(width * 0.52), dialogue_rect.width - 36)
        input_height = max(34, int(dialogue_rect.height * 0.30))
        input_y = dialogue_rect.bottom - input_height - 12
        input_rect = pygame.Rect(
            dialogue_rect.centerx - input_width // 2,
            input_y,
            input_width,
            input_height,
        )

        enemy_px = max(5, int(width * 0.007))
        player_px = max(6, int(width * 0.008))
        enemy_sprite_w = 12 * enemy_px
        enemy_sprite_h = 8 * enemy_px
        player_sprite_w = 12 * player_px
        player_sprite_h = 9 * player_px

        enemy_sprite_pos = (
            enemy_platform.centerx - enemy_sprite_w // 2,
            enemy_platform.y - int(height * 0.14),
        )
        player_sprite_pos = (
            player_platform.centerx - player_sprite_w // 2,
            player_platform.y - int(height * 0.16),
        )

        _ = enemy_sprite_h
        _ = player_sprite_h

        return BattleLayout(
            enemy_area=enemy_area,
            middle_area=middle_area,
            bottom_area=bottom_area,
            enemy_platform=enemy_platform,
            player_platform=player_platform,
            enemy_sprite_pos=enemy_sprite_pos,
            player_sprite_pos=player_sprite_pos,
            enemy_hp_rect=enemy_hp_rect,
            player_hp_rect=player_hp_rect,
            dialogue_rect=dialogue_rect,
            message_rect=message_rect,
            question_rect=question_rect,
            input_rect=input_rect,
        )
