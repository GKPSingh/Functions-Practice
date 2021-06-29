# "Write a function that accepts following dict argument:
# fresh_produce = {
#         ""apple"": ""red"",
#   ""grapes"": ""black"",
#   ""avocado"": ""green"",
#   ""pineapple"": ""golden"",
#   ""peach"": ""coral""
# }
# Print all keys of fresh_produce"

def fresh(argument):
    for key, value in argument.items():
        print(key)



fresh({"apple":"red", "grapes": "black", "avocado": "green", "pineapple": "golden", "peach": "coral"})
