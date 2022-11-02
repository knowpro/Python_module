lnum = int(input("Enter the no: "))
dic={ (no + .6):(no*3 - 7.04) for no in range(0,lnum) }
print(dic)

m = float(input("Enter key to remove"))
a = dic.pop(m)

print(a)
print(dic)



