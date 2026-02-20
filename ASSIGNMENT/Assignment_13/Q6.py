# 6. Python Program to Multiply All the Items in a Dictionary
def multiply_dict_values(d):
    result = 1
    for value in d.values():
        result = result * value
    return result

# Example dictionary
my_dict = {'a': 2, 'b': 3, 'c': 4}

print(multiply_dict_values(my_dict))
