lnum=int(input("Enter the no: "))
dic1={}
dic2={}

for mapro in range(0,lnum):
    key=input("Enter the key: ")
    value=input("Enter the values: ")
    dic1.update({key: value})

for mapro in range(0,lnum):
    key=input("Enter the key: ")
    value=input("Enter the values: ")
    dic2.update({key:value})
    
dic = dict(zip(dic1,dic2))