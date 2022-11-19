import tkinter as tk

class PanelAdvanced(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.labelReadPreference = tk.Label(self, text="Read Preference")
        self.labelReadPreference.grid()

        self.buttonDefault = tk.Button(self, text="Default")
        self.buttonDefault.grid()

        self.buttonPrimary = tk.Button(self, text="Primary")
        self.buttonPrimary.grid()

        self.buttonPrimaryPreferred = tk.Button(self, text="Primary Preferred")
        self.buttonPrimaryPreferred.grid()

        self.buttonSecondary = tk.Button(self, text="Secondary")
        self.buttonSecondary.grid()

        self.buttonSecondaryPreferred = tk.Button(self, text="Secondary Preferred")
        self.buttonSecondaryPreferred.grid()

        self.buttonNearest = tk.Button(self, text="Nearest")
        self.buttonNearest.grid()