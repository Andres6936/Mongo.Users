import tkinter as tk

class PanelInfo(tk.LabelFrame):
    
    def __init__(self, parent):
        
        tk.LabelFrame.__init__(self, parent, text='Información')
        
        self.config(background='white')
        
        self.etiquetaPerimetro = tk.Label(self, text='Perímetro')
        self.etiquetaPerimetro.grid(row=0, sticky=tk.N+tk.S+tk.E+tk.W)
        
        self.etiquetaArea = tk.Label(self, text='Área')
        self.etiquetaArea.grid(row=1, sticky=tk.N+tk.S+tk.E+tk.W)
        
        self.etiquetaAltura = tk.Label(self, text='Altura')
        self.etiquetaAltura.grid(row=2, sticky=tk.N+tk.S+tk.E+tk.W)
