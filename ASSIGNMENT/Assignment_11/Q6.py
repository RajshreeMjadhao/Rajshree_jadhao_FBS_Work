#6. Python Program to Find the Union of two Lists
def union_list(li1, li2):
    union = []
    for i in li1:
        if(i not in union):
            union.append(i)
    for i in li2:
        if(i not in union):
            union.append(i)
    return union

list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [3, 4, 8, 9]
result = union_list(list1,list2)
print(result)
