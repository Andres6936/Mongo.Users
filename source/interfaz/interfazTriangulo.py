import tkinter as tk


from source.interfaz.panelTriangulo import PanelTriangulo
from source.interfaz.panelOpciones import PanelOpciones
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
            
        
        # Construye los paneles.
        self.panelImagen = PanelImagen(self)
        self.panelImagen.grid(row=0, sticky=tk.E+tk.W)
        
        self.panelBotones = PanelBotones(self)
        self.panelBotones.grid(row=1, sticky=tk.E+tk.W)
        
        self.panelTriangulo = PanelTriangulo(self)
        self.panelTriangulo.grid(row=1, rowspan=2, column=1,
            sticky=tk.E+tk.W)
        
        self.panelInfo = PanelInfo(self)
        self.panelInfo.grid(row=2, sticky=tk.E+tk.W)
        
        self.panelOpciones = PanelOpciones(self)
        self.panelOpciones.grid(row=3, column=0, columnspan=2,
            sticky=tk.E+tk.W)
            
        # Enviamos el triangulo para dibujar
        self.panelTriangulo.setTriangulo(self.triangulo)
        
        self.panelTriangulo.paintComponent()

    
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
 
