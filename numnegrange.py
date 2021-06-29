# Python program to print all negative numbers in a range
def negnum(a,b):
    lst = []
    for num in range(a,b):
        if num < 0:
            lst.append(num)
    print(lst)


negnum(-3,3)
