# 7. Write a program to find sum of digits using recursion.

def sumOfDigit(n):
    if(n == 0):
        return 0
    return (n % 10) + sumOfDigit(n // 10)

n = int(input("Enter number: "))
print("Sum of digits =", sumOfDigit(n))