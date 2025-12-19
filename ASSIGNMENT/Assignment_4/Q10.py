# WAP to check if given number is Perfect Number.
n = int(input("Enter number to check for  perfect:"))
sum = 0
for i in range(1, n):
    if(n % i == 0):
        sum = sum + i
if(sum ==n):
    print(f'{n} is a perfect number.')
else:
    print(f'{n} is not a perfect number.')