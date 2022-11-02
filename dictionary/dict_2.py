lnum = int(input("Enter the length of dictionary: "))
dic1 = {}
dic2={}

for concat in range(0,lnum):
    key=input("Enter the key: ")
    value=input("Enter the value: ")
    dic1[key]=value
    
    
for concat in range(0,lnum):
    key=input("Enter the key: ")
    value=input("Enter the value: ")
    dic2[key]=value
    
dic_concat={**dic1,**dic2}
print(dic1)
print(dic2)
print(dic_concat)
    