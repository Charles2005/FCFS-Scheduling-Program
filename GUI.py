from tkinter import *
from config import SIZE, TITLE, ALGO_NAME
from config import BG_COLOR, TEXT_BORDER_COLOR, ENTRY_BG_COLOR, TABLE_BG_COLOR
from config import ALGO_FONT_SIZE, LABEL_FONT_SIZE


class FCFS():
    def __init__(self):
        self.window_size = SIZE
        self.title = TITLE
        self.background_color = BG_COLOR

    def input_window(self):
        sc = Tk()
        # Windows size
        sc.geometry(self.window_size)
        sc.resizable(False, False)
        # Windows title
        sc.title(self.title)
        # Windows Background Color
        sc.config(background=self.background_color)
        # Function to initialize the window
        sc.mainloop()
