import tkinter as tk


from source.interfaz.panelTriangulo import PanelTriangulo
from source.interfaz.TabNewConnection import TabNewConnection
from source.interfaz.panelBotones import PanelBotones
from source.interfaz.panelImagen import PanelImagen
from source.interfaz.panelInfo import PanelInfo

from source.mundo.triangulo import Triangulo
from source.mundo.color import Color
from source.mundo.punto import Punto


class InterfazTriangulo(tk.Frame):
    
    def __init__(self, parent):
        
        tk.Frame.__init__(self, parent)
        
        self.config(background='white')
        
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        self.punto1 = Punto(120, 20)
        self.punto2 = Punto(220, 200)
        self.punto3 = Punto(20, 200)
        
        
        self.colorRelleno = "#0000AA"
        self.colorLineas = "#000000"
        
        self.triangulo = Triangulo(self.punto1, self.punto2,
            self.punto3, self.colorRelleno, self.colorLineas)
        
        self.panelOpciones = TabNewConnection(self)
        self.panelOpciones.grid(row=0, column=0, padx=4, pady=4, sticky=tk.E+tk.W)
        self.pack()

    
    def getTriangulo(self):
        
        return self.triangulo
        
    def setPuntos(self):
        pass
        
    def setColorFondo(self):
        pass
        
    def setColorLineas(self):
        pass
        
    def repintar(self):
        pass
        
    def Colineales(self):
        pass
        
    def reqFuncOpcion1(self):
        pass
        
    def reqFuncOpcion2(self):
        pass
 
