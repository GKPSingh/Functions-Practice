# Write a function that uses for loop to print sum of all numbers from 1 to 100
def sum_100(limit):
    sum = 0
    for num in range(1,limit+1):
        sum = sum + num
    print(sum)



sum_100(100)
