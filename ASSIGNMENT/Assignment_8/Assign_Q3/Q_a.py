#Write a program to find sum of following series using functions :
#a. 1+ 2 + 3 + 4+..... + n

def sumOfSeries(num):
    if(num <= 0):
        return 0
    else:
        return num + sumOfSeries(num - 1)
    
num = int(input("Enter a number:"))
print(sumOfSeries(num))