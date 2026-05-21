from __future__ import annotations


class FlashTransition:
    def __init__(self, duration: float = 0.45) -> None:
        self.duration = duration
        self.elapsed = 0.0
        self.active = False

    def start(self) -> None:
        self.elapsed = 0.0
        self.active = True

    def update(self, dt: float) -> bool:
        if not self.active:
            return False
        self.elapsed += dt
        if self.elapsed >= self.duration:
            self.active = False
            return True
        return False

    def alpha(self) -> int:
        if not self.active:
            return 0
        return int(min(255, (self.elapsed / self.duration) * 255))
