import tkinter as tk
from tkinter import ttk

class PanelAdvanced(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), uniform="uniform", weight=1)

        self.labelReadPreference = tk.Label(self, text="Read Preference")
        self.labelReadPreference.grid(row=0, column=0)

        self.buttonDefault = ttk.Button(self, text="Default")
        self.buttonDefault.grid(row=1, column=0)

        self.buttonPrimary = ttk.Button(self, text="Primary")
        self.buttonPrimary.grid(row=1, column=1)

        self.buttonPrimaryPreferred = ttk.Button(self, text="Primary\nPreferred")
        self.buttonPrimaryPreferred.grid(row=1, column=2)

        self.buttonSecondary = ttk.Button(self, text="Secondary")
        self.buttonSecondary.grid(row=1, column=3)

        self.buttonSecondaryPreferred = ttk.Button(self, text="Secondary\nPreferred")
        self.buttonSecondaryPreferred.grid(row=1, column=4)

        self.buttonNearest = ttk.Button(self, text="Nearest")
        self.buttonNearest.grid(row=1, column=5)

        self.labelReplicaSetName = ttk.Label(self, text="Replica Set Name")
        self.labelReplicaSetName.grid(row=3, columnspan=3)

        self.entryReplicaSetName = ttk.Entry(self)
        self.entryReplicaSetName.grid(row=4, columnspan=3)

        self.labelDefaultAuthenticationDatabase = ttk.Label(self, text="Default Authentication Database")
        self.labelDefaultAuthenticationDatabase.grid(row=5, columnspan=3)

        self.entryDefaultAuthenticationDatabase = ttk.Entry(self)
        self.entryDefaultAuthenticationDatabase.grid(row=6, columnspan=3)
