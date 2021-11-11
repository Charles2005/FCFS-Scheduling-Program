from GUI import FCFS
from config import SIZE, TITLE
from tkinter import *


def main():
    root = Tk()
    # Windows size
    root.geometry(SIZE)
    root.resizable(False, False)
    # Windows title
    root.title(TITLE)
    # FCFS Init
    fcfs = FCFS(root)
    fcfs.input_window()
    # Main loop
    root.mainloop()


if __name__ == '__main__':
    main()
