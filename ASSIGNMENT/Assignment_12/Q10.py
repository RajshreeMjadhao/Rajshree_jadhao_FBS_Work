#10.Python Program to Take in Two Strings and Display the Larger String
# without Using Built-in Functions

str1 = 'Data Science'
str2 = 'FirstBit'

char1 = 0
for ch in str1:
    char1 += 1

char2 = 0
for ch in str2:
    char2 += 1

if (char1 > char2):
    print("Larger string:", str1)
else:
    print("Larger string:", str2)
