#4. Remove all of the vowels in a string (take input from user)

str = input("Enter a string: ")
no_vowels = ''.join([ch for ch in str if (ch.lower() not in 'python')])
print(f"String without vowels: {no_vowels}")