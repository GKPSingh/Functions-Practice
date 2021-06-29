# Write a function called showNumbers that takes a parameter called limit.
# It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
# For example, if the limit is 3, it should print:
# 0 Even
# 1 Odd
# 2 Even
# 3 Odd
def shownum(limit):
    for num in range(0, limit+1):
        if num % 2 == 0:
            print(f'{num} Even')
        else:
            print(f'{num} Odd')


shownum(10)