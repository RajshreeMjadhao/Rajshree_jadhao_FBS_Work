# 1. Python Program to Put Even and Odd elements of a List into two Different Lists
def evenOdd(li):
    even = []
    odd = []
    for ind in range(len(li)):
        if(ind % 2 == 0):
            even.append(ind)
        else:
            odd.append(ind)
    print(f'Even Elements:  {even}')
    print(f'Odd Elements:  {odd}')
li = [1, 2, 3, 4, 5, 6, 7]
result = evenOdd(li)
print(result)