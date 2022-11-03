
class Rectangle:
    
    def __init__(self):
        print("This is Rectangle")

    def setWide(self, wide):
        self.wide = wide
        
    def setLong(self, long):
        self.long = long
        
    def areaRect(self):
        return self.wide*self.long
    
r1 = Rectangle()

r1.setWide(10.5)
r1.setLong(15.10)

print(r1.areaRect())