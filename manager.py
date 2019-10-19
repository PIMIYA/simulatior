import logging
import typing

from action_type import ActionType
from controller import Controller


class Manager:

    def __init__(self) -> object:
        self.controllers: typing.Dict[str, Controller] = {}

    def get_or_create(self, name: [str, None]) -> Controller:
        if not name:
            name = "main"
        if name not in self.controllers:
            self.controllers[name] = Controller()
        return self.controllers[name]

    def do_action(self, name: str, action: ActionType, args: dict):
        logging.info(f"Id: {name} Action: {action} Args: {args}")
        ctl = self.get_or_create(name)
        ctl.do_action(action=action, **args)
