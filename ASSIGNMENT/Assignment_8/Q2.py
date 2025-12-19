def areaOfCircle(r):
    area = 3.14 * (r*2)
    return area

r = int(input("Enter radius of a circle:"))
result = areaOfCircle(r)
print(f'Area of a circle is {result}')