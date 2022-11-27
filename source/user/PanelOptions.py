import tkinter as tk
from tkinter import ttk


class PanelOptions(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.config(padx=20, pady=20)
        self.grid_columnconfigure((0), uniform="uniform", weight=1)

        self.labelUserManager = ttk.Label(self, text="User Manager")
        self.labelUserManager.grid(row=0, sticky=tk.W, pady=12)

        self.buttonCreateUser = ttk.Button(self, text="Create User")
        self.buttonCreateUser.grid(row=1, sticky=tk.W + tk.E)

        self.buttonUpdateUser = ttk.Button(self, text="Update User")
        self.buttonUpdateUser.grid(row=2, sticky=tk.W + tk.E, pady=8)

        self.buttonRemoveUser = ttk.Button(self, text="Remove User")
        self.buttonRemoveUser.grid(row=3, sticky=tk.W + tk.E)

        self.labelRolManager = ttk.Label(self, text="Rol Manager")
        self.labelRolManager.grid(row=4, sticky=tk.W, pady=12)

        self.buttonCreateRol = ttk.Button(self, text="Create Rol")
        self.buttonCreateRol.grid(row=5, sticky=tk.W + tk.E)

        self.buttonUpdateRol = ttk.Button(self, text="Update Rol")
        self.buttonUpdateRol.grid(row=6, sticky=tk.W + tk.E, pady=8)

        self.buttonRemoveRol = ttk.Button(self, text="Remove Rol")
        self.buttonRemoveRol.grid(row=7, sticky=tk.W + tk.E)
