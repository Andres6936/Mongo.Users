import tkinter as tk
from ctypes import windll

from source.interfaz.ConnectionInterface import ConnectionInterface

# Avoid the blurry font in Windows 10 - Reference: https://stackoverflow.com/a/43046744
windll.shcore.SetProcessDpiAwareness(1)

if __name__ == '__main__':
    root = tk.Tk()
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "light")
    root.title("N1-Triangulo-Python-Tkinter")

    app = ConnectionInterface(root)
    app.pack(fill="both", expand=True)

    root.mainloop()
