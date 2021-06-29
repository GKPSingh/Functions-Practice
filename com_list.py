# Write a function that takes a list and returns a new list
# that contains all the elements of the first list minus all the duplicates.
def com_elements(a):
    lst = []
    for num in set(a):
        lst.append(num)
    print(lst)


com_elements([1,2,1,2,3,5,6,4,6,7,44,44, 373, 23])