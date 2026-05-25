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
from states.world_state import WorldState
from systems.battle import EncounterProfileService
from systems.world import WorldSession
from systems.difficulty import EducationalDifficultyScaler


@dataclass
class GameServices:
    battle: BattleController
    quiz: MathQuizService
    world: WorldSession
    difficulty: EducationalDifficultyScaler
    encounter_profiles: EncounterProfileService


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
            world=WorldSession(),
            difficulty=EducationalDifficultyScaler(),
            encounter_profiles=EncounterProfileService(),
        )

        self.state_machine = StateMachine([MenuState(self)])
        self.state_machine.current.on_enter()

    def change_state(self, state_name: str) -> None:
        mapping = {
            "menu": MenuState,
            "world": WorldState,
            "battle": BattleState,
            "reward": RewardState,
            "pause": PauseState,
            "game_over": GameOverState,
        }
        state_cls = mapping[state_name]
        self.state_machine.change_state(state_cls(self))

    def push_state(self, state_name: str) -> None:
        mapping = {
            "menu": MenuState,
            "world": WorldState,
            "battle": BattleState,
            "reward": RewardState,
            "pause": PauseState,
            "game_over": GameOverState,
        }
        self.state_machine.push_state(mapping[state_name](self))

    def pop_state(self) -> None:
        self.state_machine.pop_state()

    def run(self) -> None:
        while self.running:
            dt = self.clock.tick(self.config.fps) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    continue
                self.state_machine.handle_event(event)

            self.state_machine.update(dt)
            action = getattr(self.state_machine.current, "state_action", None)
            if action:
                action_name, state_name = action
                if action_name == "change" and state_name:
                    self.change_state(state_name)
                elif action_name == "push" and state_name:
                    self.push_state(state_name)
                elif action_name == "pop":
                    self.pop_state()

            self.state_machine.render(self.screen)
            pygame.display.flip()

        pygame.quit()
