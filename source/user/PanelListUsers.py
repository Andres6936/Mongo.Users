import tkinter as tk

from source.user.User import User


class PanelListUsers(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        for i in range(0, 5):
            self.user = User(self)
            self.user.grid(row=i, column=0)
