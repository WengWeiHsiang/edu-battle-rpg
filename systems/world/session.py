from __future__ import annotations

from dataclasses import dataclass, field

from entities.quiz_orb import QuizOrb
from entities.snake import Snake
from systems.combo import ComboSystem
from systems.enemy import EnemyManager, StationaryEnemy
from systems.quiz import QuizOrbSystem
from systems.snake import SnakeSystem


@dataclass
class WorldSession:
    cols: int = 24
    rows: int = 14
    snake: Snake = field(default_factory=lambda: Snake.create(8, 7, length=4))
    score: int = 0
    feedback: str = ""
    feedback_timer: float = 0.0
    orb: QuizOrb | None = None
    pending_encounter: dict[str, int | str] | None = None

    def __post_init__(self) -> None:
        self.combo_tracker = ComboSystem()
        self.snake_system = SnakeSystem(cols=self.cols, rows=self.rows)
        self.orb_system = QuizOrbSystem(cols=self.cols, rows=self.rows)
        self.enemy_manager = EnemyManager(cols=self.cols, rows=self.rows, min_enemies=3)
        self.enemy_manager.reset(blocked=set(self.snake.segments))
        self.orb = self.orb_system.spawn(blocked=set(self.snake.segments))

    @property
    def is_game_over(self) -> bool:
        return self.snake.length <= 1

    def set_direction(self, direction: tuple[int, int]) -> None:
        self.snake.set_direction(direction)

    def update(self, dt: float) -> None:
        moved = self.snake_system.update(self.snake, dt)
        blocked = set(self.snake.segments)
        if self.orb:
            blocked.add((self.orb.x, self.orb.y))
        self.enemy_manager.update(dt, blocked=blocked)
        if moved:
            self._handle_collisions()
        if self.feedback_timer > 0:
            self.feedback_timer -= dt
            if self.feedback_timer <= 0:
                self.feedback = ""

    def _handle_collisions(self) -> None:
        head = self.snake.head
        if self.orb and (head[0], head[1]) == (self.orb.x, self.orb.y):
            self.orb = self.orb_system.spawn(blocked=set(self.snake.segments))
            self.score += 5
            self._feedback("+5 Orb")

    @property
    def enemies(self) -> list[StationaryEnemy]:
        return self.enemy_manager.active_enemies

    def find_enemy_collision(self) -> StationaryEnemy | None:
        return self.enemy_manager.find_collision(self.snake.head)

    def begin_encounter(self, enemy: StationaryEnemy) -> None:
        removed = self.enemy_manager.remove_for_battle(enemy.enemy_id)
        if removed is None:
            return
        self.pending_encounter = {
            "id": removed.enemy_id,
            "name": removed.name,
            "max_hp": removed.max_hp,
            "attack": removed.attack,
        }

    def consume_encounter(self) -> dict[str, int | str] | None:
        data = self.pending_encounter
        self.pending_encounter = None
        return data

    def apply_battle_result(self, encounter_enemy_id: str | None, is_correct: bool) -> None:
        if is_correct:
            self.snake.grow(1)
            multiplier = self.combo_tracker.on_correct()
            self.score += 10 * multiplier
            self._feedback(f"Defeated! x{multiplier}")
        else:
            self.snake.shrink(1)
            self.combo_tracker.reset()
            self._feedback("Wrong! -1 length")
        self.enemy_manager.schedule_respawn()

    def remove_enemy_by_id(self, enemy_id: str) -> None:
        self.enemy_manager.remove_for_battle(enemy_id)

    def _feedback(self, text: str) -> None:
        self.feedback = text
        self.feedback_timer = 0.8

    def reset(self) -> None:
        self.snake = Snake.create(8, 7, length=4)
        self.score = 0
        self.combo_tracker.reset()
        self.feedback = ""
        self.feedback_timer = 0.0
        self.pending_encounter = None
        self.enemy_manager.reset(blocked=set(self.snake.segments))
        self.orb = self.orb_system.spawn(blocked=set(self.snake.segments))
