import tkinter as tk
from tkinter import ttk

class PanelTLSSSL(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.grid_columnconfigure((0, 1, 2), uniform="uniform", weight=1)

        self.sslTLSConnection = tk.Label(self, text="SSL/TLS Connection")
        self.sslTLSConnection.grid(row=0, column=0, sticky=tk.W)

        self.buttonDefault = ttk.Button(self, text="Default")
        self.buttonDefault.grid(row=1, column=0)

        self.buttonOn = ttk.Button(self, text="On")
        self.buttonOn.grid(row=1, column=1)

        self.buttonOff = ttk.Button(self, text="Off")
        self.buttonOff.grid(row=1, column=2)

        self.labelCertificateAuthority = ttk.Label(self, text="Certificate Authority (.pem)")
        self.labelCertificateAuthority.grid(row=2, column=0, sticky=tk.W)

        self.fileCertificatePEM = ttk.Button(self, text="Select a file...")
        self.fileCertificatePEM.grid(row=2, column=1, columnspan=2, sticky=tk.W + tk.E)

        self.labelClientCertificate = ttk.Label(self, text="Client Certificate and Key (.pem)")
        self.labelClientCertificate.grid(row=3, column=0, sticky=tk.W)

        self.fileClientCertificatePEM = ttk.Button(self, text="Select a file...")
        self.fileClientCertificatePEM.grid(row=3, column=1, columnspan=2, sticky=tk.W + tk.E)

        self.labelClientKey = ttk.Label(self, text="Client Key Password")
        self.labelClientKey.grid(row=4, column=0, sticky=tk.W)

        self.inputClientPassword = ttk.Entry(self)
        self.inputClientPassword.grid(row=5, column=0, columnspan=3, sticky=tk.W + tk.E)

        self.checkInsecure = ttk.Checkbutton(self, text="tlsInsecure")
        self.checkInsecure.grid(row=6, sticky=tk.W)

        self.checkAllowInvalidHostnames = ttk.Checkbutton(self, text="tlsAllowInvalidHostnames")
        self.checkAllowInvalidHostnames.grid(row=7, sticky=tk.W)

        self.checkAllowInvalidCertificates = ttk.Checkbutton(self, text="tlsAllowInvalidCertificates")
        self.checkAllowInvalidCertificates.grid(row=8, sticky=tk.W)
