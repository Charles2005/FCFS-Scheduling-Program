import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import matplotlib

def fcfs_sched(arrival_time, burst_time):
    arrival_time = [int(i) for i in arrival_time.split()]
    burst_time = [int(i) for i in burst_time.split()]

    return arrival_time, burst_time


def gantt_chart(master):
    t = np.arange(0, 3, .01)
    fig, ax = plt.subplots(figsize=(7, 3), dpi=75)
    ax.plot(t, 2 * np.pi * t)
    canvas = FigureCanvasTkAgg(fig, master=master)
    canvas.draw()
    canvas.get_tk_widget().place(x=100, y=35)
