import tkinter as tk
from tkinter import ttk

from source.user.PanelFilters import PanelFilters
from source.user.PanelListRoles import PanelListRoles
from source.user.PanelListUsers import PanelListUsers


class TabManager(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.advanceConnectionOptions = ttk.Notebook(self)

        self.panelUserList = PanelListUsers(self.advanceConnectionOptions)
        self.advanceConnectionOptions.add(self.panelUserList, text="Users")

        self.panelRolesList = PanelListRoles(self.advanceConnectionOptions)
        self.advanceConnectionOptions.add(self.panelRolesList, text="Roles")

        self.advanceConnectionOptions.grid(row=0, column=0, padx=5, pady=5)

        self.panelFilter = PanelFilters(self)
        self.panelFilter.grid(row=1, column=0, sticky=tk.W + tk.E)
