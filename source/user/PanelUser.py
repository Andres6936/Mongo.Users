import tkinter as tk

from source.user.User import User


class PanelUser(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.user = User(self)
        self.user.grid()
