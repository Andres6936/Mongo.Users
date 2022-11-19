import tkinter as tk
from tkinter import ttk

from source.interfaz.PanelAuthentication import PanelAuthentication


class PanelOpciones(tk.LabelFrame):

    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text='New Connection')

        self.config(background='white')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.advanceConnectionOptions = ttk.Notebook(self)

        self.tabGeneral = PanelAuthentication(self.advanceConnectionOptions)
        self.advanceConnectionOptions.add(self.tabGeneral, text="General")

        self.tabAuthentication = PanelAuthentication(self.advanceConnectionOptions)
        self.advanceConnectionOptions.add(self.tabAuthentication, text="Authentication")

        self.tabTLS_SSL = PanelAuthentication(self.advanceConnectionOptions)
        self.advanceConnectionOptions.add(self.tabTLS_SSL, text="TLS/SSL")

        self.tabProxy_SSH = tk.Frame(self.advanceConnectionOptions)
        self.advanceConnectionOptions.add(self.tabProxy_SSH, text="Proxy/SSH")

        self.tabInUseEncryption = tk.Frame(self.advanceConnectionOptions)
        self.advanceConnectionOptions.add(self.tabInUseEncryption, text="In-Use Encryption")

        self.tabAdvanced = tk.Frame(self.advanceConnectionOptions)
        self.advanceConnectionOptions.add(self.tabAdvanced, text="Advanced")

        self.advanceConnectionOptions.pack(padx=5, pady=5)

    def connect(self):
        print("Connect")
