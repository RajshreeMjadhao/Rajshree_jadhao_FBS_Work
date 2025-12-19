# 9. WAP to print all numbers in a range divisible by a given number.
str = int(input("Enter Start:"))
end = int(input("Enter End:"))
num = int(input("Enter divisor:"))

for i in range(str, end + 1):
    if(i % num == 0):
        print(i)