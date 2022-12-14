import tkinter as tk

from source.connection.ConnectionInterface import ConnectionInterface
from source.manager.TypeScene import TypeScene
from source.user.PanelUser import PanelUser


class SceneManager(tk.Tk):
    """
    The scene manager used for show the current scene of program,
    currently there are 2 scenes, for defect the current scene
    is of new connection.

    - The first scene is the new connection for MongoDB
    - The second scene is the view of users and roles of MongoDB

    Note: The policy for initialize the scene is lazy evaluation
    """

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.call("source", "azure.tcl")
        self.call("set_theme", "dark")
        self.title("MongoDB Users")

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Lazy evaluation of scene
        self.panelManager = None

        self.panelConnection = ConnectionInterface(self.container, self)
        self.panelConnection.grid(row=0, column=0, sticky="nsew")
        self.panelConnection.tkraise()

    def showScene(self, typeScene: TypeScene) -> None:
        """
        Used for change the current scene of manager,
        the connection in this point to MongoDB must
        be set.

        :param typeScene: The type of scene to show.
        """
        if typeScene == TypeScene.PANEL_CONNECTION:
            self.panelConnection.grid(row=0, column=0, sticky="nsew")
            self.panelConnection.tkraise()
        elif typeScene == TypeScene.PANEL_MANAGER:
            if self.panelManager is None:
                self.panelManager = PanelUser(self.container, self)
            self.panelManager.grid(row=0, column=0, sticky="nsew")
            self.panelManager.tkraise()
