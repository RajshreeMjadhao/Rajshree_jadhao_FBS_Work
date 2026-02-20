#6. Use a dictionary comprehension to count the length of each word in a sentence (take input from user)
str = input("Enter a sentence: ")
word_length = {word: len(word) for word in str.split()}
result = word_length
print(result)
