#2. Python Program to Remove the nth Index Character from a Non-Empty String
str = 'Data Science'
n = int(input("Enter index: "))
value = ''

for ind in range(len(str)):
    if (ind != n):
        value += str[ind]

print(value)
