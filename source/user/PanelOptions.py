import tkinter as tk
from tkinter import ttk


class PanelOptions(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.config(padx=20, pady=20)
        self.grid_columnconfigure((0), uniform="uniform", weight=1)

        self.buttonCreateUser = ttk.Button(self, text="Create User")
        self.buttonCreateUser.grid(row=0, sticky=tk.W + tk.E)

        self.buttonUpdateUser = ttk.Button(self, text="Update User")
        self.buttonUpdateUser.grid(row=1, sticky=tk.W + tk.E)

        self.buttonRemoveUser = ttk.Button(self, text="Remove User")
        self.buttonRemoveUser.grid(row=2, sticky=tk.W + tk.E)
