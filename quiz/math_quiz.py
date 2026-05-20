from __future__ import annotations

import random

from quiz.question import Question


class MathQuizService:
    def __init__(self) -> None:
        self._rng = random.Random()

    def generate_question(self, difficulty: int = 1) -> Question:
        max_num = 10 + (difficulty - 1) * 5
        a = self._rng.randint(1, max_num)
        b = self._rng.randint(1, max_num)
        op = self._rng.choice(["+", "-"])

        if op == "+":
            answer = a + b
        else:
            answer = a - b

        return Question(prompt=f"{a} {op} {b} = ?", answer=str(answer), difficulty=difficulty)

    def validate_answer(self, question: Question, user_answer: str) -> bool:
        return question.answer.strip() == user_answer.strip()
