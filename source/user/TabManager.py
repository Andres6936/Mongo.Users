import tkinter as tk
from tkinter import ttk

from source.user.PanelListUsers import PanelListUsers


class TabManager(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.advanceConnectionOptions = ttk.Notebook(self)

        self.panelUserList = PanelListUsers(self.advanceConnectionOptions)
        self.advanceConnectionOptions.add(self.panelUserList, text="Users")

        self.advanceConnectionOptions.grid(row=0, column=0, padx=5, pady=5)
