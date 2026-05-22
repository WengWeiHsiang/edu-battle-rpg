from __future__ import annotations

import pygame

from states.base_state import BaseState
from systems.transition import FlashTransition
from ui.world_view import WorldView


class WorldState(BaseState):
    def __init__(self, game: "Game") -> None:
        super().__init__(game)
        self.view = WorldView()
        self.world = game.services.world
        self.transition = FlashTransition(duration=0.25)

    def on_enter(self) -> None:
        super().on_enter()
        if self.world.is_game_over:
            self.world.reset()
            self.game.services.difficulty.reset()
        self.transition.active = False

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.transition_to("menu")
                return

            directions = {
                pygame.K_w: (0, -1),
                pygame.K_UP: (0, -1),
                pygame.K_s: (0, 1),
                pygame.K_DOWN: (0, 1),
                pygame.K_a: (-1, 0),
                pygame.K_LEFT: (-1, 0),
                pygame.K_d: (1, 0),
                pygame.K_RIGHT: (1, 0),
            }
            if event.key in directions:
                self.world.set_direction(directions[event.key])
                return

    def update(self, dt: float) -> None:
        if self.transition.active:
            if self.transition.update(dt):
                self.transition_to("battle")
            return

        self.world.update(dt)
        enemy = self.world.find_enemy_collision()
        if enemy:
            self.world.begin_encounter(enemy)
            self.transition.start()

        if self.world.is_game_over:
            self.transition_to("game_over")

    def render(self, surface: pygame.Surface) -> None:
        self.view.draw(surface, self.world, self.transition.alpha())
