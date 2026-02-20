#12. Python Program to count number of lowercase characters in a string.
str = 'Data Science'
num = 0
for char in str:
    if (char.islower()):
        num += 1

print(f'Numbers of Lowercase:{num}')
