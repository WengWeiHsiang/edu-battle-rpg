from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pygame


class BaseState:
    def __init__(self, game: "Game") -> None:
        self.game = game
        self._state_action: tuple[str, str | None] | None = None

    @property
    def next_state(self) -> str | None:
        if self._state_action and self._state_action[0] == "change":
            return self._state_action[1]
        return None

    @property
    def state_action(self) -> tuple[str, str | None] | None:
        return self._state_action

    def transition_to(self, state_name: str) -> None:
        self._state_action = ("change", state_name)

    def push_state(self, state_name: str) -> None:
        self._state_action = ("push", state_name)

    def pop_state(self) -> None:
        self._state_action = ("pop", None)

    def on_enter(self) -> None:
        self._state_action = None

    def on_exit(self) -> None:
        self._state_action = None

    def handle_event(self, event: "pygame.event.Event") -> None:
        pass

    def update(self, dt: float) -> None:
        pass

    def render(self, surface: "pygame.Surface") -> None:
        pass
