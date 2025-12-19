# 10.Write a program to check if entered year is a leap year or not.
def leapYear(num):
    if (num % 4 == 0):
        return f'{num} is a leap year.'
    else:
        return f'{num} is not a leap year.'
    
num = int(input("Enter year:"))
print(leapYear(num))