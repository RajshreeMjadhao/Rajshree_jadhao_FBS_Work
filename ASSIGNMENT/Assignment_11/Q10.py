def remove(li):
    result = []
    for i in li:
        if (i % 2 != 0):
            result.append(i)
    return result

li = [1, 2, 3, 4, 5, 6]
print(f'After removing even number: {remove(li)}')