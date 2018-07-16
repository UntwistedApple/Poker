# -*- coding: utf-8 -*-

import os
import shutil
import threading
from PIL import Image, ImageTk
import tkinter
import time


class Window:

    def __init__(self, driver):
        self.wnd = threading.Thread
        self.refresh_window_thread = threading.Thread
        self.panel = tkinter.Label
        self.driver = driver
        self.run = bool
        self.window_size = (960, 769)

    def create(self):
        tk = tkinter.Tk()
        frame = tkinter.Frame(tk, relief="ridge", borderwidth=2)
        frame.pack(fill="both", expand=1)
        img = ImageTk.PhotoImage(Image.open('default.png').resize(self.window_size))
        self.panel = tkinter.Label(tk, image=img)
        self.panel.pack(fill="both", expand="yes")
        tk.mainloop()

    def refresh_window(self):
        self.run = True
        ind = 1
        while self.run:
            try:
                if ind >= 13:
                    ind = 1
                name = 'sketch%d' % ind
                self.driver.save_screenshot('saves/'+name+'.png')
                if ind % 2 == 0:
                    if os.path.exists('sketch.png'):
                        os.remove('sketch.png')
                    shutil.copy('saves/'+name+'.png', 'sketch.png')
                img = ImageTk.PhotoImage(Image.open('saves/'+name+'.png').resize((960, 769)))
                self.panel.configure(image=img)
                self.panel.image = img
            except:
                pass
            time.sleep(1)
            ind += 1

    def start(self, ref=True):
        if ref:
            pass
            #self.wnd = threading.Thread(name='window', target=self.create)
            #self.wnd.start()
        #self.refresh_window_thread = threading.Thread(name='refresh_window', target=self.refresh_window)
        #self.refresh_window_thread.start()

    def get_refwnd(self):
        return self.refresh_window_thread

    def set_run(self, new_run=bool):
        self.run = new_run
