p = float(input('enter principle:'))
t = float(input('enter time:'))
r = float(input('enter rate:'))

amount = p*((1+r/100)**t)
ci = amount-p
print(f'total compound amount is {ci}.')