import math
a = float(input('Enter value for a:'))
b = float(input('Enter value for b:'))
c = float(input('Enter value for c:'))

d = b**2 - 4*a*c

root1 = (-b + d**0.5)/2*a
root2 = (-b - d**0.5)/2*a

print(f'The root of a quadratic equation root1 is {root1} and root2 is {root2}.')