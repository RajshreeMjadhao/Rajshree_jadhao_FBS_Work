#b. 1!+ 2! + 3! + 4!+..... + n!

def fact(num):
    if(num <= 0):
        return 1
    else:
        return num * fact(num - 1)

def sumOfFact(n):
    if(n <= 0):
        return 0
    else:
        return fact(n) + sumOfFact(n - 1)


num = int(input("Enter number:")) 
result = sumOfFact(num)
print(result)