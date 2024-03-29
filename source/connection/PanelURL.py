import tkinter as tk
from tkinter import ttk


class PanelURL(tk.Frame):

    def __init__(self, parent, uri: tk.StringVar):
        tk.Frame.__init__(self, parent)

        self.grid(padx=4, pady=4)
        self.grid_columnconfigure((0, 1), uniform="uniform", weight=1)

        self.labelNewConnection = tk.Label(self, text="New Connection", font=("-size", 15))
        self.labelNewConnection.grid(row=0, column=0, columnspan=2, sticky=tk.W)

        self.labelDescription = tk.Label(self, text="Connect to a MongoDB deployment", font=("-size", 10),
                                         foreground="#979797")
        self.labelDescription.grid(row=1, column=0, columnspan=2, sticky=tk.W)

        self.labelURI = tk.Label(self, text='URI')
        self.labelURI.grid(row=2, column=0, sticky=tk.W)

        self.editConnectionString = ttk.Checkbutton(self, text='Edit Connection String', style="Switch.TCheckbutton")
        self.editConnectionString.grid(row=2, column=1, sticky=tk.E)

        self.entryURI = ttk.Entry(self, textvariable=uri)
        self.entryURI.grid(row=3, column=0, columnspan=2, sticky=tk.E + tk.W)

        self.labelAdvanceConnectionOptions = tk.Label(self, text="Advanced Connection Options")
        self.labelAdvanceConnectionOptions.grid(row=4, column=0, columnspan=2, sticky=tk.W)
