import tkinter as tk
from ctypes import windll

from source.interfaz.ConnectionInterface import ConnectionInterface

# Avoid the blurry font in Windows 10 - Reference: https://stackoverflow.com/a/43046744
windll.shcore.SetProcessDpiAwareness(1)


class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.config(background='white')
        
        # Obtenemos el ventana superior (Top-Level window)
        top = self.winfo_toplevel()
        top.resizable(width=False, height=False)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.interfazTriangulo = ConnectionInterface(self)
        self.interfazTriangulo.grid(row=0, sticky=tk.E + tk.W)

        self.grid(sticky=tk.N + tk.E + tk.S + tk.W)


if __name__ == '__main__':
    root = tk.Tk()
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "light")
    root.title("N1-Triangulo-Python-Tkinter")

    app = Application(root)
    app.pack(fill="both", expand=True)

    root.mainloop()
