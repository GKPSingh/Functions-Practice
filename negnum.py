# Python program to print negative numbers in a list
def numneg(a):
    lst = []
    for num in a:
        if num < 0:
            lst.append(num)
    print(lst)



numneg([33,93,383, -12, 22,-56])

