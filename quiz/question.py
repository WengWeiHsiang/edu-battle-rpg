from dataclasses import dataclass


@dataclass(frozen=True)
class Question:
    prompt: str
    answer: str
    options: tuple[str, str, str, str]
    correct_index: int
    difficulty: int = 1
