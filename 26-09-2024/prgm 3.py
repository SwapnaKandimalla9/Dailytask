#checks if a number is prime, a prime number is a number greater than 1 that is only divisible by 1 and itself
def is-prime(n):
if n <= 1:
    return False
for i in range(2,int(n**0.5)+ 1):
    if n % i == 0:
        return False
    return True
number= int(input("enter a number:"))
if is-prime(number):
    print("number is a prime number: ")
else:
    print("number is not a prime number.")