from __future__ import annotations

from dataclasses import dataclass

import pygame

from ui.battle import AnswerGrid


@dataclass(frozen=True)
class BattleLayout:
    enemy_zone: pygame.Rect
    question_zone: pygame.Rect
    answer_zone: pygame.Rect
    enemy_platform: pygame.Rect
    enemy_sprite_pos: tuple[int, int]
    enemy_info_rect: pygame.Rect
    player_info_rect: pygame.Rect
    enemy_hp_rect: pygame.Rect
    player_hp_rect: pygame.Rect
    question_rect: pygame.Rect
    message_rect: pygame.Rect
    meta_rect: pygame.Rect
    answers_area_rect: pygame.Rect
    option_rects: tuple[pygame.Rect, ...]


class BattleLayoutBuilder:
    def __init__(self) -> None:
        self._answer_grid = AnswerGrid(cols=2, rows=2)

    def build(self, surface_size: tuple[int, int]) -> BattleLayout:
        width, height = surface_size

        padding = max(12, int(width * 0.02))
        enemy_h = max(140, int(height * 0.28))
        question_h = max(180, int(height * 0.34))
        answer_h = max(170, height - enemy_h - question_h)
        total_h = enemy_h + question_h + answer_h
        if total_h > height:
            overflow = total_h - height
            question_h = max(160, question_h - overflow)
            answer_h = max(150, height - enemy_h - question_h)

        enemy_zone = pygame.Rect(0, 0, width, enemy_h)
        question_zone = pygame.Rect(0, enemy_h, width, question_h)
        answer_zone = pygame.Rect(0, enemy_h + question_h, width, answer_h)

        question_rect = pygame.Rect(
            padding,
            question_zone.y + max(8, int(question_zone.height * 0.10)),
            width - (padding * 2),
            question_zone.height - max(16, int(question_zone.height * 0.14)),
        )

        enemy_platform = pygame.Rect(
            int(width * 0.5 - width * 0.12),
            int(enemy_zone.bottom - enemy_zone.height * 0.25),
            int(width * 0.24),
            int(height * 0.06),
        )

        info_h = max(60, min(72, int(height * 0.1)))
        info_w = max(180, int(width * 0.28))
        info_y = max(8, int(height * 0.02))
        enemy_info_rect = pygame.Rect(
            int(width * 0.03), info_y, info_w, info_h)
        player_info_rect = pygame.Rect(
            width - int(width * 0.03) - info_w, info_y, info_w, info_h)

        hp_h = max(10, int(info_h * 0.20))
        enemy_hp_rect = pygame.Rect(
            enemy_info_rect.x + 10, enemy_info_rect.bottom - hp_h - 8, enemy_info_rect.width - 20, hp_h)
        player_hp_rect = pygame.Rect(
            player_info_rect.x + 10, player_info_rect.bottom - hp_h - 8, player_info_rect.width - 20, hp_h)

        line_h = max(22, int(question_rect.height * 0.15))
        message_rect = pygame.Rect(
            question_rect.x, question_rect.y, question_rect.width, line_h)
        meta_rect = pygame.Rect(
            question_rect.x, question_rect.bottom - line_h, question_rect.width, line_h)

        answers_area_rect = pygame.Rect(
            padding,
            answer_zone.y + max(6, int(answer_zone.height * 0.08)),
            width - (padding * 2),
            answer_zone.height - max(12, int(answer_zone.height * 0.12)),
        )
        option_rects = self._answer_grid.build_rects(
            answers_area_rect, gap=max(8, int(width * 0.01)))

        enemy_px = max(5, int(width * 0.007))
        enemy_sprite_w = 12 * enemy_px
        enemy_sprite_pos = (
            enemy_platform.centerx - enemy_sprite_w // 2,
            enemy_platform.y - int(enemy_zone.height * 0.50),
        )

        return BattleLayout(
            enemy_zone=enemy_zone,
            question_zone=question_zone,
            answer_zone=answer_zone,
            enemy_platform=enemy_platform,
            enemy_sprite_pos=enemy_sprite_pos,
            enemy_info_rect=enemy_info_rect,
            player_info_rect=player_info_rect,
            enemy_hp_rect=enemy_hp_rect,
            player_hp_rect=player_hp_rect,
            question_rect=question_rect,
            message_rect=message_rect,
            meta_rect=meta_rect,
            answers_area_rect=answers_area_rect,
            option_rects=option_rects,
        )
