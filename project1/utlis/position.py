import tkinter as tk


def RootPosition(rt: tk.Tk, title: str, w, h: int):
    root = rt
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    w = w
    h = h
    x = (screenWidth - w) / 2
    y = (screenHeight - h) / 2

    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    root.title(title)