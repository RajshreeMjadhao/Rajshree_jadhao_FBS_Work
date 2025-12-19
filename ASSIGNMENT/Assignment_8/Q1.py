# Write a program to calculate area of rectangle

def areaOfRect(l, b):
    area = l * b
    return area

l = int(input("Enter length of rectangle:"))
b = int(input("Enter breadth of rectangle:"))
result = areaOfRect(l, b)
print(f'Area of rectangle is {result}')

