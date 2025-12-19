# Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.

def linearSearch(li, searchEle):
    for ind in range(0, len(li)):
        if(li[ind] == searchEle):
            return ind
    else:
        return -1
        
li = [25, 36, 70, 26, 55, 89]
ele = int(input("Enter number to find:"))
result = linearSearch(li, ele)
if(result != -1):
    print(f'{ele} is present at index {result}.')

else:
    print(f'{ele} is not present in list .')

