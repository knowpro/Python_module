lnum=int(input("Enter the no: "))
dic1=[]
dic2=[]

for mapro in range(0,lnum):
    value = input("Enter the values: ")
    dic1.append(value)
print(dic1)

for mapro in range(0,lnum):
    value = input("Enter the values: ")
    dic2.append(value)
print(dic2)
    
dic = dict(zip(dic1,dic2))
print(dic)