import tkinter as tk


class PanelGeneral(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.connectionStringScheme = tk.Label(self, text="Connection String Scheme")