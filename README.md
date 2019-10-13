# Project auto art

兩個 full-hd 的螢幕轉 90 度合併，用 Selenium 去開瀏覽器 or [Hammer spoon](https://www.hammerspoon.org)
跑影片，在最上層
要可以操控 os

## Require

- Python 3.7+

### Create the python virtual environment

```sh
python3 -m venv env
```

## Package

- selenium
- PyAutoGUI

## TODO

- [x] load data from config file
- [x] move mouse
- [ ] function of action
  - [ ] mouse click to open web browser
  - [ ] type text and search by browser
  - [ ] random click result in search page
  - [ ] get the position of element on browser
  - [ ] move mouse to element on browser
  - [ ] click the link

## Reference

- [selenium](https://seleniumhq.github.io/selenium/docs/api/py/)

```py
>>> from selenium import webdriver
>>> from random import randint

>>> driver = webdriver.Firefox()
>>> driver.get('http://www.python.org')

>>> links = driver.find_elements_by_partial_link_text('')
>>> l = links[randint(0, len(links)-1)]
>>> l.click()
```
