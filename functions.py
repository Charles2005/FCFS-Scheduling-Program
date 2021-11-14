import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from config import TEXT_BORDER_COLOR, BG_COLOR, COLORS
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)


def fcfs_sched(process_name, arrival_time, burst_time, master):
    # Variables needed
    process_names = np.array([i for i in process_name.split()])
    sorted_process_names = []
    burst_values = np.array([int(i) for i in burst_time.split()])
    sorted_burst_values = []
    arrival_values = np.array([int(i) for i in arrival_time.split()])
    sorted_arrival_time = np.array(sorted(arrival_values))
    gantt_values = {arrival: burst for arrival, burst in zip(arrival_values, burst_values)}
    gantt_process = {values: names for values, names in zip(arrival_values, process_names)}
    complete_time = []

    # Creating Table
    if len(set(arrival_values)) <= 1:  # if all arrival elements were the same
        # Calculating complete time
        num = 0
        for i in burst_values:
            num += i
            complete_time.append(num)
        # Calculating turnaround time and waiting time
        turnaround_time = complete_time - arrival_values
        waiting_time = turnaround_time - burst_values
        # Creating DataFrame
        summ_table = pd.DataFrame({"Process": process_names,
                                   "Arrival Time": arrival_values,
                                   "Burst Time": burst_values,
                                   "Complete Time": complete_time,
                                   "Turnaround Time": turnaround_time,
                                   "Waiting Time": waiting_time })
    else:
        num1 = 0
        for num in sorted_arrival_time:
            sorted_burst_values.append(gantt_values[num])
        for num in sorted_burst_values:
            num1 += num
            complete_time.append(num1)
        for values in sorted_arrival_time:
            sorted_process_names.append(gantt_process[values])
        # Calculating turnaround time and waiting time
        turnaround_time = complete_time - sorted_arrival_time
        waiting_time = turnaround_time - sorted_burst_values
        # Creating DataFrame
        summ_table = pd.DataFrame({"Process": sorted_process_names,
                                   "Arrival Time": sorted_arrival_time,
                                   "Burst Time": sorted_burst_values,
                                   "Complete Time": complete_time,
                                   "Turnaround Time": turnaround_time,
                                   "Waiting Time": waiting_time})
    return summ_table



def gantt_chart(process_name, arrival_time, burst_time, master):
    # Variables needed
    process_names = np.array([i for i in process_name.split()])
    sorted_process_names = []
    burst_values = np.array([int(i) for i in burst_time.split()])
    sorted_burst_values = []
    arrival_values = np.array([int(i) for i in arrival_time.split()])
    sorted_arrival_time = sorted(arrival_values)
    gantt_values = {arrival: burst for arrival, burst in zip(arrival_values, burst_values)}
    gantt_process = {values: names for values, names in zip(arrival_values, process_names)}
    burst_values2 = []

    # Creating Gantt Chart
    if len(set(arrival_values)) <= 1:  # if all arrival elements were the same
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

        # For embedding the chart into window
        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.draw()
        canvas.get_tk_widget().place(x=100, y=20)
    else:
        num1 = 0
        for num in sorted_arrival_time:
            sorted_burst_values.append(gantt_values[num])
        for num in sorted_burst_values:
            burst_values2.append(num1)
            num1 += num
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

        # For embedding the chart into window
        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.draw()
        canvas.get_tk_widget().place(x=100, y=25)
