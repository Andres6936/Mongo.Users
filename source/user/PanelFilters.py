import tkinter as tk
from tkinter import ttk


class PanelFilters(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.grid(padx=8)
        self.grid_columnconfigure((0, 1), weight=1)

        self.labelUsername = ttk.Label(self, text="Filter by Username:")
        self.labelUsername.grid(row=0, column=0, sticky=tk.W)

        self.entryUsername = ttk.Entry(self)
        self.entryUsername.grid(row=0, column=1, sticky=tk.W + tk.E)

        self.labelRole = ttk.Label(self, text="Filter by Role:")
        self.labelRole.grid(row=1, column=0, sticky=tk.W)

        self.entryRole = ttk.Entry(self)
        self.entryRole.grid(row=1, column=1, sticky=tk.W + tk.E)
