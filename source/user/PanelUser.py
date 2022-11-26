import tkinter as tk

from source.user.PanelListUsers import PanelListUsers
from source.user.PanelOptions import PanelOptions


class PanelUser(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.grid_columnconfigure((0, 1), uniform="uniform", weight=1)

        self.panelUserList = PanelListUsers(self)
        self.panelUserList.grid(row=0, column=0)

        self.panelOptions = PanelOptions(self)
        self.panelOptions.grid(row=0, column=1, sticky=tk.E + tk.N)
