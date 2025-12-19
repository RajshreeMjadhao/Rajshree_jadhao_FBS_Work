start = int(input("Enter start: "))
end = int(input("Enter end: "))

for num in range(start, end + 1):
    temp = num
    sum = 0
    digits = len(str(num))

    while temp > 0:
        d = temp % 10
        sum += d ** digits
        temp //= 10

    if sum == num:
        print(num)