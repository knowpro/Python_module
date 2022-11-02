
def varfunct (s_name, *marks):
    print(s_name)
    
    #return s_name, *marks
    
    for mark in marks:
        print(mark, end=" ")
    
temp = varfunct ("Alexa", 59, 54, 23, 58,)

print(temp) 
