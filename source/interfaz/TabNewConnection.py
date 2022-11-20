import tkinter as tk
from tkinter import ttk

from source.interfaz.PanelAdvanced import PanelAdvanced
from source.interfaz.PanelAuthentication import PanelAuthentication
from source.interfaz.PanelGeneral import PanelGeneral
from source.interfaz.PanelInUseEncryption import PanelInUseEncryption
from source.interfaz.PanelProxySSH import PanelProxySSH
from source.interfaz.PanelTLSSSL import PanelTLSSSL


class TabNewConnection(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.advanceConnectionOptions = ttk.Notebook(self)

        self.tabGeneral = PanelGeneral(self.advanceConnectionOptions)
        self.advanceConnectionOptions.add(self.tabGeneral, text="General")

        self.tabAuthentication = PanelAuthentication(self.advanceConnectionOptions)
        self.advanceConnectionOptions.add(self.tabAuthentication, text="Authentication")

        self.tabTLS_SSL = PanelTLSSSL(self.advanceConnectionOptions)
        self.advanceConnectionOptions.add(self.tabTLS_SSL, text="TLS/SSL")

        self.tabProxy_SSH = PanelProxySSH(self.advanceConnectionOptions)
        self.advanceConnectionOptions.add(self.tabProxy_SSH, text="Proxy/SSH")

        self.tabInUseEncryption = PanelInUseEncryption(self.advanceConnectionOptions)
        self.advanceConnectionOptions.add(self.tabInUseEncryption, text="In-Use Encryption")

        self.tabAdvanced = PanelAdvanced(self.advanceConnectionOptions)
        self.advanceConnectionOptions.add(self.tabAdvanced, text="Advanced")

        self.advanceConnectionOptions.pack(padx=5, pady=5)

    def connect(self):
        print("Connect")
