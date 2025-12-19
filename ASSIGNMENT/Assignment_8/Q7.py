#7. Write a program to find sum of digits of a number.

def sumOfDigit(num):
    if(num <= 0):
        return 0
    else:
        return (num % 10) + (sumOfDigit(num // 10))
    
num = int(input("Enter number:"))
print(sumOfDigit(num))