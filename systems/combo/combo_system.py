from dataclasses import dataclass


@dataclass
class ComboSystem:
    streak: int = 0

    def on_correct(self) -> int:
        self.streak += 1
        return self.multiplier

    def reset(self) -> None:
        self.streak = 0

    @property
    def multiplier(self) -> int:
        return 1 + (self.streak // 3)

