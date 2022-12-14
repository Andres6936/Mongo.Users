import tkinter as tk
from tkinter import ttk


class TabX509(tk.Frame):
    """
    MongoDB supports x.509 certificate authentication for client
    authentication and internal authentication of the members of
    replica sets and sharded clusters. x.509 certificate
    authentication requires a secure TLS/SSL connection.

    To use MongoDB with x.509, you must use valid certificates
    generated and signed by a certificate authority. The client
    x.509 certificates must meet the client certificate
    requirements.
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.labelMessage = ttk.Label(self,
                                      text="X.509 Authentication type requires a Client Certificate to work. Make sure to enable TLS and add\none in the TLS/SSL tab.")
        self.labelMessage.grid()
