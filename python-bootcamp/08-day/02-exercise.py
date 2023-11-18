# Check for prime number 

input = int(input("Check your number: "))


def prime(number):
    prime_checker = True
    for i in range(2, number): 
        if number % i == 0:
            prime_checker = False 
    if prime_checker:
        print("this is prime number")
    else:
        print("not a prime number")


prime(number=input)
