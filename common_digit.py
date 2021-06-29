# Take two lists, eg:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# write a function that returns a list that contains
# only the elements that are common between the lists (without duplicates).
# Make sure program works on two lists of different sizes also.

def common_num(a,b):
    lst = []
    for num in a:
        if num in b:
            lst.append(num)
    print(lst)



common_num([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
