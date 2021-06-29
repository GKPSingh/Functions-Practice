# Write a function that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.

def first_last(number):
    lst = []
    number.sort()
    lst.append(number[0])
    lst.append(number[-1])
    print(lst)



first_last([5,10,15,20,25])