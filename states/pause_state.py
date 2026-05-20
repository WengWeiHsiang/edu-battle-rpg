from __future__ import annotations

import pygame

from states.base_state import BaseState
from ui.menu_view import MenuView


class PauseState(BaseState):
    def __init__(self, game: "Game") -> None:
        super().__init__(game)
        self.view = MenuView(title="Paused", subtitle="Press P to back battle")

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            self.transition_to("battle")

    def render(self, surface: pygame.Surface) -> None:
        self.view.draw(surface)
