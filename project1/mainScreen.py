import tkinter as tk
from utlis.position import RootPosition
from mainView import EntryFrame


class MainScreen:
    def __init__(self, rt):
        self.root = rt
        # self.main_Screen_Frame = tk.Frame(self.root)
        RootPosition(self.root, 'Fv System v0.0.1', 820, 560)
        EntryFrame(self.root)


if __name__ == '__main__':
    root = tk.Tk()
    MainScreen(root)
    root.resizable(False, False)
    root.mainloop()
