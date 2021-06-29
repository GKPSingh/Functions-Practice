# Write a function that uses for loop to print all even number from 0 to 100.
def even_num(limit):
    for num in range(0,limit+1):
        if num % 2 ==0:
            print(num)
        else:
            pass


even_num(100)