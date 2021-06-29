# Write a function that takes three number arguments and return the smallest number.

def small3num(num1, num2, num3):
    if num1 < num2 and num1< num3:
        print(num1)
    elif num2 < num1  and num2 < num3:
        print(num2)
    else:
        print(num3)



small3num(2,-0.00001,0)
