import tkinter as tk

from source.connection.ConnectionInterface import ConnectionInterface
from source.user.PanelUser import PanelUser


class SceneManager(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.call("source", "azure.tcl")
        self.call("set_theme", "light")
        self.title("MongoDB Users")

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.currentScene = ConnectionInterface(self.container, self)
        self.currentScene.grid(row=0, column=0, sticky="nsew")
        self.currentScene.tkraise()

    def next(self):
        frame = PanelUser(self.container)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
