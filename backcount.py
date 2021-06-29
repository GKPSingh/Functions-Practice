# Write a function that accepts an int argument greater than 10. Function should print numbers counting backward from the argument until 0.
# E.g. if argument entered is 12 then it should print
# 12
# 11
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0

def count_back(number):
    for num in range(11,-1,-1):
        print(num)


count_back(11)