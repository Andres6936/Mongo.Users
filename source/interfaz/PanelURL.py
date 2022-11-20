import tkinter as tk


class PanelURL(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.config(padx=4, pady=4)

        self.labelURI = tk.Label(self, text='URI')
        self.labelURI.grid(row=0, column=0, sticky=tk.E + tk.W)

        self.editConnectionString = tk.Radiobutton(self, text='Altura')
        self.editConnectionString.grid(row=0, column=1, sticky=tk.E + tk.W)

        self.entryURI = tk.Entry(self)
        self.entryURI.grid(row=1, sticky=tk.E + tk.W)
