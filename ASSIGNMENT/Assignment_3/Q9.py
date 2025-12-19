# Input 5 subject marks from user and display grade(eg.First class,Second class ..)
total = 0
marks = int(input("Enter marks:"))
for i in range(5):
    total += marks

avg = total/5
if (avg >= 60):
    print("First class")
elif (avg >= 50):
    print("Secong class")
elif (avg >= 40):
    print("Pass")
else:
    print("Fail")