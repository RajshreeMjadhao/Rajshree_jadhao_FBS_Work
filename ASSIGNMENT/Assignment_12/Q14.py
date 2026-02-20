# 14. Python Program to count the occurrences of ach word in a string.
str = input("Enter string: ")
words = str.split()

for w in words:
    print(f'{w}:{words.count(w)}')
