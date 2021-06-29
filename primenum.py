# Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.
def prime_number(limit):
    prime_list=[]
    for num in range(2,limit+1):
        for num2 in range(2,num):
            if num%num2==0:
                break
            else:
                prime_list.append(num)
                print(prime_list)



prime_number(5)