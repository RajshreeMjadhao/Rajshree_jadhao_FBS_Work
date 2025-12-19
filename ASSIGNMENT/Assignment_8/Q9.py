#9. Write a program to check if entered number is a palindrome or not.

def reverse(num):
    original = num
    rev = 0
    while num > 0:
        rev = rev * 10 + (num % 10)
        num //= 10
    return rev == original
    
num = int(input("Enter number:"))
if(reverse(num)):
    print('Number is a Palindrome')
else:
    print('Number is not a Palindrome')