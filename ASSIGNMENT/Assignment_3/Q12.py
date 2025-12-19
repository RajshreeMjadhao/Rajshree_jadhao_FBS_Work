# 12. Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a number:"))
rev = int(str(num) [::-1])
if num == rev:
    print("Palindrome")
else:
    print("Not palindrome")