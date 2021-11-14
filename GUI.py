from tkinter import *
from tkinter.ttk import Treeview, Style
from config import  ALGO_NAME
from config import BG_COLOR, TEXT_BORDER_COLOR, ENTRY_BG_COLOR, TABLE_BG_COLOR
from functions import fcfs_sched, gantt_chart


class FCFS:
    def __init__(self, master):
        self.master = master

    def input_window(self):
        # Rectangle
        my_canvas = Canvas(self.master, width=720, height=680, bg=BG_COLOR, bd=0, highlightthickness=0)
        my_canvas.pack()
        my_canvas.create_rectangle(10, 668, 710, 665, fill=TEXT_BORDER_COLOR)
        my_canvas.create_rectangle(10, 13, 710, 10, fill=TEXT_BORDER_COLOR)
        # Label
        algo_title = Label(self.master, text=ALGO_NAME, font=("Play", 48, "bold"), fg=TEXT_BORDER_COLOR, bg=BG_COLOR)
        algo_title.place(x=50, y=125)
        # Process entry
        process_label = Label(self.master, text="Process Name:",
                              font=("Play", 14, "bold"), fg=TEXT_BORDER_COLOR, bg=BG_COLOR)
        process_label.place(x=300, y=120)
        self.process_name = Entry(self.master, font=("Play", 24), bg=ENTRY_BG_COLOR, bd=5)
        self.process_name.place(x=300, y=150)
        # Entry for arrival time
        arrival_time_label = Label(self.master, text="Arrival Time e.g 1 3 5 7: ",
                                   font=("Play", 14, "bold"), fg=TEXT_BORDER_COLOR, bg=BG_COLOR)
        arrival_time_label.place(x=300, y=245)
        self.arrival_time = Entry(self.master, font=("Play", 24), bg=ENTRY_BG_COLOR, bd=5)
        self.arrival_time.place(x=300, y=275)
        # Entry for burst time
        burst_time_label = Label(self.master, text="Burst Time e.g 1 3 5 7: ",
                                 font=("Play", 14, "bold"), fg=TEXT_BORDER_COLOR, bg=BG_COLOR)
        burst_time_label.place(x=300, y=370)
        self.burst_time = Entry(self.master, font=("Play", 24), bg=ENTRY_BG_COLOR, bd=5)
        self.burst_time.place(x=300, y=400)
        # Submit Button
        submit_button = Button(self.master,
                               text="Submit",
                               font=("Play", 24),
                               bg=TEXT_BORDER_COLOR,
                               fg=TABLE_BG_COLOR,
                               command=self.chart_window)
        submit_button.place(x=415, y=475)

    def chart_window(self):
        chart_root = Toplevel(self.master)
        chart_root.geometry("720x720")
        chart_root.resizable(False, False)
        # Rectangle
        my_canvas = Canvas(chart_root, width=720, height=720, bg=BG_COLOR, bd=0, highlightthickness=0)
        my_canvas.pack()
        my_canvas.create_rectangle(10, 708, 710, 705, fill=TEXT_BORDER_COLOR)
        my_canvas.create_rectangle(10, 13, 710, 10, fill=TEXT_BORDER_COLOR)
        # Gantt Chart
        gantt_chart(self.process_name.get(), self.arrival_time.get(), self.burst_time.get(), my_canvas)

        # Table
        style = Style(chart_root)
        style.theme_use("clam")
        style.configure("Treeview",
                        background=TABLE_BG_COLOR,
                        fieldbackground=TABLE_BG_COLOR,
                        font=('Play', 11))  # Modify the font and background of the body
        style.map("Treeview", background=[('selected', TEXT_BORDER_COLOR)])

        style.configure("Treeview.Heading", font=('Play', 13, 'bold'))  # Modify the font of the headings

        summ_table = fcfs_sched(self.process_name.get(), self.arrival_time.get(), self.burst_time.get(), my_canvas)
        tv1 = Treeview(chart_root)
        tv1.place(x=100, y=340)
        tv1["column"] = list(summ_table.columns)
        tv1.column("#0", width=75, minwidth=25)
        tv1.column("Process", width=75, minwidth=25)
        tv1.column("Arrival Time", width=75, minwidth=25)
        tv1.column("Burst Time", width=75, minwidth=25)
        tv1.column("Complete Time", width=75, minwidth=25)
        tv1.column("Turnaround Time", width=75, minwidth=25)
        tv1.column("Waiting Time", width=75, minwidth=25)
        for column in tv1["column"]:
            tv1.heading(column, text=column)

        summ_table_values = summ_table.to_numpy().tolist()
        for row in summ_table_values:
            tv1.insert("", "end", values=row)
        treescrolly = Scrollbar(my_canvas, orient="vertical", command=tv1.yview)
        treescrollx = Scrollbar(my_canvas, orient="horizontal", command=tv1.xview)
        treescrollx.place(x=100, y=580)
        treescrolly.place(x=630, y=425)
        # Averages
        average_turnaround_time = round(sum(summ_table["Turnaround Time"]) / len(summ_table), 2)
        average_waiting_time = round(sum(summ_table["Waiting Time"]) / len(summ_table), 2)
        average_turnaround_time_label= Label(chart_root, text="Average Turnaround Time",
                                             font=("Play", 12, "bold"),
                                             fg=TEXT_BORDER_COLOR,
                                             bg=BG_COLOR)
        average_turnaround_time_label.place(x=175, y=590)
        average_TT = Text(chart_root,bg=ENTRY_BG_COLOR, font=("Play"), height=1, width=10)
        average_TT.insert(END, str(average_turnaround_time) + " ms")
        average_TT.place(x=250, y=620)
        average_waiting_time_label = Label(chart_root, text="Average Waiting Time",
                                              font=("Play", 12, "bold"),
                                              fg=TEXT_BORDER_COLOR,
                                              bg=BG_COLOR)
        average_waiting_time_label.place(x=400, y=590)
        average_WT = Text(chart_root,bg=ENTRY_BG_COLOR,font=("Play"), height=1, width=10)
        average_WT.insert(END, str(average_waiting_time) + " ms")
        average_WT.place(x=450, y=620)



