from __future__ import annotations

import pygame

from states.base_state import BaseState
from systems.transition import FlashTransition
from ui.world_view import WorldView


class WorldState(BaseState):
    def __init__(self, game: "Game") -> None:
        super().__init__(game)
        self.view = WorldView()
        self.transition = FlashTransition()
        self.world = game.services.world
        self.encounter_enemy_id: str | None = None

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.transition_to("menu")

    def update(self, dt: float) -> None:
        bounds = pygame.Rect(42, 42, self.game.config.width - 84, self.game.config.height - 84)
        keys = pygame.key.get_pressed()
        dx = float(keys[pygame.K_d] or keys[pygame.K_RIGHT]) - float(keys[pygame.K_a] or keys[pygame.K_LEFT])
        dy = float(keys[pygame.K_s] or keys[pygame.K_DOWN]) - float(keys[pygame.K_w] or keys[pygame.K_UP])

        if not self.transition.active:
            self.world.player.move(dx, dy, dt, bounds)
            for enemy in self.world.enemies:
                enemy.update(dt, bounds)

            for enemy in self.world.enemies:
                if self.world.player.rect.colliderect(enemy.rect):
                    self.world.begin_encounter(enemy)
                    self.encounter_enemy_id = enemy.enemy_id
                    self.transition.start()
                    break
        else:
            if self.transition.update(dt):
                self.transition_to("battle")

    def render(self, surface: pygame.Surface) -> None:
        hint = "Move: WASD / Arrow Keys  |  Touch enemy to battle"
        self.view.draw(surface, self.world.player, self.world.enemies, hint, self.transition.alpha())
