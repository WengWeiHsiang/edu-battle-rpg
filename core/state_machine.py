from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


class State(Protocol):
    def on_enter(self) -> None: ...
    def on_exit(self) -> None: ...
    def handle_event(self, event: object) -> None: ...
    def update(self, dt: float) -> None: ...
    def render(self, surface: object) -> None: ...


@dataclass
class StateMachine:
    _stack: list[State]

    @property
    def current(self) -> State:
        return self._stack[-1]

    def change_state(self, new_state: State) -> None:
        self.current.on_exit()
        self._stack[-1] = new_state
        self.current.on_enter()

    def push_state(self, new_state: State) -> None:
        self._stack.append(new_state)
        self.current.on_enter()

    def pop_state(self) -> None:
        if len(self._stack) <= 1:
            return
        self.current.on_exit()
        self._stack.pop()

    def handle_event(self, event: object) -> None:
        self.current.handle_event(event)

    def update(self, dt: float) -> None:
        self.current.update(dt)

    def render(self, surface: object) -> None:
        self.current.render(surface)
