from __future__ import annotations

from dataclasses import dataclass

import pygame

from battle.battle_controller import BattleController
from core.config import GameConfig
from core.state_machine import StateMachine
from quiz.math_quiz import MathQuizService
from states.battle_state import BattleState
from states.game_over_state import GameOverState
from states.menu_state import MenuState
from states.pause_state import PauseState
from states.reward_state import RewardState


@dataclass
class GameServices:
    battle: BattleController
    quiz: MathQuizService


class Game:
    def __init__(self, config: GameConfig | None = None) -> None:
        self.config = config or GameConfig()
        pygame.init()
        self.screen = pygame.display.set_mode((self.config.width, self.config.height))
        pygame.display.set_caption(self.config.title)
        self.clock = pygame.time.Clock()
        self.running = True

        self.services = GameServices(
            battle=BattleController(),
            quiz=MathQuizService(),
        )

        self.state_machine = StateMachine(MenuState(self))
        self.state_machine.current.on_enter()

    def change_state(self, state_name: str) -> None:
        mapping = {
            "menu": MenuState,
            "battle": BattleState,
            "reward": RewardState,
            "pause": PauseState,
            "game_over": GameOverState,
        }
        state_cls = mapping[state_name]
        self.state_machine.change_state(state_cls(self))

    def run(self) -> None:
        while self.running:
            dt = self.clock.tick(self.config.fps) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    continue
                self.state_machine.handle_event(event)

            self.state_machine.update(dt)
            next_state = self.state_machine.current.next_state
            if next_state:
                self.change_state(next_state)

            self.state_machine.render(self.screen)
            pygame.display.flip()

        pygame.quit()
