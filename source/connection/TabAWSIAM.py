import tkinter as tk
from tkinter import ttk


class TabAWSIAM(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.labelKeyID = ttk.Label(self, text="AWS Access Key Id")
        self.labelKeyID.grid(row=0, sticky=tk.W)

        self.entryKeyID = ttk.Entry(self)
        self.entryKeyID.grid(row=1)

        self.labelAccessKey = ttk.Label(self, text="AWS Secret Access Key")
        self.labelAccessKey.grid(row=2, sticky=tk.W)

        self.entryAccessKey = ttk.Entry(self)
        self.entryAccessKey.grid(row=3)

        self.labelSessionToken = ttk.Label(self, text="AWS Session Token")
        self.labelSessionToken.grid(row=0, sticky=tk.W)

        self.entrySessionToken = ttk.Entry(self)
        self.entrySessionToken.grid(row=1)
