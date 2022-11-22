import tkinter as tk
from tkinter import ttk

class PanelTLSSSL(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.sslTLSConnection = tk.Label(self, text="SSL/TLS Connection")
        self.sslTLSConnection.grid()

        self.buttonDefault = ttk.Button(self, text="Default")
        self.buttonDefault.grid()

        self.buttonOn = ttk.Button(self, text="On")
        self.buttonOn.grid()

        self.buttonOff = ttk.Button(self, text="Off")
        self.buttonOff.grid()

        self.labelCertificateAuthority = ttk.Label(self, text="Certificate Authority (.pem)")
        self.labelCertificateAuthority.grid()

        self.fileCertificatePEM = ttk.Button(self, text="Select a file...")
        self.fileCertificatePEM.grid()

        self.labelClientCertificate = ttk.Label(self, text="Client Certificate and Key (.pem)")
        self.labelClientCertificate.grid()

        self.fileClientCertificatePEM = ttk.Button(self, text="Select a file...")
        self.fileClientCertificatePEM.grid()

        self.labelClientKey = ttk.Label(self, text="Client Key Password")
        self.labelClientKey.grid()

        self.inputClientPassword = ttk.Entry(self)
        self.inputClientPassword.grid()
