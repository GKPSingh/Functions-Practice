# "Write a function that accepts following dict argument:
# fresh_produce = {
#         ""apple"": ""red"",
#   ""grapes"": ""black"",
#   ""avocado"": ""green"",
#   ""pineapple"": ""golden"",
#   ""peach"": ""coral""
# }
# Check if fresh_produce has gala in it.
# Hint: Use logical operator"

def fresh_produce(argument):
    if 'gala' in argument.items():
        print('gala is present')
    else:
        print('gala is not present')


fresh_produce({"apple": "red", "grapes": "black", "avocado": "green", "pineapple": "golden","peach": "coral"} )