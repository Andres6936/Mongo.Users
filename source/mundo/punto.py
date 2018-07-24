class Punto(object):
    
    def __init__(self, x_coord, y_coord):
        
        self.x = x_coord
        self.y = y_coord
        
    def getX(self):
       
        return self.x
       
    def getY(self):
        
        return self.y
        
    def setX(self, x_coord):
        
        self.x = x_coord
        
    def setY(self, y_coord):
        
        self.y = y_coord
