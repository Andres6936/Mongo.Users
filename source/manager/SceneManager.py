import tkinter as tk

from source.connection.ConnectionInterface import ConnectionInterface


class SceneManager(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.call("source", "azure.tcl")
        self.call("set_theme", "light")
        self.title("MongoDB Users")

        self.currentScene = ConnectionInterface(self)
        self.currentScene.pack(fill="both", expand=True)
