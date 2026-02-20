#5. Find all of the words in a string that are less than 5 letters (take input from user)
str = input("Enter a letter: ")
small_words = [word for word in str.split() if (len(word) < 5)]
print(f'Words with less than 5 letters: {small_words}')
