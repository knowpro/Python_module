
def squareList(num):
    lst = [ no for no in range(4,num+1) if no%2 == 0]
    return lst

print(squareList(30))