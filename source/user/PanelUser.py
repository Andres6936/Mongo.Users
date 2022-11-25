import tkinter as tk
from tkinter import ttk


class PanelUser(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.button = ttk.Button(self, text="Next")
        self.button.grid(pady=80, padx=80)
