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
        # Rectangle
        my_canvas = Canvas(sc, width=720, height=480, bg=BG_COLOR, bd=0, highlightthickness=0)
        my_canvas.pack()
        my_canvas.create_rectangle(10, 468, 710, 465, fill=TEXT_BORDER_COLOR)
        my_canvas.create_rectangle(10, 13, 710, 10, fill=TEXT_BORDER_COLOR)
        # Label
        algo_title = Label(sc, text=ALGO_NAME, font=("Play", 48, "bold"), fg=TEXT_BORDER_COLOR, bg=BG_COLOR)
        algo_title.place(x=50, y=50)
        # Entry for arrival time
        arrival_time_label = Label(sc, text="Arrival Time: ", font=("Play", 14, "bold"), fg=TEXT_BORDER_COLOR, bg=BG_COLOR)
        arrival_time_label.place(x=300, y=120)
        arrival_time = Entry(sc, font=("Play", 24), bg=ENTRY_BG_COLOR, bd=5)
        arrival_time.place(x=300, y=150)
        # Entry for burst time
        burst_time_label = Label(sc, text="Burst Time: ", font=("Play", 14, "bold"), fg=TEXT_BORDER_COLOR,
                                   bg=BG_COLOR)
        burst_time_label.place(x=300, y=250)
        burst_time = Entry(sc, font=("Play", 24), bg=ENTRY_BG_COLOR, bd=5)
        burst_time.place(x=300, y=275)
        # Function to initialize the window
        sc.mainloop()

    def chart_window(self):
        root = Tk()
        # Windows size
        root.geometry(self.window_size)
        root.resizable(False, False)
        # Windows Title
        root.title(self.title)
        # Windows Background Color
        root.config(background=self.background_color)
        # Function to initialize the window
        root.mainloop()
