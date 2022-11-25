import tkinter as tk
from tkinter import ttk

class PanelAuthentication(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

        self.labelAuthenticationMethod = tk.Label(self, text="Authentication Method")
        self.labelAuthenticationMethod.grid(row=0, column=0, columnspan=2, sticky=tk.W)

        self.buttonNone = ttk.Button(self, text='None', command=self.connect)
        self.buttonNone.grid(row=1, column=0)

        self.buttonUsernamePassword = ttk.Button(self, text='Username/Password')
        self.buttonUsernamePassword.grid(row=1, column=1)

        self.buttonX509 = ttk.Button(self, text="X.509")
        self.buttonX509.grid(row=1, column=2)

        self.buttonKerberos = ttk.Button(self, text="Kerberos")
        self.buttonKerberos.grid(row=1, column=3)

        self.buttonLDAP = ttk.Button(self, text="LDAP")
        self.buttonLDAP.grid(row=1, column=4)

        self.buttonAWSIAM = ttk.Button(self, text="AWS IAM")
        self.buttonAWSIAM.grid(row=1, column=5)

    def connect(self):
        print("Connect")
