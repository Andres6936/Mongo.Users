class Color(object):
    
    def __init__(self, elRojo, elVerde, elAzul):
        
        self.rojo = elRojo
        self.verde = elVerde
        self.azul = elAzul
        
    def getRojo(self):
        
        return self.rojo
    
    def getVerde(self):
        
        return self.verde
        
    def getAzul(self):
        
        return self.azul
        
    def setRojo(self, elRojo):
        
        self.rojo = elRojo
        
    def setVerde(self, elVerde):
        
        self.verde = elVerde
        
    def setAzul(self, elAzul):
        
        self.azul = elAzul
