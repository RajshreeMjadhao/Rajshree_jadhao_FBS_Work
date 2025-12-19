#Find the sum of three-digit number.

num = int(input('Enter a 3 digit number :'))

d1 = num//100
d2 = (num//10)%10
d3 = num%10

sum = d1 + d2 + d3

print(f'Sum of a three digit is {sum}')