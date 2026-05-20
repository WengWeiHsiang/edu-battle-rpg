from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pygame


class BaseState:
    def __init__(self, game: "Game") -> None:
        self.game = game
        self._next_state: str | None = None

    @property
    def next_state(self) -> str | None:
        return self._next_state

    def transition_to(self, state_name: str) -> None:
        self._next_state = state_name

    def on_enter(self) -> None:
        self._next_state = None

    def on_exit(self) -> None:
        self._next_state = None

    def handle_event(self, event: "pygame.event.Event") -> None:
        pass

    def update(self, dt: float) -> None:
        pass

    def render(self, surface: "pygame.Surface") -> None:
        pass
