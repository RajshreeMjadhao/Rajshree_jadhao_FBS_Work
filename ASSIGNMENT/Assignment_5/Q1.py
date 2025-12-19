# 1. Write a program to prompt user to enter userid and password.
# If Id and password is incorrect give him chance to re-enter the credentials. 
# Let him try 3 times. 
# After that program to terminate.
for i in range(3):
    uid = input("Enter userid: ")
    pwd = input("Enter password: ")

    if uid == "shree" and pwd == "1403":
        print("Login successful")
        break
    else:
        print("Wrong credentials")

else:
    print("Program terminated")