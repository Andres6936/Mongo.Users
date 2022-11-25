import tkinter as tk
from tkinter import ttk
from typing import Callable


class PanelGeneral(tk.Frame):
    def __init__(self, parent, port: tk.StringVar, hostname: tk.StringVar,
                 setPort: Callable[[str], None], setHostname: Callable[[str], None]):
        tk.Frame.__init__(self, parent)

        self.setPort = setPort
        self.setHostname = setHostname

        self.grid_columnconfigure((0, 1), uniform="uniform", weight=1)

        self.connectionStringScheme = tk.Label(self, text="Connection String Scheme")
        self.connectionStringScheme.grid(row=0, column=0, columnspan=3, sticky=tk.W)

        self.buttonConnectionMongo = ttk.Button(self, text="mongodb")
        self.buttonConnectionMongo.grid(row=1, column=0, sticky=tk.W + tk.E)

        self.buttonConnectionSRV = ttk.Button(self, text="mongodb+svr")
        self.buttonConnectionSRV.grid(row=1, column=1, sticky=tk.W + tk.E)

        self.buttonDescription = tk.Label(self, text="Standard Connection String Format. "
                                                     "The standard format of the MongoDB "
                                                     "connection URI is used to connect "
                                                     "to a MongoDB deployment: standalone,"
                                                     " replica set, or a sharded cluster.",
                                          wraplength="400px", font=("-size", 10), foreground="#979797")
        self.buttonDescription.grid(row=2, column=0, columnspan=3, sticky=tk.W)

        self.labelHostname = tk.Label(self, text="Host")
        self.labelHostname.grid(row=3, column=0, columnspan=3, sticky=tk.W)

        self.hostnameVar = tk.StringVar(value=f"{hostname.get()}:{port.get()}")
        self.hostnameVar.trace_add(mode="write", callback=self.updateHostnamePort)
        self.inputHostname = ttk.Entry(self, textvariable=self.hostnameVar)
        self.inputHostname.grid(row=4, column=0, columnspan=3, sticky=tk.W + tk.E)

        self.checkDirectConnection = ttk.Checkbutton(self, text="Direct Connection")
        self.checkDirectConnection.grid(row=5, column=0, columnspan=3, sticky=tk.W)

        self.labelDescriptionDirectConnection = tk.Label(self, font=("-size", 10), foreground="#979797",
                                                         text="Specifies whether to force dispatch all operations to the specified host.")
        self.labelDescriptionDirectConnection.grid(row=6, column=0, columnspan=3, sticky=tk.W)

    def updateHostnamePort(self, *args):
        (hostname, port) = self.hostnameVar.get().split(":")
        self.setPort(port)
        self.setHostname(hostname)
