#7. Python Program to Calculate the Length of a String Without Using a Library Function
str = input("Enter string: ")
count = 0

for char in str:
    count += 1

print(f'Length of string is: {count}')
