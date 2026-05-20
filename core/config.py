from dataclasses import dataclass


@dataclass(frozen=True)
class GameConfig:
    width: int = 960
    height: int = 540
    fps: int = 60
    title: str = "Edu Battle RPG"
