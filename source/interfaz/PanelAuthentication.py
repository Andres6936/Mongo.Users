import tkinter as tk

class PanelAuthentication(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

        self.labelAuthenticationMethod = tk.Label(self, text="Authentication Method")
        self.labelAuthenticationMethod.grid(row=0)

        self.buttonNone = tk.Button(self, text='None', command=self.connect)
        self.buttonNone.grid(row=1, column=0, sticky=tk.E + tk.W)

        self.buttonUsernamePassword = tk.Button(self, text='Username/Password')
        self.buttonUsernamePassword.grid(row=1, column=1, sticky=tk.E + tk.W)

        self.buttonX509 = tk.Button(self, text="X.509")
        self.buttonX509.grid(row=1, column=2, sticky=tk.E + tk.W)

        self.buttonKerberos = tk.Button(self, text="Kerberos")
        self.buttonKerberos.grid(row=1, column=3, sticky=tk.E + tk.W)

        self.buttonLDAP = tk.Button(self, text="LDAP")
        self.buttonLDAP.grid(row=1, column=4, sticky=tk.E + tk.W)

        self.buttonAWSIAM = tk.Button(self, text="AWS IAM")
        self.buttonAWSIAM.grid(row=1, column=5, sticky=tk.E + tk.W)

    def connect(self):
        print("Connect")
