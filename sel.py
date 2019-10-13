import logging
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
# import pyautogui


def config():
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')


def click_random_link(driver, target):
    logging.info('clicking random link')
    try:
        links = [link for link in driver.find_elements_by_tag_name(
            target) if link.is_displayed()]
        logging.info('get all links')
        if links:
            logging.info('random links from {0}'.format(len(links)))
            ln = links[random.randint(0, len(links) - 1)]
            logging.info('get link')
            driver.execute_script('arguments[0].scrollIntoView();', ln)
            logging.info(ln.get_attribute("href"))
            # ln.click()
        else:
            logging.warning('link NOT found....')
    except NoSuchElementException:
        logging.warning('link NOT found....')


def run(driver):
    wpos = driver.get_window_position()
    xShiftPixel = 5
    yShiftPixel = 3 + driver.execute_script(
        'return window.outerHeight - window.innerHeight;')

    targetUrl = 'https://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.action_chains.html#module-selenium.webdriver.common.action_chains'
    driver.get(targetUrl)
    click_random_link(driver, 'a')
    # menu = driver.find_element_by_css_selector(".viewcode-link")
    # location = menu.location
    # print(location)
    # x = location['x'] + xShiftPixel
    # y = location['y'] + yShiftPixel
    # print(x, y)
    # pyautogui.moveTo(x, y, 0.7, pyautogui.easeOutQuad)
    # pyautogui.click(x=x, y=y)


config()
mainDriver = webdriver.Chrome(executable_path='./bin/driver/chromedriver.exe')
mainDriver.implicitly_wait(3)
mainDriver.maximize_window()
run(mainDriver)
