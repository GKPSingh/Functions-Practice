# Python program to find second largest number in a list
def larsec(a):
    a.sort()
    seclar = a[-2]
    print(seclar)



larsec([44,233,756,34])