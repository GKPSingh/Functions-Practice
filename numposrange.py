# Python program to print all positive numbers in a range
def posnum(a,b):
    lst = []
    for num in range(a,b):
        if num > 0:
            lst.append(num)
    print(lst)




posnum(-3,10)
