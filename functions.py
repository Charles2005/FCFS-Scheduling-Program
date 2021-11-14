import numpy as np
import matplotlib.pyplot as plt
from pandastable import Table
from config import TEXT_BORDER_COLOR, BG_COLOR, COLORS
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)


def fcfs_sched(arrival_time, burst_time):
    arrival_time = [int(i) for i in arrival_time.split()]
    burst_time = [int(i) for i in burst_time.split()]



def gantt_chart(process_name, arrival_time, burst_time, master):
    # Values needed
    process_names = np.array([i for i in process_name.split()])
    burst_values = np.array([int(i) for i in burst_time.split()])
    arrival_values = np.array([int(i) for i in arrival_time.split()])
    sorted_arrival_time = sorted(arrival_values)
    gantt_values = {arrival: burst for arrival, burst in zip(arrival_values, burst_values)}
    gantt_process = {values: names for values, names in zip(arrival_values, process_names)}
    sorted_process_names = []
    sorted_burst_values = []
    burst_values2 = []

    # Creating Gantt Chart
    if len(set(arrival_values)) <= 1:
        num = 0
        for i in burst_values:
            burst_values2.append(num)
            num += i
        fig, ax = plt.subplots(figsize=(7, 4), dpi=75)
        fig.set_facecolor(BG_COLOR)
        ax.set_facecolor(TEXT_BORDER_COLOR)
        ax.set_xlabel("ms")
        ax.set_ylabel("Process")
        ax.set_xticks(burst_values2)
        ax.grid(True)
        ax.barh(process_names, burst_values, left=burst_values2, color=COLORS)

        # For embeding the chart into window
        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.draw()
        canvas.get_tk_widget().place(x=100, y=25)
    else:
        num1 = 0
        for num in sorted_arrival_time:
            sorted_burst_values.append(gantt_values[num])
        for i in sorted_burst_values:
            burst_values2.append(num1)
            num1 += i
        for values in sorted_arrival_time:
            sorted_process_names.append(gantt_process[values])
        # Creating gantt chart
        fig, ax = plt.subplots(figsize=(7, 4), dpi=75)
        fig.set_facecolor(BG_COLOR)
        ax.set_facecolor(TEXT_BORDER_COLOR)
        ax.set_xlabel("ms")
        ax.set_ylabel("Process")
        ax.set_xticks(burst_values2)
        ax.grid(True)
        ax.barh(sorted_process_names, sorted_burst_values, left=burst_values2, color=COLORS)

        # For embeding the chart into window
        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.draw()
        canvas.get_tk_widget().place(x=100, y=25)
