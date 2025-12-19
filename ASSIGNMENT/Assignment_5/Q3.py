n = int(input("Enter number of person: "))
ticket = int(input("Enter ticket price: "))

total = 0

for i in range(n):
    age = int(input("Enter age: "))

    if age < 12:
        amount = ticket * 0.7
    elif age > 59:
        amount = ticket * 0.5
    else:
        amount = ticket

    total += amount

print("Total amount:", total)