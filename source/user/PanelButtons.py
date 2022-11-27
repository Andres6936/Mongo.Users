import tkinter as tk
from tkinter import ttk

from source.manager.TypeScene import TypeScene


class PanelButtons(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.config(pady=4, padx=4)
        self.grid_columnconfigure(0, uniform="uniform", weight=1)

        self.controller = controller

        self.buttonDisconnect = ttk.Button(self, text="Disconnect", command=self.disconnect)
        self.buttonDisconnect.grid(sticky=tk.E)

    def disconnect(self):
        self.controller.showScene(TypeScene.PANEL_CONNECTION)
