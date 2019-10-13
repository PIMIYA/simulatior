import pyautogui
from actions import ActionType

# pyautogui.FAILSAFE = False
# screenWidth, screenHeight = pyautogui.size()
# pyautogui.moveTo(screenWidth / 2, screenHeight / 2, 0.35)

ids = [1, 2, 3]


def clear(obj: list):
    obj.clear()


print(ids)
clear(ids)
print(ids)
