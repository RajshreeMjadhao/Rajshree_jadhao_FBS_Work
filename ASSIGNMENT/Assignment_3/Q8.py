'''Write a program to prompt user to enter userid and password. After verifying
userid and password display a 4 digit random number and ask user to enter the
same. If user enters the same number then show him success message otherwise
failed. (Something like captcha)'''
# import random
# user_id = input("enter username:")
# user_password = input("enter password:") 

# if (user_id == "admin" and user_password == "151"):
#     print("login sussessfully")
#     captcha = random.randint(100,999)

#     print("Captcha:",captcha)
#     user_captcha == int(input("enter captcha:"))

#     if (user_captcha == captcha):
#         print("sussecc")

import random

userid = input("Enter userid: ")
password = input("Enter password: ")

if userid == "raji" and password == "234":
    print("Login successful")

    captcha = random.randint(1099, 9900)
    print("Captcha:", captcha)

    user_captcha = int(input("Enter captcha: "))

    if user_captcha == captcha:
        print("Success")
    else:
        print("Failed")
else:
    print("Wrong userid or password")