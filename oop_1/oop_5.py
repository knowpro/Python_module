class Temperature:
    
    def __init__(self):
        print("Hello Tempo")    
    
    def convertFahrenheit(self, c_temp):
        return c_temp*(9/5) + 32
    
    def convertCelsius(self, f_temp):
        return (f_temp - 32)*5/9
    
t1 = Temperature()
a = t1.convertCelsius(27)
b = t1.convertFahrenheit(27)

print("in Degree: ", a, "in fahrenheit", b)