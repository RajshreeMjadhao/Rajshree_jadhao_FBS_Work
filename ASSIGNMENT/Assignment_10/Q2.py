#Write a program to find maximum and minimum element in a list.

def maxMinEle(li):
    max = li[0]
    min = li[0]
    for ind in range(0, len(li)):
        if(max < li[ind]):
            max = li[ind]
        if(min > li[ind]):
            min = li[ind]
    return max,min
    
li = [54, 67, 78, 43, 56, 79, 24]
Max_Ele, Min_Ele = maxMinEle(li)
print(f'Maximun element:{Max_Ele}')
print(f'Minimun element:{Min_Ele}')


