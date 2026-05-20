from __future__ import annotations

import pygame

from entities.combatant import Combatant


class BattleView:
    def draw(
        self,
        surface: pygame.Surface,
        player: Combatant,
        enemy: Combatant,
        turn_owner: str,
        question_text: str,
        answer_text: str,
        last_note: str,
    ) -> None:
        surface.fill((20, 20, 24))
        font = pygame.font.SysFont("consolas", 28)
        small = pygame.font.SysFont("consolas", 22)

        player_text = font.render(f"{player.name} HP: {player.hp}/{player.max_hp}", True, (170, 255, 170))
        enemy_text = font.render(f"{enemy.name} HP: {enemy.hp}/{enemy.max_hp}", True, (255, 170, 170))
        turn_text = small.render(f"Turn: {turn_owner}", True, (210, 210, 240))
        prompt_text = small.render(f"Question: {question_text}", True, (240, 240, 180))
        answer_label = small.render(f"Answer: {answer_text}", True, (200, 230, 255))
        note_text = small.render(last_note, True, (190, 190, 190))

        surface.blit(player_text, (50, 80))
        surface.blit(enemy_text, (520, 80))
        surface.blit(turn_text, (50, 170))
        surface.blit(prompt_text, (50, 260))
        surface.blit(answer_label, (50, 320))
        surface.blit(note_text, (50, 390))
