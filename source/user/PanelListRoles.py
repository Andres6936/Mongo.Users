import tkinter as tk
from tkinter import ttk

from source.user.User import User


class PanelListRoles(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollableFrame = ttk.Frame(canvas)
        self.scrollableFrame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollableFrame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar.pack(side="right", fill="y")

        for i in range(0, 25):
            self.user = User(self.scrollableFrame)
            self.user.pack()
