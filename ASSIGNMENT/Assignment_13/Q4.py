def sq_dict(n):
    d = {}
    for i in range(1, n + 1):
        d[i] = i*i
    return d

num = int(input("Enter number:"))
print(sq_dict(num))