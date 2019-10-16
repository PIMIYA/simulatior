import logging
from enum import Enum, unique
import pyautogui as autogui

from controller import Controller


@unique
class ActionType(Enum):
    OPEN_BROWSER = 100
    OPEN_URL = 101
    TRIGGER_ELEMENT_INDEX = 102
    TRIGGER_ELEMENT_RANDOM = 103
    MOUSE_MOVE = 200
    MOUSE_CLICK = 201
    MOUSE_DOUBLECLICK = 202
    MOUSE_CLICK_RIGHT = 203
    KEY_PRESS = 300
    KEY_TYPEWRITE = 301
    KEY_HOTKEY = 302

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class Actor:
    def __init__(self):
        self._actionMethods = {
            ActionType.OPEN_BROWSER: self.open_browser,
            ActionType.OPEN_URL: self.open_url,
            ActionType.TRIGGER_ELEMENT_INDEX: self.trigger_element_index,
            ActionType.TRIGGER_ELEMENT_RANDOM: self.trigger_element_random,
            ActionType.MOUSE_MOVE: self.mouse_move,
            ActionType.MOUSE_CLICK: self.mouse_click,
            ActionType.MOUSE_DOUBLECLICK: self.mouse_doubleclick,
            ActionType.MOUSE_CLICK_RIGHT: self.mouse_click_right,
            ActionType.KEY_PRESS: self.key_press,
            ActionType.KEY_TYPEWRITE: self.key_typewrite,
            ActionType.KEY_HOTKEY: self.key_hotkey,
        }
        self._web = Controller()

    def do_action(self, step) -> bool:
        logging.info(f'run {step}')
        if not ActionType.has_value(step.type):
            logging.warning(f'{step.type} not int ActionType')
            return False
        action_type = ActionType(step.type)
        if action_type not in self._actionMethods:
            logging.warning(f'{step.type} not int methods')
            return False
        logging.info(f'{step.args}')
        args = {} if step.args is None else step.args._asdict()
        self._actionMethods[action_type](**args)
        return True

    def open_browser(self, **kwargs):
        x = kwargs['x'] if 'x' in kwargs else 10
        y = kwargs['y'] if 'y' in kwargs else 10
        self._web.open_browser(x=x, y=y)

    def open_url(self, **kwargs):
        url = kwargs['url'] if 'url' in kwargs else None
        self._web.open_browser(url)

    def trigger_element_index(self, **kwargs):
        element = kwargs['element'] if 'element' in kwargs else ''
        index = kwargs['index'] if 'index' in kwargs else 0
        self._web.click_element(element=element, index=index)

    def trigger_element_random(self, **kwargs):
        element = kwargs['element'] if 'element' in kwargs else ''
        self._web.click_random_element(element=element)

    def mouse_move(self, **kwargs):
        x = kwargs['x']
        y = kwargs['y']
        duration = kwargs['duration'] if 'duration' in kwargs else 0.2
        autogui.moveTo(x=x, y=y, duration=duration)

    def mouse_click(self, **kwargs):
        logging.info(f'mouse_click {kwargs}')
        x = kwargs['x']
        y = kwargs['y']
        autogui.click(x=x, y=y)

    def mouse_doubleclick(self, **kwargs):
        logging.info(f'mouse_doubleclick {kwargs}')
        x = kwargs['x']
        y = kwargs['y']
        autogui.doubleClick(x=x, y=y)

    def mouse_click_right(self, **kwargs):
        logging.info(f'mouse_click_right {kwargs}')
        x = kwargs['x']
        y = kwargs['y']
        autogui.rightClick(x=x, y=y)

    def key_press(self, **kwargs):
        logging.info(f'key_press {kwargs}')
        key = kwargs['key']
        presses = kwargs['presses'] if 'presses' in kwargs else 1
        interval = kwargs['interval'] if 'interval' in kwargs else 0.0
        autogui.press(key, presses=presses, interval=interval)

    def key_typewrite(self, **kwargs):
        logging.info(f'key_typewrite {kwargs}')
        text = kwargs['text']
        interval = kwargs['interval']
        autogui.typewrite(text, interval)

    def key_hotkey(self, **kwargs):
        logging.info(f'key_hotkey {kwargs}')
        key1 = kwargs['key1']
        key2 = kwargs['key2']
        autogui.hotkey(key1, key2)
