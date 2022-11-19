import tkinter as tk

from source.interfaz.PanelMainButtons import PanelMainButtons
from source.interfaz.TabNewConnection import TabNewConnection


class ConnectionInterface(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.tabNewConnection = TabNewConnection(self)
        self.tabNewConnection.grid(row=0, column=0, padx=4, pady=4, sticky=tk.E + tk.W)

        self.panelMainButtons = PanelMainButtons(self)
        self.panelMainButtons.grid(row=1, column=0, sticky=tk.E + tk.W)

        self.pack()
