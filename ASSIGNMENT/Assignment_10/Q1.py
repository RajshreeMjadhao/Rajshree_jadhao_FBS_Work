#Write a program to find sum of all elements of list

def sum_of_ele(li):
    sum = 0
    for ind in range(len(li)):
        sum = sum + li[ind]
    return sum

li =[15, 12, 24, 35]
result = sum_of_ele(li)
print(result)
