# 11.WAP to check if a given number is Armstrong number or not. For each task create separate functions.
def countOfDigit(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count


num = int(input("Enter number: "))
print(countOfDigit(num))