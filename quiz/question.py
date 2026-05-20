from dataclasses import dataclass


@dataclass(frozen=True)
class Question:
    prompt: str
    answer: str
    difficulty: int = 1
