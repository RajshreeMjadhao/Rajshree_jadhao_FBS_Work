def add_dict(d):
    num1 = input('Enter key:')
    num2 = input('Enter value:')
    d[num1] = num2
    print(f'Dictionary: {d}')

my_dict = {"name" : "Shree"}
add_dict(my_dict)
