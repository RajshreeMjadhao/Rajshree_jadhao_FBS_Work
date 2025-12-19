# Q7.i.
n = int(input("Enter n: "))
sum = 0

for i in range(1, n + 1):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    sum += fact
print("Sum =", sum)

# Q7.ii.
n = int(input("Enter n: "))
sum = 0

for i in range(1, n + 1):
    sum += n ** i
print("Sum =", sum)
      
# Q7.iii.      
n = int(input("Enter n: "))
sum = 0
term = 1

for i in range(n):
    sum += term
    term *= 2

print("Sum =", sum)


# Q7.iv.
a = int(input("Enter a: "))
sum = 0

for i in range(1, 11):
    sum += (a ** i) / i

print("Sum =", sum)


# Q7.v.
x = int(input("Enter x: "))
n = int(input("Enter n: "))
sum = 0
sign = 1
den = 1

for i in range(1, n + 1):
    sum += sign * (x ** i) / den
    sign *= -1
    den += 2

print("Sum =", sum)