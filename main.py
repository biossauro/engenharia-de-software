import tkinter as tk
from src.thread_controller import ThreadController
from src.ui import UserInterface
from src.utils import *


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Timer Simulator')
        ui = UserInterface(self)
        controller = ThreadController()
        self.geometry('400x400')
        ui.set_controller(controller)
        ui.mainloop()


if __name__ == '__main__':
    cli_clear()
    app = App()
