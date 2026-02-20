#6. Python Program to Take in a String and Replace Every Blank Space with Hyphen
str = input('Enter String:')
result = ""

for char in str:
    if (char == ' '):
        result += '-'
    else:
        result += char

print(result)
