from enum import unique, Enum


@unique
class ActionType(Enum):
    OPEN_BROWSER = 100
    OPEN_URL = 101
    TRIGGER_ELEMENT_INDEX = 102
    TRIGGER_ELEMENT_RANDOM = 103
    DRAG_BROWSER_WIN = 104
    RESIZE_BROWSER_WIN = 105
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
