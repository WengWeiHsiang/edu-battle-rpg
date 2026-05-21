from __future__ import annotations

import pygame

from states.base_state import BaseState
from ui.menu_view import MenuView


class MenuState(BaseState):
    def __init__(self, game: "Game") -> None:
        super().__init__(game)
        self.view = MenuView()

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.transition_to("world")
            if event.key == pygame.K_ESCAPE:
                self.game.running = False

    def render(self, surface: pygame.Surface) -> None:
        self.view.draw(surface)
