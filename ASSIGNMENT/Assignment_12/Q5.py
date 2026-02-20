#5. Python Program to Count the Number of Vowels in a String

str = 'Data Science'
# print(str.count('a'))

count = 0

for char in str:
    if (char in 'FirstBit'):
        count += 1

print(f'Number of Vowels present is: {count}')

