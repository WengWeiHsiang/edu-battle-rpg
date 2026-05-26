from __future__ import annotations

import pygame

from entities.combatant import Combatant
from ui.layout import BattleLayout
from ui.theme import ENEMY_HP_COLORS, ENEMY_PANEL_COLORS, HERO_HP_COLORS, HERO_PANEL_COLORS
from ui.widgets import HPBar, Label


class StatusPanel:
    def __init__(self) -> None:
        self.name_label = Label(font_size=18, bold=True)
        self.hp_label = Label(font_size=14)
        self.meta_label = Label(font_size=14)
        self.hp_bar = HPBar()

    def draw(
        self,
        surface: pygame.Surface,
        layout: BattleLayout,
        player: Combatant,
        enemy: Combatant,
        hp_ratio: dict[str, float],
        enemy_grade: str,
    ) -> None:
        self._draw_box(
            surface,
            layout.enemy_info_rect,
            layout.enemy_hp_rect,
            enemy.name,
            enemy_grade,
            enemy.hp,
            enemy.max_hp,
            hp_ratio["enemy"],
            ENEMY_PANEL_COLORS,
            ENEMY_HP_COLORS,
        )
        self._draw_box(
            surface,
            layout.player_info_rect,
            layout.player_hp_rect,
            player.name,
            "",
            player.hp,
            player.max_hp,
            hp_ratio["player"],
            HERO_PANEL_COLORS,
            HERO_HP_COLORS,
        )

    def _draw_box(
        self,
        surface: pygame.Surface,
        rect: pygame.Rect,
        hp_rect: pygame.Rect,
        name: str,
        meta: str,
        hp: int,
        max_hp: int,
        ratio: float,
        panel_colors: dict[str, tuple[int, int, int] | tuple[int, int, int, int]],
        hp_colors: dict[str, tuple[int, int, int]],
    ) -> None:
        panel = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        pygame.draw.rect(panel, panel_colors["fill"], panel.get_rect(), border_radius=10)
        pygame.draw.rect(panel, panel_colors["border"], panel.get_rect(), width=2, border_radius=10)
        surface.blit(panel, rect.topleft)

        hp_text = f"HP {hp}/{max_hp}"
        hp_width = self.hp_label.font.size(hp_text)[0]
        hp_x = rect.right - hp_width - 10
        hp_x = max(rect.x + 10, hp_x)

        title_max = max(40, hp_x - (rect.x + 10) - 10)
        name_text = self._fit_text(name, self.name_label.font, title_max)
        meta_text = self._fit_text(meta, self.meta_label.font, rect.width - 20)

        self.name_label.draw(surface, name_text, panel_colors["name"], (rect.x + 10, rect.y + 8))
        if meta_text:
            self.meta_label.draw(surface, meta_text, panel_colors["meta"], (rect.x + 10, rect.y + 28))
        self.hp_label.draw(surface, hp_text, panel_colors["hp_text"], (hp_x, rect.y + 8))
        self.hp_bar.draw(surface, hp_rect, ratio, hp_colors)

    @staticmethod
    def _fit_text(text: str, font: pygame.font.Font, max_width: int) -> str:
        if font.size(text)[0] <= max_width:
            return text
        suffix = "..."
        suffix_w = font.size(suffix)[0]
        for i in range(len(text), 0, -1):
            candidate = text[:i].rstrip() + suffix
            if font.size(candidate)[0] <= max_width and font.size(text[:i])[0] + suffix_w <= max_width:
                return candidate
        return suffix
