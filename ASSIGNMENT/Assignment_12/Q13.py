#13. Python Program to count number of digits and letters in a string.
str = 'Data Science'
d = 0
l = 0

for char in str:
    if (char.isdigit()):
        d += 1
    elif char.isalpha():
        l += 1

print(f'Digits:{d}')
print(f'Letters:{l}')
