# "Write a function that accepts following dict argument:
# fresh_produce = {
#         ""apple"": ""red"",
#   ""grapes"": ""black"",
#   ""avocado"": ""green"",
#   ""pineapple"": ""golden"",
#   ""peach"": ""coral""
# }
# Print all value of fresh_produce"

def fresh_produce(argument):
    for key, value in argument.items():
        print(value)


fresh_produce({
        "apple": "red",
  "grapes": "black",
  "avocado": "green",
  "pineapple": "golden",
  "peach": "coral"
} )