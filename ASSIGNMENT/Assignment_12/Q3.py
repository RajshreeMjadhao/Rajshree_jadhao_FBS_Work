#3. Python Program to Detect if Two Strings are Anagrams
str1 = input('Enter String 1:')
str2 = input('Enter String 2:')

if (sorted(str1) == sorted(str2)):
    print("Anagram")
else:
    print("Not Anagram")
