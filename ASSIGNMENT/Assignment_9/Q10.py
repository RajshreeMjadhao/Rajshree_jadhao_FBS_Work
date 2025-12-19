# 10. Write a program to reverse a number using recursion.

def reverse_num(n):
    if(len(str(n)) == 1):
        return n
    return int(str(n % 10) + str(reverse_num(n // 10)))

num = int(input("Enter number: "))
print("Reverse =", reverse_num(num))