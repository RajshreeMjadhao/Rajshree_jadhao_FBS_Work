def sort_list(li):
    n = len(li)
    for i in range(n):
        for j in range(0, n-i-1):
            if(len(li[j]) > len(li[j + 1])):
                temp = li[j+1]
                li[j+1] = li[j]
                li[j] = temp
    return li
li = ["Rajshree", "Mahadeo", "Jadhao"]
result = sort_list(li)
print(result)