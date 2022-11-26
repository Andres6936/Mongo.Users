import tkinter as tk
from tkinter import ttk


class User(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.labelUsername = ttk.Label(self, text="Username")
        self.labelUsername.grid(row=0, column=0, columnspan=2, sticky=tk.W)

        self.labelUsername = ttk.Label(self, text="Rol")
        self.labelUsername.grid(row=0, column=2, sticky=tk.E)

        self.buttonShowDetails = ttk.Button(self, text="Show Details")
        self.buttonShowDetails.grid(row=1, column=0)

        self.buttonUpdate = ttk.Button(self, text="Update")
        self.buttonUpdate.grid(row=1, column=1)

        self.buttonRemove = ttk.Button(self, text="Remove")
        self.buttonRemove.grid(row=1, column=2)
