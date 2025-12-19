#Write a program to input all sides of a triangle and check whether triangle is valid or not.
a = int(input("Enter angle a:"))
b = int(input("Enter angle b:"))
c = int(input("Enter angle c:"))

if a+b>c and a+c>b and b+c>a:
     print(f'Valid triangle.')
else:
    print(f'Invalid triangle.')