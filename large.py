# Python Program to Find the Largest Among Three Numbers

def large(a,b,c):
    if a > b and a > c:
        print(f'{a} is greatest')
    elif b > a and b > c:
        print(f'{b} is greatest')
    else:
        print(f'{c} is greatest')


large(14,-23,2)
