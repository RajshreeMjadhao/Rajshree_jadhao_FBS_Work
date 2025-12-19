# 5. WAP to print Fibonacci series upto n.
num = int(input("Enter Fibonacci number:"))
a = 0
b = 1
for i in range(num):
    print(a)
    a, b=b, a+b