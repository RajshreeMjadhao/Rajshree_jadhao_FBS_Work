# Write a program to check if given number is Armstrong number or not.

n = int(input("Enter number:"))
temp = n
sum = 0
digit = len(str(n))

while(n>0):
    d = n % 10
    sum = sum +(d ** digit)
    n = n // 10

if(sum==temp):
    print("Armstrong number")
else:
    print("Not an Armstrong number")