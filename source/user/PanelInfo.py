import tkinter as tk


class PanelInfo(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.grid(padx=4, pady=4)

        self.labelNewConnection = tk.Label(self, text="User Manager", font=("-size", 15))
        self.labelNewConnection.grid(row=0, column=0, columnspan=2, sticky=tk.W)

        self.labelDescription = tk.Label(self, text="Create, update and remove roles and users", font=("-size", 10),
                                         foreground="#979797")
        self.labelDescription.grid(row=1, column=0, columnspan=2, sticky=tk.W)
