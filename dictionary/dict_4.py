lnum = int(input("Enter the num: "))

dic = { no:no*no for no in range(1,lnum) }
print(dic)
res = 1

for no in dic.values():
    res = res*no
    
print(res)