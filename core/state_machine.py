from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


class State(Protocol):
    def on_enter(self) -> None: ...
    def on_exit(self) -> None: ...
    def handle_event(self, event: object) -> None: ...
    def update(self, dt: float) -> None: ...
    def render(self, surface: object) -> None: ...
    @property
    def next_state(self) -> str | None: ...


@dataclass
class StateMachine:
    current: State

    def change_state(self, new_state: State) -> None:
        self.current.on_exit()
        self.current = new_state
        self.current.on_enter()

    def handle_event(self, event: object) -> None:
        self.current.handle_event(event)

    def update(self, dt: float) -> None:
        self.current.update(dt)

    def render(self, surface: object) -> None:
        self.current.render(surface)
