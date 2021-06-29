# Write a function that accepts following dict argument:
# fresh_produce = {
#         "apple": "red",
#   "grapes": "black",
#   "avocado": "green",
#   "pineapple": "golden",
#   "peach": "coral"
# }
# Check if fresh_produce has mango as key

def fresh_produce(argument):
    if 'mango' in argument.keys():
        print('Mango is Present')
    else:
            print('Mango is not present')



fresh_produce({"apple": "red", "grapes": "black", "avocado": "green","pineapple": "golden","peach": "coral"} )
