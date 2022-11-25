import tkinter as tk
from tkinter import ttk
from typing import Callable


class PanelMainButtons(tk.Frame):

    def __init__(self, parent, connect: Callable[[None], None]):
        tk.Frame.__init__(self, parent)

        self.grid(padx=4, pady=4)
        self.grid_columnconfigure((0, 1, 2, 3, 4), uniform="uniform", weight=1)

        self.buttonSave = ttk.Button(self, text='Save')
        self.buttonSave.grid(row=0, column=0, sticky=tk.E + tk.W)

        self.buttonSaveConnect = ttk.Button(self, text='Save Connect')
        self.buttonSaveConnect.grid(row=0, column=3, sticky=tk.E + tk.W)

        self.buttonConnect = ttk.Button(self, text='Connect', command=connect)
        self.buttonConnect.grid(row=0, column=4, sticky=tk.E + tk.W)
