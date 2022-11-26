import tkinter as tk
from tkinter import ttk


class TabX509(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.labelMessage = ttk.Label(self,
                                      text="X.509 Authentication type requires a Client Certificate to work. Make sure to enable TLS and add\none in the TLS/SSL tab.")
        self.labelMessage.grid()
