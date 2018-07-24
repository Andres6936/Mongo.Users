import tkinter as tk

class PanelOpciones(tk.LabelFrame):
    
    def __init__(self, parent):
        
        tk.LabelFrame.__init__(self, parent, text='Opciones')
        
        self.config(background='white')
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        
        self.botonOpcion1 = tk.Button(self, text='Opcion 1')
        self.botonOpcion1.grid(row=0, column=0, sticky=tk.E+tk.W)
        
        self.botonOpcion2 = tk.Button(self, text='Opcion 2')
        self.botonOpcion2.grid(row=0, column=1, sticky=tk.E+tk.W)
