import tkinter as tk

from source.user.PanelButtons import PanelButtons
from source.user.PanelInfo import PanelInfo
from source.user.PanelListUsers import PanelListUsers
from source.user.PanelOptions import PanelOptions


class PanelUser(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=6)
        self.grid_columnconfigure((0, 1), weight=1)

        self.panelInfo = PanelInfo(self)
        self.panelInfo.grid(row=0, sticky=tk.W + tk.E)

        self.panelUserList = PanelListUsers(self)
        self.panelUserList.grid(row=1, column=0, sticky="nsew")

        self.panelOptions = PanelOptions(self)
        self.panelOptions.grid(row=1, column=1, sticky="nsew")

        self.panelButtons = PanelButtons(self)
        self.panelButtons.grid(row=2, columnspan=2, sticky=tk.W + tk.E)
