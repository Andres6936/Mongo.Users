import tkinter as tk
from tkinter import ttk
from typing import Callable

from source.connection.PanelAdvanced import PanelAdvanced
from source.connection.PanelAuthentication import PanelAuthentication
from source.connection.PanelGeneral import PanelGeneral
from source.connection.PanelInUseEncryption import PanelInUseEncryption
from source.connection.PanelProxySSH import PanelProxySSH
from source.connection.PanelTLSSSL import PanelTLSSSL


class TabNewConnection(tk.Frame):

    def __init__(self, parent, port: tk.StringVar, hostname: tk.StringVar,
                 setPort: Callable[[str], None], setHostname: Callable[[str], None]):
        tk.Frame.__init__(self, parent)

        self.grid_columnconfigure((0), uniform="uniform", weight=1)
        self.grid_rowconfigure((0), uniform="uniform", weight=1)

        self.advanceConnectionOptions = ttk.Notebook(self)

        self.tabGeneral = PanelGeneral(self.advanceConnectionOptions, port=port, hostname=hostname,
                                       setPort=setPort, setHostname=setHostname)
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

        self.advanceConnectionOptions.grid(row=0, column=0, padx=5, pady=5)

    def connect(self):
        print("Connect")
