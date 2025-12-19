# WAP to check if given number Strong Number.
n = int(input("enter number:"))
num = n
sum = 0

while (n > 0):
    d = n % 10
    fact = 1
    for i in range(1, d+1):
        fact = fact * i
    sum = sum + fact
    n = n // 10

if(sum == num):
    print("Strong number")
else:
    print("Is not a strong number")