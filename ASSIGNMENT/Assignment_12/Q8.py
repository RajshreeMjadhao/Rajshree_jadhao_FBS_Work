#8. Python Program to Remove the Characters of Odd Index Values in a String
str = input("Enter string: ")
result = ""

for ind in range(len(str)):
    if (ind % 2 == 0):
        result += str[ind]

print(result)

