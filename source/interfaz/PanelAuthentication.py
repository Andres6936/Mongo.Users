import tkinter as tk

class PanelAuthentication(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.usernameLabel = tk.Label(self, text="Username")
        self.usernameLabel.grid(row=1, column=0, sticky=tk.E + tk.W)

        self.username = tk.StringVar()
        self.usernameInput = tk.Entry(self, textvariable=self.username)
        self.usernameInput.grid(row=1, column=1, sticky=tk.E + tk.W)

        self.passwordLabel = tk.Label(self, text="Password")
        self.passwordLabel.grid(row=1, column=2, sticky=tk.E + tk.W)

        self.password = tk.StringVar()
        self.passwordInput = tk.Entry(self, textvariable=self.password)
        self.passwordInput.grid(row=1, column=3, sticky=tk.E + tk.W)

        self.buttonConnect = tk.Button(self, text='Connect', command=self.connect)
        self.buttonConnect.grid(row=2, column=0, columnspan=2, sticky=tk.E + tk.W)

        self.buttonCancel = tk.Button(self, text='Cancel')
        self.buttonCancel.grid(row=2, column=2, columnspan=2, sticky=tk.E + tk.W)

    def connect(self):
        print("Connect")