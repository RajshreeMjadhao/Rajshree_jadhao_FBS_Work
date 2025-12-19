#Write a program to calculate profit or loss.
CP = float(input("enter cost price:"))
SP = float(input("enter selling price:"))

if SP > CP:
    print("profit:")
elif SP < CP:
    print("loss:")
else:
    print("no profit, no loss")
