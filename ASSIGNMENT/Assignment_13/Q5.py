def sum_dictionary(d):
    total = 0
    for key in d:
        total = total + d[key]
    return total

my_dict = {"age": 22, "height": 167, "weight": 50}
print("Sum of values:", sum_dictionary(my_dict))