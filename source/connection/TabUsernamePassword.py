import tkinter as tk
from tkinter import ttk


class TabUsernamePassword(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.grid_columnconfigure((0, 1, 2), uniform="uniform", weight=1)

        self.labelUsername = ttk.Label(self, text="Username")
        self.labelUsername.grid(row=0, sticky=tk.W)

        self.entryUsername = ttk.Entry(self)
        self.entryUsername.grid(row=1)

        self.labelPassword = ttk.Label(self, text="Password")
        self.labelPassword.grid(row=2, sticky=tk.W)

        self.entryPassword = ttk.Entry(self)
        self.entryPassword.grid(row=3)

        self.labelAuthenticationDatabase = ttk.Label(self, text="Authentication Database")
        self.labelAuthenticationDatabase.grid(row=4, sticky=tk.W)

        self.entryAuthenticationDatabase = ttk.Entry(self)
        self.entryAuthenticationDatabase.grid(row=5)

        self.labelAuthenticationMechanism = ttk.Label(self, text="Authentication Mechanism")
        self.labelAuthenticationMechanism.grid(row=6, sticky=tk.W)

        self.buttonDefault = ttk.Button(self, text="Default")
        self.buttonDefault.grid(row=7, column=0)

        self.buttonSCRAM_SHA1 = ttk.Button(self, text="SCRAM-SHA-1")
        self.buttonSCRAM_SHA1.grid(row=7, column=1)

        self.buttonSCRAM_SHA256 = ttk.Button(self, text="SCRAM-SHA-256")
        self.buttonSCRAM_SHA256.grid(row=7, column=2)
