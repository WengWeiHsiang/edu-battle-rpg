from dataclasses import dataclass


@dataclass
class Combatant:
    name: str
    max_hp: int
    attack: int
    hp: int | None = None

    def __post_init__(self) -> None:
        if self.hp is None:
            self.hp = self.max_hp

    @property
    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, amount: int) -> int:
        actual = max(0, amount)
        self.hp = max(0, self.hp - actual)
        return actual
