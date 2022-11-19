import tkinter as tk

from source.interfaz.ConnectionInterface import ConnectionInterface


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
        self.interfazTriangulo.grid(row=0, sticky=tk.E+tk.W)
        
        self.grid(sticky=tk.N+tk.E+tk.S+tk.W)

        
app = Application()
app.master.title('N1-Triangulo-Python-Tkinter')
app.mainloop()

