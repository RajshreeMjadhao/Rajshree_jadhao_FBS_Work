#7. Python Program to Find the Intersection of Two Lists
def intersection_list(li1,li2):
    n = []
    for i in li1:
        if(i in li2 and i not in n):
            n.append(i)
    return n

list1 = [9, 8, 7, 6, 5]
list2 = [3, 4, 5, 6, 7]
result = intersection_list(list1,list2)
print(result)