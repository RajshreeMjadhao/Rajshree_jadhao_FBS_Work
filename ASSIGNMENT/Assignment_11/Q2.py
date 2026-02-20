# 2. Python Program to Merge Two Lists and Sort it
def merge_Sort(li1 ,li2):
    a = li1 + li2
    a.sort()
    return a

list1 = [23, 45, 56, 67]
list2 = [21, 11, 22, 32, 43]
result = merge_Sort(list1, list2)
print(result)