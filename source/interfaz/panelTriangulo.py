import tkinter as tk

class PanelTriangulo(tk.Canvas):
    
    def __init__(self, parent):
        
        tk.Canvas.__init__(self, parent)
        
        self.config(width=270, height=200, background='white')
        
        # Triangulo a dibujar
        self.triangulo = None
        
    def setTriangulo(self, elTriangulo):
        
        self.triangulo = elTriangulo
    
    def paintComponent(self):
        
        punto1X = int(self.triangulo.getPunto1().getX())
        punto1Y = int(self.triangulo.getPunto1().getY())
        
        punto2X = int(self.triangulo.getPunto2().getX())
        punto2Y = int(self.triangulo.getPunto2().getY())
        
        punto3X = int(self.triangulo.getPunto3().getX())
        punto3Y = int(self.triangulo.getPunto3().getY())
        
        colorRelleno = self.triangulo.getColorRelleno()
        colorLineas = self.triangulo.getColorLineas()
        
        self.create_polygon(punto1X, punto1Y, punto2X, punto2Y,
            punto3X, punto3Y, fill=colorRelleno, outline=colorLineas)
