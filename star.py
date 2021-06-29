# Write a function called show_stars(rows). If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****

def show_stars(rows):
    for num in range(1,rows+1):
        print('*'  * num)



show_stars(10)