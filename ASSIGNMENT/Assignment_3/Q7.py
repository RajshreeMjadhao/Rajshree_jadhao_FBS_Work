# Write a program to check if user has entered correct userid and password.
user_id = input("enter username:")
user_password = input("enter password:") 

if (user_id == "admin" and user_password == "1512"):
    print("logged in successfully.")
else:
    print("wrong user Id or password.")
 