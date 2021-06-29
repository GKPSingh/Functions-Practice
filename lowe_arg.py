# "Write a function that takes an english alphabet as an argument. If alphabet is lowercase then return lowercase. Example:
# if argument is ‘a return lowercase
# if argument is ‘r’ return lowercase
# if argument is ‘A’ do nothing
#
# Hint: use if statement"

def lower_fun(argument):
    if argument.islower():
        print('lowercase')
    else:
        pass



lower_fun('D')