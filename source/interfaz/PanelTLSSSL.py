import tkinter as tk

class PanelTLSSSL(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.sslTLSConnection = tk.Label(self, text="SSL/TLS Connection")
        self.sslTLSConnection.grid()

        self.buttonDefault = tk.Button(self, text="Default")
        self.buttonDefault.grid()

        self.buttonOn = tk.Button(self, text="On")
        self.buttonOn.grid()

        self.buttonOff = tk.Button(self, text="Off")
        self.buttonOff.grid()

        self.fileCertificatePEM = tk.Button(self, text="Select a file...")
        self.fileCertificatePEM.grid()

        self.fileClientCertificatePEM = tk.Button(self, text="Select a file...")
        self.fileClientCertificatePEM.grid()