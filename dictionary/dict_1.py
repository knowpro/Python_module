lnum = int(input("Enter the length of dictionary: "))
dic = {}

for pair in range(0, lnum):
    key = input('enter key: ')
    val = input('enter value: ')
    dic[key] = val

print(dic)
print(type(dic))