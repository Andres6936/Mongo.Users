from math import sqrt

class Triangulo(object):
    
    def __init__(self, elPunto1, elPunto2, elPunto3, relleno, lineas):
        
        self.punto1 = elPunto1
        self.punto2 = elPunto2
        self.punto3 = elPunto3
        
        self.colorRelleno = relleno
        self.colorLineas = lineas
        
    def getPunto1(self):
        
        return self.punto1
        
    def getPunto2(self):
        
        return self.punto2
    
    def getPunto3(self):
        
        return self.punto3
    
    def getColorRelleno(self):
        
        return self.colorRelleno
    
    def getColorLineas(self):
        
        return self.colorLineas
    
    def getPerimetro(self):

        return self.getLado1() + self.getLado2() + self.getLado3()
        
    def getArea(self):
        
        perimetro = self.getPerimetro()
        s = perimetro / 2
        
        valorLado1 = s - self.getLado1()
        valorLado2 = s - self.getLado2()
        valorLado3 = s - self.getLado3()
        
        area = sqrt(s * valorLado1 * valorLado2 * valorLado3)
        
        return area
        
    def getAltura(self):
        
        area = self.getArea()
        base = selg.getLado1()
        altura = (area / base) * 2
        
        return altura
        
    def getLado1(self):
        
        valorX = pow(self.punto1.getX() - self.punto2.getX(), 2)
        valorY = pow(self.punto1.getY() - self.punto2.getY(), 2)
        
        distancia = sqrt(valorX + valorY)
        
        return distancia
        
    def getLado2(self):
        
        valorX = pow(self.punto2.getX() - self.punto3.getX(), 2)
        valorY = pow(self.punto2.getY() - self.punto3.getY(), 2)
        
        distancia = sqrt(valorX + valorY)
        
        return distancia
        
    def getLado3(self):
        
        valorX = pow(self.punto3.getX() - self.punto1.getX(), 2)
        valorY = pow(self.punto3.getY() - self.punto1.getY(), 2)
        
        distancia = sqrt(valorX + valorY)
        
        return distancia
        
    def metodo1(self):
        
        return "Respuesta 1"
        
    def metodo2(self):
        
        return "Respuesta 2"
     
