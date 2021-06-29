# Python Program to Find the Sum of n Natural Numbers
def natsum(a):
    sum = 0
    for num in range(1,a+1):
        sum = sum + num
    print(sum)



natsum(5)