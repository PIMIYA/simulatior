import logging

from common.yaml_extension import yaml2obj
from typing import List, Type


class ActionData:
    """ Action data class """
    durationTime: float = 0.0

    def __init__(self, path: str) -> None:
        self.durationTime: float = 0.0
        self.executedActions: List = []
        self.actions: List[tuple] = yaml2obj(path=path)
        self.actions.sort(key=lambda x: x.time)

    def reset_actions(self):
        self.executedActions.clear()
        self.durationTime = 0.0

    def is_all_action_executed(self) -> bool:
        """ check the all actions is executed or not """
        return len(self.executedActions) == len(self.actions)

    def reset_if_all_action_executed(self):
        if self.is_all_action_executed():
            self.reset_actions()

    def add_duration_time(self, tick: float):
        self.durationTime += tick

    def get_next_action(self) -> [Type[tuple], None]:
        for index, step in enumerate(self.actions, start=0):
            if index in self.executedActions:
                continue
            if self.durationTime < step.time:
                continue
            self.executedActions.append(index)
            return step
        return None


def setting_logging():
    logging.basicConfig(
        format='%(asctime)-22s %(levelname)-8s %(message)s',
        level=logging.INFO)
