import tkinter as tk

from source.connection.PanelMainButtons import PanelMainButtons
from source.connection.PanelURL import PanelURL
from source.connection.TabNewConnection import TabNewConnection
from source.manager.TypeScene import TypeScene


class ConnectionInterface(tk.Frame):
    """
    Central panel used for controller the type of connection to MongoDB
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.port = tk.StringVar(value="27017")
        self.password = tk.StringVar(value='')
        self.username = tk.StringVar(value='')
        self.hostname = tk.StringVar(value="hostname")
        self.uri = tk.StringVar(value=f"mongodb://{self.hostname.get()}:{self.port.get()}/")

        self.username.trace_add(mode="write", callback=self.updateVariable)
        self.password.trace_add(mode="write", callback=self.updateVariable)

        self.grid_columnconfigure((0), uniform="uniform", weight=1)
        self.grid_columnconfigure((0), uniform="uniform", weight=1)

        self.panelURL = PanelURL(self, uri=self.uri)
        self.panelURL.grid(row=0, sticky=tk.E + tk.W)

        self.tabNewConnection = TabNewConnection(
            self, port=self.port, hostname=self.hostname, username=self.username,
            password=self.password, setPort=self.setPort, setHostname=self.setHostname)
        self.tabNewConnection.grid(row=1, sticky=tk.E + tk.W)

        self.panelMainButtons = PanelMainButtons(self, connect=self.connect)
        self.panelMainButtons.grid(row=2, sticky=tk.E + tk.W)

    def connect(self) -> None:
        self.controller.showScene(TypeScene.PANEL_MANAGER)

    def setPort(self, value) -> None:
        self.port.set(value)
        self.updateVariable()

    def setHostname(self, value) -> None:
        self.hostname.set(value)
        self.updateVariable()

    def updateVariable(self, *args) -> None:
        if len(self.username.get()) > 0 or len(self.password.get()) > 0:
            self.uri.set(
                f"mongodb://{self.username.get()}:{self.password.get()}@{self.hostname.get()}:{self.port.get()}/")
        else:
            self.uri.set(f"mongodb://{self.hostname.get()}:{self.port.get()}/")
