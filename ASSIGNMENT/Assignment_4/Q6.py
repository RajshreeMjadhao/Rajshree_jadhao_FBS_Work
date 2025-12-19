# WAP to check if a given number is prime number or not.
n = int(input("Enter number to check for prime:"))
for i in range (2,n):
    if(n % 1 == 0):
        print(f'{n} is not a prime number.')

        break
else:
    print(f'{n} is a prime number.')