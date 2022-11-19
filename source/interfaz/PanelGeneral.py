import tkinter as tk


class PanelGeneral(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.connectionStringScheme = tk.Label(self, text="Connection String Scheme")
        self.connectionStringScheme.grid()

        self.buttonConnectionMongo = tk.Button(self, text="mongodb")
        self.buttonConnectionMongo.grid()

        self.buttonConnectionSRV = tk.Button(self, text="mongodb+svr")
        self.buttonConnectionSRV.grid()

        self.labelHostname = tk.Label(self, text="Host")
        self.labelHostname.grid()

        self.inputHostname = tk.Entry(self)
        self.inputHostname.grid()