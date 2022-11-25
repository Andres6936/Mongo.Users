import tkinter as tk
from tkinter import ttk

class PanelInUseEncryption(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.labelInfo = ttk.Label(self, text="In-Use Encryption is an Enterprise/Atlas-only feature of MongoDB.")
        self.labelInfo.grid(sticky=tk.W)

        self.labelKeyVault = ttk.Label(self, text="Key Vault Namespace")
        self.labelKeyVault.grid(sticky=tk.W)

        self.labelDescriptionKeyVault = ttk.Label(self,
                                                  text="Specify a collection in which data encryption keys are stored in the format <db>.<collection>.")
        self.labelDescriptionKeyVault.grid(sticky=tk.W)

        self.entryKeyVault = ttk.Entry(self)
        self.entryKeyVault.grid(sticky=tk.W + tk.E)

        self.labelKMS = ttk.Label(self, text="KMS Providers")
        self.labelKMS.grid(sticky=tk.W)

        self.labelDescriptionKMS = ttk.Label(self, text="Specify one or more Key Management Systems to use.",
                                             font=("-size", 10), foreground="#979797")
        self.labelDescriptionKMS.grid(sticky=tk.W)

        self.checkStoreKMS = ttk.Checkbutton(self, text="Store KMS provider secrets")
        self.checkStoreKMS.grid(sticky=tk.W)

        self.labelCheckStoreKMS = ttk.Label(self, font=("-size", 10), foreground="#979797",
                                            text="Control whether KMS secrets are stored on disk (protected by the OS keychain) or discarded after disconnecting.")
        self.labelCheckStoreKMS.grid(sticky=tk.W)
