# Python program to print even length words in a string
def leneven(a):
    a = a.split(' ')
    for word in a:
        if len(word) % 2 == 0:
            print(word)


leneven('My name is Gurkirpal Singh Parmar')
