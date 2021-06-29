# "Write a function that takes an english alphabet as an argument. If alphabet is uppercase then return uppercase otherwise return lowercase

def check_arg(argument):
    if argument.isupper():
        print('uppercase')
    elif argument.islower():
        print('lowercase')
    else:
        pass




check_arg('GURU')
