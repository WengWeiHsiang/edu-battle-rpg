from __future__ import annotations

import pygame

from states.base_state import BaseState
from ui.menu_view import MenuView


class GameOverState(BaseState):
    def __init__(self, game: "Game") -> None:
        super().__init__(game)
        self.view = MenuView(title="Game Over", subtitle="Press Enter to return menu")

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.transition_to("menu")

    def render(self, surface: pygame.Surface) -> None:
        self.view.draw(surface)
