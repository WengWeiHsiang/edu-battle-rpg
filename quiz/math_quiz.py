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

        answer = a + b if op == "+" else a - b
        options, correct_index = self._build_options(answer, difficulty)
        return Question(
            prompt=f"{a} {op} {b} = ?",
            answer=str(answer),
            options=options,
            correct_index=correct_index,
            difficulty=difficulty,
        )

    def validate_answer(self, question: Question, user_answer: str) -> bool:
        return question.answer.strip() == user_answer.strip()

    def validate_choice(self, question: Question, choice_index: int) -> bool:
        return choice_index == question.correct_index

    def _build_options(self, answer: int, difficulty: int) -> tuple[tuple[str, str, str, str], int]:
        spread = max(2, difficulty + 1)
        distractors: set[int] = set()
        while len(distractors) < 3:
            delta = self._rng.randint(1, spread * 2)
            candidate = answer + delta if self._rng.random() < 0.5 else answer - delta
            if candidate != answer:
                distractors.add(candidate)
        option_values = [answer, *distractors]
        self._rng.shuffle(option_values)
        correct_index = option_values.index(answer)
        return tuple(str(v) for v in option_values), correct_index
