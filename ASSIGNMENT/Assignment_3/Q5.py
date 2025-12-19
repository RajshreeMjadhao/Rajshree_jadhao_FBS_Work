#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
a = int(input("Enter angle a:"))
b = int(input("Enter angle b:"))
c = int(input("Enter angle c:"))

if a == b == c:
    print("Equilateral triangle")
elif a==b or b==c or a==c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")