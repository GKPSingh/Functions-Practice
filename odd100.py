# Write a function that uses for loop to print all odd number from 1 to 100.
def odd_num(limit):
    for num in range(1,limit+1):
        if num % 2 == 1:
            print(num)



odd_num(100)