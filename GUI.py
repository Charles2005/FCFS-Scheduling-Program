from tkinter import *
from config import SIZE, TITLE, BG_COLOR


class FCFS():
    def __init__(self):
        self.window_size = SIZE
        self.title = TITLE
        self.background_color = BG_COLOR

    def run(self):
        sc = Tk()
        # Window size
        sc.geometry(self.window_size)
        sc.resizable(False, False)
        # Window title
        sc.title(self.title)
        # Window Background Color
        sc.config(background=self.background_color)
        # Function to initialize the window
        sc.mainloop()
