#Write a program to swap two numbers without using third variable.

x = 30
y = 10

print(f'Before swapping x is {x} and y is {y}')

#x,y=y,x
    #OR
x = x+y
y = x-y
x = x-y

print(f'After swapping x is {x} and y is {y}')