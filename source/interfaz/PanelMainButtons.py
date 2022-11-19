import tkinter as tk

class PanelMainButtons(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.config(padx=4, pady=4)
        self.columnconfigure(0, weight=1)

        self.buttonSave = tk.Button(self, text='Save')
        self.buttonSave.grid(row=0, column=0, sticky=tk.E + tk.W)

        self.buttonSaveConnect = tk.Button(self, text='Save Connect')
        self.buttonSaveConnect.grid(row=0, column=1, sticky=tk.E + tk.W)

        self.buttonConnect = tk.Button(self, text='Connect')
        self.buttonConnect.grid(row=0, column=2, sticky=tk.E + tk.W)
