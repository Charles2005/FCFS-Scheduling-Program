from tkinter import *
from config import SIZE, TITLE, ALGO_NAME
from config import BG_COLOR, TEXT_BORDER_COLOR, ENTRY_BG_COLOR, TABLE_BG_COLOR
from functions import fcfs_sched

class FCFS:
    def __init__(self, master):
        self.master = master

    def input_window(self):
        # Rectangle
        my_canvas = Canvas(self.master, width=720, height=480, bg=BG_COLOR, bd=0, highlightthickness=0)
        my_canvas.pack()
        my_canvas.create_rectangle(10, 468, 710, 465, fill=TEXT_BORDER_COLOR)
        my_canvas.create_rectangle(10, 13, 710, 10, fill=TEXT_BORDER_COLOR)
        # Label
        algo_title = Label(self.master, text=ALGO_NAME, font=("Play", 48, "bold"), fg=TEXT_BORDER_COLOR, bg=BG_COLOR)
        algo_title.place(x=50, y=50)
        # Entry for arrival time
        arrival_time_label = Label(self.master, text="Arrival Time e.g 1 3 5 7: ",
                                   font=("Play", 14, "bold"), fg=TEXT_BORDER_COLOR, bg=BG_COLOR)
        arrival_time_label.place(x=300, y=120)
        self.arrival_time = Entry(self.master, font=("Play", 24), bg=ENTRY_BG_COLOR, bd=5)
        self.arrival_time.place(x=300, y=150)
        # Entry for burst time
        burst_time_label = Label(self.master, text="Burst Time e.g 1 3 5 7: ",
                                 font=("Play", 14, "bold"), fg=TEXT_BORDER_COLOR, bg=BG_COLOR)
        burst_time_label.place(x=300, y=245)
        self.burst_time = Entry(self.master, font=("Play", 24), bg=ENTRY_BG_COLOR, bd=5)
        self.burst_time.place(x=300, y=275)
        # Submit Button
        submit_button = Button(self.master,
                               text="Submit",
                               font=("Play", 24),
                               bg=TEXT_BORDER_COLOR,
                               fg=TABLE_BG_COLOR,
                               command=self.chart_window)
        submit_button.place(x=415, y=350)

    def chart_window(self):
        print(fcfs_sched(self.arrival_time.get(), self.burst_time.get()))
        # Rectangle
        my_canvas = Canvas(Toplevel(self.master), width=720, height=480, bg=BG_COLOR, bd=0, highlightthickness=0)
        my_canvas.pack()
        my_canvas.create_rectangle(10, 468, 710, 465, fill=TEXT_BORDER_COLOR)
        my_canvas.create_rectangle(10, 13, 710, 10, fill=TEXT_BORDER_COLOR)
