# 6. Write a program to print Fibonacci series using recursion.

def fibonacci(n):
    if(n <= 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter how many terms:"))

for i in range(n):
    print(fibonacci(i), end=' ')