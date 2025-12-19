# WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.
Str = int(input("Enter start:"))
End = int(input("Enter End:"))

for i in range (Str, End + 1):
    if(i % 7 == 0 and i % 5 == 0):
        print(i)