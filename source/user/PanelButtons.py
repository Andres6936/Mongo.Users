import tkinter as tk
from tkinter import ttk

from source.manager.TypeScene import TypeScene


class PanelButtons(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.config(pady=4, padx=4)
        self.grid_columnconfigure((0, 1), uniform="uniform", weight=1)

        self.controller = controller

        self.buttonApplyFilter = ttk.Button(self, text="Apply Filter")
        self.buttonApplyFilter.grid(row=0, column=0, sticky=tk.W)

        self.buttonDisconnect = ttk.Button(self, text="Disconnect", command=self.disconnect)
        self.buttonDisconnect.grid(row=0, column=1, sticky=tk.E)

    def disconnect(self):
        self.controller.showScene(TypeScene.PANEL_CONNECTION)
