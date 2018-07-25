import tkinter as tk

class PanelBotones(tk.LabelFrame):
    
    def __init__(self, parent):
        
        tk.LabelFrame.__init__(self, parent, text='Modificaciones')
        
        self.config(background='white', padx=4, pady=4)
        
        self.columnconfigure(0, weight=1)
        
        self.botonPuntos = tk.Button(self, text='Cambiar Puntos')
        self.botonPuntos.grid(row=0, sticky=tk.E+tk.W)
        
        self.botonColorLinea = tk.Button(self, text='Cambiar Lineas')
        self.botonColorLinea.grid(row=1, sticky=tk.E+tk.W)
        
        self.botonColorFondo = tk.Button(self, text='Cambiar Fondo')
        self.botonColorFondo.grid(row=2, sticky=tk.E+tk.W)
