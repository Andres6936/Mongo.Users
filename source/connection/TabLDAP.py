import tkinter as tk
from tkinter import ttk


class TabLDAP(tk.Frame):
    """
    MongoDB Enterprise and MongoDB Atlas support LDAP Proxy
    Authentication proxy authentication through a Lightweight
    Directory Access Protocol (LDAP) service.
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.labelUsername = ttk.Label(self, text="Username")
        self.labelUsername.grid(row=0, sticky=tk.W)

        self.entryUsername = ttk.Entry(self)
        self.entryUsername.grid(row=1)

        self.labelPassword = ttk.Label(self, text="Password")
        self.labelPassword.grid(row=2, sticky=tk.W)

        self.entryPassword = ttk.Entry(self)
        self.entryPassword.grid(row=3)
