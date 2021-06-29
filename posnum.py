# Python program to print positive numbers in a list
def poslst(a):
    lst = []
    for num in a:
        if num > 0:
            lst.append(num)
    print(lst)


poslst([3,5,6,-4,-3,-9])