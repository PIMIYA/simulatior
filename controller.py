import logging
import platform
import random
import time

import pyautogui as gui
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


# 如果有需要把滑鼠移動到左上角需要打開此設定
# 此設定是為了防止控制滑鼠的時候進入到無法控制的狀況而設置的防護措施，
# 只要將滑鼠手動控制到左上角則會強制解除控制
# gui.FAILSAFE = False


class Controller:
    SCROLL_GAP: int = 300
    SCROLL_INTERVAL: float = 0.25

    def __init__(self):
        self.xOffset = 6
        self.yOffset = 0
        self.driver: WebDriver = None

    def _dump_window_rect(self):
        if not self._is_driver_valid():
            return
        logging.info(f'{self.driver.get_window_rect()}')

    def _is_driver_valid(self) -> bool:
        if self.driver is None:
            logging.error('Driver is none.')
            return False
        return True

    def _get_element(self, element: str, index: int = 0) -> [WebElement, None]:
        """
        :param element: HTML Tag
        :param index:  index of element
        :return: WebElement if founded
        """
        if not self._is_driver_valid():
            return
        if not element:
            logging.error('element is empty or none.')
            return
        try:
            links = [link for link in self.driver.find_elements_by_tag_name(
                element)]
            if links:
                if index < 0:
                    index = random.randint(0, len(links) - 1)
                else:
                    index = index if len(links) > index else len(links) - 1
                logging.info(f'index of link: {index}')
                return links[index]
            else:
                logging.warning('link NOT found....')
        except NoSuchElementException:
            logging.error('NoSuchElementException')

    def _action_click_element(self, element: [WebElement, None]):
        if not self._is_driver_valid():
            return
        if element is None:
            logging.error('element is None')
            return
        loc = element.location
        for i in range(loc['y'] // self.SCROLL_GAP):
            self.driver.execute_script(f'window.scrollBy(0, {self.SCROLL_GAP})')
            time.sleep(self.SCROLL_INTERVAL)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.click(element)
        actions.perform()

    # region selenium
    def close_browser(self, duration: float = 0.3):
        if self.driver is not None:
            self.move_to_browser_close_button(duration=duration)
            self.driver.quit()
            self.driver = None

    def open_browser(self, url: [str, None] = None, x: int = 10, y: int = 10):
        _path = None
        system_name = platform.system()
        if system_name == "Windows":
            _path = "./bin/driver/chromedriver.exe"
        if system_name == "Darwin":
            _path = "./bin/driver/chromedriver"
        if _path is None:
            logging.error(f"platform {system_name} not supported")
            return

        if self.driver is None:
            _options = Options()
            _options.add_experimental_option("useAutomationExtension", False)
            _options.add_experimental_option(
                "excludeSwitches", ["enable-automation"])
            _options.add_argument(f"--window-position={x},{y}")
            self.driver = webdriver.Chrome(
                executable_path=_path, options=_options)
        if url is not None:
            self.driver.get(url)

    def maximize_window(self):
        if not self._is_driver_valid():
            return
        self.driver.maximize_window()

    def click_random_element(self, element: str):
        if not self._is_driver_valid():
            return
        link = self._get_element(element, -1)
        logging.info(link.get_attribute("href"))
        if link is None:
            logging.error(f"can not found any {element}")
            return
        self._action_click_element(element=link)

    def click_element(self, element: str, index: int):
        if not self._is_driver_valid():
            return
        link = self._get_element(element, index)
        logging.info(link.get_attribute("href"))
        if link is None:
            logging.error(f"can not found any {element}")
            return
        self._action_click_element(element=link)

    def drag_browser(self, offset_x: int = 0, offset_y: int = 0,
                     duration: float = 0.3):
        if not self._is_driver_valid():
            return
        rect = self.driver.get_window_rect()
        x, y, w, h = rect["x"], rect["y"], rect["width"], rect["height"]
        shift_x = w // 8
        target_x = self.xOffset + x + shift_x
        target_y = self.yOffset + y + 5
        self.mouse_move(x=target_x, y=target_y, duration=duration)
        gui.drag(xOffset=offset_x, yOffset=offset_y, duration=duration)

    def move_to_browser_close_button(self, offset_x: int = -20,
                                     offset_y: int = 10,
                                     duration: float = 0.3):
        if not self._is_driver_valid():
            return
        rect = self.driver.get_window_rect()
        x, y, w, h = rect["x"], rect["y"], rect["width"], rect["height"]
        target_x = self.xOffset + x + w + offset_x
        target_y = self.yOffset + y + offset_y
        self.mouse_move(x=target_x, y=target_y, duration=duration)

    def resize_browser(self, target_width: int, target_height: int,
                       move_duration: float = 0.3,
                       drag_duration: float = 0.3):
        if not self._is_driver_valid():
            return
        # target_width += 12
        # target_height += 3
        rect = self.driver.get_window_rect()
        x, y, w, h = rect["x"], rect["y"], rect["width"], rect["height"]
        target_x = self.xOffset + x + w - 10
        target_y = self.yOffset + y + h - 5
        self.mouse_move(x=target_x, y=target_y, duration=move_duration)
        target_x = x + target_width
        target_y = y + target_height
        gui.dragTo(x=target_x, y=target_y, duration=drag_duration)

    # endregion

    # region gui
    @staticmethod
    def mouse_move(x: float, y: float, duration: float = 0.3):
        gui.moveTo(x=x, y=y, duration=duration)

    @staticmethod
    def mouse_click(x: float, y: float, duration: float = 0.3):
        gui.click(x=x, y=y, duration=duration)

    @staticmethod
    def mouse_doubleclick(x: float, y: float, duration: float = 0.3):
        gui.doubleClick(x=x, y=y, duration=duration)

    @staticmethod
    def mouse_click_right(x: float, y: float, duration: float = 0.3):
        gui.rightClick(x=x, y=y, duration=duration)

    @staticmethod
    def key_press(key: str, presses: int = 1, interval: float = 0.0):
        gui.press(key, presses=presses, interval=interval)

    @staticmethod
    def key_typewrite(text: str, interval: float = 0.0):
        gui.typewrite(text, interval)

    @staticmethod
    def key_hotkey(key1: str, key2: str):
        gui.hotkey(key1, key2)

    # endregion
