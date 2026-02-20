def create_list(n):
    num = []
    sq = []
    cub = []
    for i in range(1, n + 1):
        num.append(i)
        sq.append(i*i)
        cub.append(i*i*i)

    print(f'Number: {num}')
    print(f'Square: {sq}')
    print(f'Cube: {cub}')

# create_list(3)
result = create_list(3)
print(result)
