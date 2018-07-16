# -*- coding: utf-8 -*-

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import threading


class Mouse:

    def __init__(self, driver):
        # self.window = window
        self.driver = driver

    def click(self, coordinates):
        print('clicking...')
        # self.window.set_run(False)
        # threads = threading.enumerate()
        # for thread in threads:
        #    if thread.name == 'refresh_window':
        #        thread.join()
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_by_offset(coordinates[0], coordinates[1])
        action.click()
        action.move_by_offset(-coordinates[0], -coordinates[1])
        action.perform()
        # self.window.start(False)

    def type(self, keys):
        print('typing...')
        # self.window.set_run(False)
        # threads = threading.enumerate()
        # for thread in threads:
        #    if thread.name == 'refresh_window':
        #        thread.join()
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.send_keys(Keys.TAB)
        # self.window.start(False)
