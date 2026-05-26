from __future__ import annotations

import random

import pygame


class BattleFeedback:
    def __init__(self) -> None:
        self._flash_color = (0, 0, 0)
        self._flash_timer = 0.0
        self._shake_timer = 0.0
        self._shake_strength = 0
        self._popup_text = ""
        self._popup_timer = 0.0

    def trigger_correct(self) -> None:
        self._flash_color = (82, 210, 128)
        self._flash_timer = 0.18
        self._popup_text = "COMBO!"
        self._popup_timer = 0.55

    def trigger_wrong(self) -> None:
        self._flash_color = (232, 86, 86)
        self._flash_timer = 0.18
        self._shake_timer = 0.28
        self._shake_strength = 8

    def update(self, dt: float) -> None:
        self._flash_timer = max(0.0, self._flash_timer - dt)
        self._shake_timer = max(0.0, self._shake_timer - dt)
        self._popup_timer = max(0.0, self._popup_timer - dt)

    def shake_offset(self) -> tuple[int, int]:
        if self._shake_timer <= 0:
            return (0, 0)
        power = max(1, int(self._shake_strength * (self._shake_timer / 0.28)))
        return (random.randint(-power, power), random.randint(-power // 2, power // 2))

    def draw_overlay(self, surface: pygame.Surface) -> None:
        if self._flash_timer <= 0:
            return
        alpha = int(90 * (self._flash_timer / 0.18))
        tint = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
        tint.fill((*self._flash_color, alpha))
        surface.blit(tint, (0, 0))

    def draw_popup(self, surface: pygame.Surface, center: tuple[int, int]) -> None:
        if self._popup_timer <= 0 or not self._popup_text:
            return
        y_offset = int((1.0 - (self._popup_timer / 0.55)) * 12)
        font = pygame.font.SysFont("consolas", 26, bold=True)
        text = font.render(self._popup_text, True, (255, 242, 112))
        shadow = font.render(self._popup_text, True, (38, 30, 12))
        pos = (center[0] - text.get_width() // 2, center[1] - y_offset)
        surface.blit(shadow, (pos[0] + 2, pos[1] + 2))
        surface.blit(text, pos)
