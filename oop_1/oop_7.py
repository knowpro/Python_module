class Time:
    
    def __init__(self, hrs, mins):
        self.hrs = hrs
        self.mins = mins
        
    def getHrs(self):
        return self.hrs
    
    def getMins(self):
        return self.mins
        
    def addTime (self, t1, t2 ):
        mins_11 = t1.getHrs()
        mins_12 = t1.getMins()
        mins_13 = mins_11*60 + mins_12
        
        mins_21 = t2.getHrs()
        mins_22 = t2.getMins()
        mins_24 = mins_21*60 + mins_22
        
        print( "Hours: ",(mins_13 + mins_24)//60 ,
              "Mins: "(mins_13 + mins_24)%60)
        
    def displayMin( t0 ):
        return t0.getHrs()*60 + t0.getMins()

t10 = Time (4, 5)
t20 = Time (1, 35)

t10.addTime(t10,t20)

t15 = Time(3, 10)

print(t15.displayMin())
       