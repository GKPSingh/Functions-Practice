# "Write a function that takes in an argument.
# If argument is integer type, function should return Integer  type argument
# If argument is a float type, function should return Float type argument
# If argument is a string type, function should return String type argument
# For all other inputs function should return Unknot type argument"
def num_type(argument):
    if type(argument) == int:
        print('Integer type Argument')
    elif type(argument) == float:
        print('Float type Argument')
    elif type(argument) == str:
        print('String type Argument')
    else:
        print('Unknown type Argument')





num_type(3.0)

