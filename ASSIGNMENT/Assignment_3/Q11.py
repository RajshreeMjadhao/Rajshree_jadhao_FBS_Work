total = 0
age = int(input("Enter age: "))
ticket = int(input("Enter ticket amount: "))
for i in range(5):

    if age < 12:
        ticket = ticket * 0.7
    elif age > 59:
        ticket = ticket * 0.5

    total += ticket

print("Total ticket amount:", total)