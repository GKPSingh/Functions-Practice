# "Write a function that accepts following dict argument:
# fresh_produce = {
#         ""apple"": ""red"",
#   ""grapes"": ""black"",
#   ""avocado"": ""green"",
#   ""pineapple"": ""golden"",
#   ""peach"": ""coral""
# }
# Check if fresh_produce has golden as value"

def fresh_produce(argument):
    if 'golden' in argument.values():
        print('Golden is present')
    else:
        print('Golden Is not present')



fresh_produce({"apple": "red", "grapes": "black", "avocado": "green", "pineapple": "golden", "peach": "coral"} )