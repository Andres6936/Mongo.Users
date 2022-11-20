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

        self.buttonDescription = tk.Label(self, text="Standard Connection String Format. "
                                                     "The standard format of the MongoDB "
                                                     "connection URI is used to connect "
                                                     "to a MongoDB deployment: standalone,"
                                                     " replica set, or a sharded cluster.", wraplength="400px")
        self.buttonDescription.grid()

        self.labelHostname = tk.Label(self, text="Host")
        self.labelHostname.grid()

        self.inputHostname = tk.Entry(self)
        self.inputHostname.grid()

        self.checkDirectConnection = tk.Checkbutton(self, text="Direct Connection")
        self.checkDirectConnection.grid()

        self.labelDescriptionDirectConnection = tk.Label(self,
                                                         text="Specifies whether to force dispatch all operations to the specified host.")
        self.labelDescriptionDirectConnection.grid()
