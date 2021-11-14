"""
COLORS
#343C55 - Text and border color
#B0D0D3 - Background Color
#DEC9C9 - Entry Background Color
#CCCCCC - For Table Background Color
"""
import matplotlib.pyplot as plt
import numpy as np

SIZE = "720x680"
TITLE = "FCFS Scheduling Algorithm"
ALGO_NAME = "FIRST\nCOME\nFIRST\nSERVE"
BG_COLOR = "#B0D0D3"
TEXT_BORDER_COLOR = "#343C55"
ENTRY_BG_COLOR = "#DEC9C9"
TABLE_BG_COLOR = "#CCCCCC"
COLORS = plt.get_cmap('plasma')(
    np.linspace(0.15, 0.85, 3))
