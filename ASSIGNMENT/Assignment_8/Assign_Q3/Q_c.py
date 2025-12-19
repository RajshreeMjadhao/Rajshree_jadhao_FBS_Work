#c. 1^1 + 2^2 + 3^3+ ...... n^n

def square(num):
    if(num <= 0):
        return 1
    else:
        return num * num
    
def sumOfSqu(n):
    if(n <= 0):
        return 0
    else:
        return square(n) + sumOfSqu(n - 1)
    
num = int(input("Enter number:")) 
result = sumOfSqu(num)
print(result)