# Write a function that asks to enter user name and age. Print out a message addressed to user that tells them the year that they will turn 100 years old.
#
# e.g. output:  Gurkipal, you will turn 100 years in 2086.
# Hint: use input to take user name and age

x = input('Enter your name:')
y = input('Enter your age:')
YOB = 1986
print(f'{x}, you will turn 100 years in {YOB+100}')