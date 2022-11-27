import tkinter as tk
from tkinter import ttk


class PanelButtons(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.config(pady=4, padx=4)
        self.grid_columnconfigure(0, uniform="uniform", weight=1)

        self.buttonDisconnect = ttk.Button(self, text="Disconnect")
        self.buttonDisconnect.grid(sticky=tk.E)
