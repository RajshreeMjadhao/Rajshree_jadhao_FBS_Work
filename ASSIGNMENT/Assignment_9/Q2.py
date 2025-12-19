#2. Write a program to check if given number is Armstrong or not using recursive function.

def power_sum(num, power):
    if num == 0:
        return 0
    digit = num % 10
    return (digit ** power) + power_sum(num // 10, power)

num = int(input("Enter number: "))
digits = len(str(num))

if power_sum(num, digits) == num:
    print("Armstrong Number")
else:
    print("Not Armstrong")