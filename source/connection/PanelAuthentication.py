import tkinter as tk
from tkinter import ttk

from source.connection.TabAWSIAM import TabAWSIAM
from source.connection.TabKerberos import TabKerberos
from source.connection.TabLDAP import TabLDAP
from source.connection.TabUsernamePassword import TabUsernamePassword
from source.connection.TabX509 import TabX509


class PanelAuthentication(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

        self.labelAuthenticationMethod = tk.Label(self, text="Authentication Method")
        self.labelAuthenticationMethod.grid(row=0, column=0, columnspan=2, sticky=tk.W)

        self.buttonNone = ttk.Button(self, text='None')
        self.buttonNone.grid(row=1, column=0)

        self.buttonUsernamePassword = ttk.Button(self, text='Username/Password', command=self.showUsernamePassword)
        self.buttonUsernamePassword.grid(row=1, column=1)

        self.buttonX509 = ttk.Button(self, text="X.509", command=self.showX509)
        self.buttonX509.grid(row=1, column=2)

        self.buttonKerberos = ttk.Button(self, text="Kerberos", command=self.showKerberos)
        self.buttonKerberos.grid(row=1, column=3)

        self.buttonLDAP = ttk.Button(self, text="LDAP", command=self.showLDAP)
        self.buttonLDAP.grid(row=1, column=4)

        self.buttonAWSIAM = ttk.Button(self, text="AWS IAM", command=self.showAWSIAM)
        self.buttonAWSIAM.grid(row=1, column=5)

        self.container = tk.Frame(self)
        self.container.grid(row=2, column=0, columnspan=6, sticky=tk.W + tk.E)

    def showUsernamePassword(self):
        self.tabUsernamePassword = TabUsernamePassword(self.container)
        self.tabUsernamePassword.grid(row=0, column=0, sticky="nsew")
        self.tabUsernamePassword.tkraise()

    def showX509(self):
        self.tabX509 = TabX509(self.container)
        self.tabX509.grid(row=0, column=0, sticky="nsew")
        self.tabX509.tkraise()

    def showKerberos(self):
        self.tabKerberos = TabKerberos(self.container)
        self.tabKerberos.grid(row=0, column=0, sticky="nsew")
        self.tabKerberos.tkraise()

    def showLDAP(self):
        self.tabLDAP = TabLDAP(self.container)
        self.tabLDAP.grid(row=0, column=0, sticky="nsew")
        self.tabLDAP.tkraise()

    def showAWSIAM(self):
        self.tabAWSIAM = TabAWSIAM(self.container)
        self.tabAWSIAM.grid(row=0, column=0, sticky="nsew")
        self.tabAWSIAM.tkraise()
