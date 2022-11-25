import tkinter as tk
from tkinter import ttk

class PanelProxySSH(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.grid_columnconfigure((0, 1, 2, 3), uniform="uniform", weight=1)

        self.labelTitle = ttk.Label(self, text="SSH Tunnel/Proxy Method")
        self.labelTitle.grid(row=0, column=0)

        self.buttonNone = ttk.Button(self, text="None")
        self.buttonNone.grid(row=1, column=0)

        self.buttonSSHWithPassword = ttk.Button(self, text="SSH with Password")
        self.buttonSSHWithPassword.grid(row=1, column=1)

        self.buttonSSHWithIdentityFile = ttk.Button(self, text="SSH with Identify File")
        self.buttonSSHWithIdentityFile.grid(row=1, column=2)

        self.buttonSocks5 = ttk.Button(self, text="Socks5")
        self.buttonSocks5.grid(row=1, column=3)
