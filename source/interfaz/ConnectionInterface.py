import tkinter as tk

from source.interfaz.PanelMainButtons import PanelMainButtons
from source.interfaz.PanelURL import PanelURL
from source.interfaz.TabNewConnection import TabNewConnection


class ConnectionInterface(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.grid_columnconfigure((0), uniform="uniform", weight=1)
        self.grid_columnconfigure((0), uniform="uniform", weight=1)

        self.panelURL = PanelURL(self)
        self.panelURL.grid(row=0, sticky=tk.E + tk.W)

        self.tabNewConnection = TabNewConnection(self)
        self.tabNewConnection.grid(row=1, sticky=tk.E + tk.W)

        self.panelMainButtons = PanelMainButtons(self)
        self.panelMainButtons.grid(row=2, sticky=tk.E + tk.W)
