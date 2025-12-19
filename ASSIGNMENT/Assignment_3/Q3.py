#Write a program to input angles of a triangle and check whether triangle is valid or not.
a = int(input("Enter angle a:"))
b = int(input("Enter angle b:"))
c = int(input("Enter angle c:"))
n = a+b+c
if n == 180:
    print(f'{n} valid triangle.')
else:
    print(f'{n} invalid triangle.')