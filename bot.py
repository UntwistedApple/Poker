# -*- coding: utf-8 -*-

import selenium
import time
import threading
import base64
from PIL import Image


class Bot:

    def __init__(self, mouse, driver):
        self.mouse = mouse
        self.refresh_window_thread = threading.Thread
        # self.window = window
        self.driver = driver

    def start(self):
        bot = threading.Thread(name='Bot', target=self.main)
        bot.start()

    def login(self):

        while True:
            try:
                bmail = self.driver.find_element_by_partial_link_text('Email')
                break
            except selenium.common.exceptions.NoSuchElementException:
                time.sleep(1)

        selenium.webdriver.common.action_chains.ActionChains(self.driver).click(bmail).perform()
        inputs = self.driver.find_elements_by_tag_name('input')
        action = selenium.webdriver.common.action_chains.ActionChains(self.driver)
        action.click(inputs[0])
        action.send_keys_to_element(inputs[0], 'spam-spasti@web.de').perform()

        action = selenium.webdriver.common.action_chains.ActionChains(self.driver)
        action.click(inputs[1])
        action.send_keys_to_element(inputs[1], 'spamspam').perform()

        bsignin = self.driver.find_element_by_css_selector('.ocp-form-button')
        action = selenium.webdriver.common.action_chains.ActionChains(self.driver)
        action.click(bsignin).perform()

    def start_game(self):

        btn1 = False
        btn2 = False

        while True:
            # ================================ close all the windows popping up ======================================
            try:
                action = selenium.webdriver.common.action_chains.ActionChains(self.driver)
                action.click(self.driver.find_element_by_css_selector('div.sprite_button:nth-child(1)')).perform()
                print('Found 1')
            except selenium.common.exceptions.NoSuchElementException:
                pass
            try:
                action = selenium.webdriver.common.action_chains.ActionChains(self.driver)
                action.click(self.driver.find_element_by_css_selector('div.element:nth-child(4)')).perform()
                print('Found 2')
            except selenium.common.exceptions.NoSuchElementException:
                pass
            try:
                action = selenium.webdriver.common.action_chains.ActionChains(self.driver)
                action.click(self.driver.find_element_by_css_selector('div.element:nth-child(5)')).perform()
                print('Found 3')
            except selenium.common.exceptions.NoSuchElementException:
                pass
            try:
                action = selenium.webdriver.common.action_chains.ActionChains(self.driver)
                action.click(self.driver.find_element_by_css_selector('div.sprite_button:nth-child(4)')).perform()
                print('Found 4')
            except selenium.common.exceptions.NoSuchElementException:
                pass
            try:
                action = selenium.webdriver.common.action_chains.ActionChains(self.driver)
                action.click(self.driver.find_element_by_css_selector('div.element: nth - child(4)')).perform()
                print('Found 5')
            except selenium.common.exceptions.NoSuchElementException:
                pass
            try:
                action = selenium.webdriver.common.action_chains.ActionChains(self.driver)
                action.click(self.driver.find_element_by_css_selector('div.sprite_button: nth - child(4)')).perform()
                print('Found 6')
            except selenium.common.exceptions.NoSuchElementException:
                pass
            # ========================================================================================================

            # =================================== click the play button ==============================================
            try:
                action = selenium.webdriver.common.action_chains.ActionChains(self.driver)
                button = self.driver.find_element_by_css_selector('button.btn:nth-child(5)')
                time.sleep(1)
                action.click(button).perform()
                btn1 = True
            except selenium.common.exceptions.NoSuchElementException:
                if btn1:
                    break
                print('Element 1 not found!')
            except selenium.common.exceptions.StaleElementReferenceException:
                break
            try:
                action = selenium.webdriver.common.action_chains.ActionChains(self.driver)
                button = self.driver.find_element_by_css_selector('button.clickable:nth-child(4)')
                time.sleep(1)
                action.click(button).perform()
                btn2 = True
            except selenium.common.exceptions.NoSuchElementException:
                if btn2:
                    break
                print('Element 2 not found!')
                time.sleep(2)
            except selenium.common.exceptions.StaleElementReferenceException:
                break
            # ========================================================================================================

        print('DONE')

    def getimg(self):
        ind = 0
        while True:
            ind += 1
            img = self.driver.find_element_by_css_selector('#GameSceneCanvasContainer > canvas:nth-child(1)').screenshot_as_png

            with open(r"saves/canvas%d.png" % ind, 'wb') as f:
                f.write(img)
            time.sleep(2)

        # return img

    def play(self):
        while True:
            try:
                self.getimg()
                break
            except selenium.common.exceptions.NoSuchElementException:
                time.sleep(1)

    def main(self):
        print('Yo what\'s up?')
        self.login()
        self.start_game()
        self.play()

        """ 
        run = True
        while run:
            print(threading.enumerate())
            for thread in threading.enumerate():
                if thread.name == 'refresh_window':
                    print(1)
                    self.refresh_window_thread = thread
                    self.window.set_run(False)
                    thread.join()
                    print(2)
                    break
            img = Image.open('sketch.png')
            img = img.convert('RGB')
            print(3)
            if img.getpixel((660, 170)) == (255, 255, 255):
                 print(4)
                 self.mouse.click((660, 170))
                print(5)
                time.sleep(1.5)
                self.mouse.type('Hallo')
                print(6)
                run = False
            img.close()
            self.window.start(False)
            time.sleep(3)
            """
