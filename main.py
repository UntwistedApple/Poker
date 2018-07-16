# -*- coding: utf-8 -*-

import threading
import mouse as ms
import os
import shutil
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import window as wnd
import bot as b


if os.path.exists('sketch.png'):
    os.remove('sketch.png')
shutil.copy('default.png', 'sketch.png')
options = Options()
# options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options, executable_path='')
driver.set_window_size(1366, 768)  # 1354 x 687
driver.get('https://standalone-proxy-prod.wsop.playtika.com/355-39865c8869b30965052f6ebfc21b98bc2044f586/index.html')  # https://www.pointerpointer.com/
# window = wnd.Window(driver)
# window.start()
mouse = ms.Mouse(driver)
bot = b.Bot(mouse, driver)
bot.main()
# bot.start()
# print('CLICKED')
# mouse.click((953, 550))

# driver.quit()
