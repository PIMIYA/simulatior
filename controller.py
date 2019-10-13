import logging
import platform
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement


class WebController:
    def __init__(self):
        self.driver: WebDriver = None

    def _get_element(self, element: str, index: int = 0) -> [WebElement, None]:
        """
        :param element: HTML Tag
        :param index:  index of element
        :return: WebElement if founded
        """
        if self.driver is None:
            logging.error('Driver is none.')
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
                return links[index]
            else:
                logging.warning('link NOT found....')
        except NoSuchElementException:
            logging.error('NoSuchElementException')

    def open_browser(self, url: [str, None] = None):
        _path = None
        system_name = platform.system()
        if system_name == 'Windows':
            _path = './bin/driver/chromedriver.exe'
        if system_name == 'Darwin':
            _path = './bin/driver/chromedriver'
        if _path is None:
            logging.error(f'platform {system_name} not supported')
            return

        if self.driver is None:
            _options = Options()
            _options.add_experimental_option('useAutomationExtension', False)
            _options.add_experimental_option(
                'excludeSwitches', ['enable-automation'])
            self.driver = webdriver.Chrome(
                executable_path=_path, options=_options)
            self.driver.implicitly_wait(3)
            self.driver.maximize_window()
        if url is not None:
            self.driver.get(url)

    def click_random_element(self, element: str):
        link = self._get_element(element, -1)
        logging.info(link.get_attribute('href'))
        if link is None:
            logging.error(f'can not found any {element}')
            return
        self.driver.execute_script('arguments[0].scrollIntoView();', link)
        link.click()

    def click_element(self, element: str, index: int):
        link = self._get_element(element, index)
        logging.info(link.get_attribute('href'))
        if link is None:
            logging.error(f'can not found any {element}')
            return
        self.driver.execute_script('arguments[0].scrollIntoView();', link)
        link.click()

    def quit(self):
        if self.driver is not None:
            self.driver.quit()


if __name__ == '__main__':
    from common import setting_logging

    setting_logging()
    controller = WebController()
    controller.open_browser('https://www.gamer.com.tw/')
    controller.click_element('a', 1)
    controller.click_element('a', 0)
    controller.quit()
