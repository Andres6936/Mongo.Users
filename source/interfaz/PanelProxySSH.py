import tkinter as tk

class PanelProxySSH(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.buttonNone = tk.Button(self, text="None")
        self.buttonNone.grid()

        self.buttonSSHWithPassword = tk.Button(self, text="SSH with Password")
        self.buttonSSHWithPassword.grid()

        self.buttonSSHWithIdentityFile = tk.Button(self, text="SSH with Identify File")
        self.buttonSSHWithIdentityFile.grid()

        self.buttonSocks5 = tk.Button(self, text="Socks5")
        self.buttonSocks5.grid()