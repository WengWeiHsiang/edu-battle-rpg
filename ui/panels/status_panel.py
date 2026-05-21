from __future__ import annotations

import pygame

from entities.combatant import Combatant
from ui.layout import BattleLayout
from ui.widgets import HPBar, Label


class StatusPanel:
    def __init__(self) -> None:
        self.name_label = Label(font_size=20, bold=True)
        self.hp_label = Label(font_size=16)
        self.hp_bar = HPBar()

    def draw(
        self,
        surface: pygame.Surface,
        layout: BattleLayout,
        player: Combatant,
        enemy: Combatant,
        hp_ratio: dict[str, float],
    ) -> None:
        self._draw_box(surface, layout.enemy_hp_rect, enemy.name, enemy.hp, enemy.max_hp, hp_ratio["enemy"])
        self._draw_box(surface, layout.player_hp_rect, player.name, player.hp, player.max_hp, hp_ratio["player"])

    def _draw_box(self, surface: pygame.Surface, rect: pygame.Rect, name: str, hp: int, max_hp: int, ratio: float) -> None:
        panel = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        pygame.draw.rect(panel, (243, 242, 226, 245), panel.get_rect(), border_radius=2)
        pygame.draw.rect(panel, (36, 41, 49), panel.get_rect(), width=3, border_radius=2)
        surface.blit(panel, rect.topleft)

        self.name_label.draw(surface, name, (32, 36, 44), (rect.x + 12, rect.y + 10))
        self.hp_label.draw(surface, f"HP {hp}/{max_hp}", (42, 46, 52), (rect.x + 12, rect.y + 36))
        gauge = pygame.Rect(rect.x + 86, rect.y + 38, rect.width - 98, 14)
        self.hp_bar.draw(surface, gauge, ratio)
