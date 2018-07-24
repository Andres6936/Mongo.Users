import tkinter as tk

from source.interfaz.interfazTriangulo import InterfazTriangulo

class Application(tk.Frame):
    
    def __init__(self, master=None):
        
        tk.Frame.__init__(self, master)
        
        self.config(background='white')
        
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        self.interfazTriangulo = InterfazTriangulo(self)
        self.interfazTriangulo.grid(row=0, sticky=tk.E+tk.W)
        
        self.grid(sticky=tk.N+tk.E+tk.S+tk.W)

        
app = Application()
app.master.title('N1-Triangulo-Python-Tkinter')
app.mainloop()

