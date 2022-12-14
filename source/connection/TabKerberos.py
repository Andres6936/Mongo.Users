import tkinter as tk
from tkinter import ttk


class TabKerberos(tk.Frame):
    """
    MongoDB Enterprise and MongoDB Atlas support Kerberos Authentication.
    Kerberos is an industry standard authentication protocol for large
    client/server systems that provides authentication using short-lived
    tokens that are called tickets.

    To use MongoDB with Kerberos, you must have a properly configured
    Kerberos deployment, configured Kerberos service principals for
    MongoDB, and a Kerberos user principal added to MongoDB.
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.grid_columnconfigure((0, 1, 2), uniform="uniform", weight=1)

        self.labelPrincipal = ttk.Label(self, text="Principal")
        self.labelPrincipal.grid(row=0, sticky=tk.W)

        self.entryPrincipal = ttk.Entry(self)
        self.entryPrincipal.grid(row=1)

        self.labelServiceName = ttk.Label(self, text="Service Name")
        self.labelServiceName.grid(row=2, sticky=tk.W)

        self.entryServiceName = ttk.Entry(self)
        self.entryServiceName.grid(row=3)

        self.labelCanonicalizeHostName = ttk.Label(self, text="Canonicalize Host Name")
        self.labelCanonicalizeHostName.grid(row=4, sticky=tk.W)

        self.buttonNone = ttk.Button(self, text="None")
        self.buttonNone.grid(row=5, column=0)

        self.buttonForward = ttk.Button(self, text="Forward")
        self.buttonForward.grid(row=5, column=1)

        self.buttonForwardReverse = ttk.Button(self, text="Forward and reverse")
        self.buttonForwardReverse.grid(row=5, column=2)

        self.labelServiceRealm = ttk.Label(self, text="Service Realm")
        self.labelServiceRealm.grid(row=6, sticky=tk.W)

        self.entryServiceRealm = ttk.Entry(self)
        self.entryServiceRealm.grid(row=7)
