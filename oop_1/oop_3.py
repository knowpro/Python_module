class StringAgain:
    
    def __init__(self):
        print("This is StringAgain")
    
    def setString(self, stg):
        self.stg = stg
    
    def getString(self):
        return self.stg
    
    def print_String(self):
        print(self.stg.upper())        

s = StringAgain()
s.setString("Dal kuch bhi")
s.print_String()