#5. Sum of all prime numbers between 1 to n

def isPrime(num):
    if(num < 2):
        return False
    for i in range(2, int(num**0.5)+1):
        if(num % i == 0):
            return False
    return True

def sum_primes(n):
    sum = 0
    for i in range(1, n+1):
        if(isPrime(i)):
            sum += i
    return sum

n = int(input("Enter n: "))
print("Sum of prime numbers =", sum_primes(n))