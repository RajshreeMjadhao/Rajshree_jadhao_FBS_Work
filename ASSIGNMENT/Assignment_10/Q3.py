#Write a program to find the second largest element in the list.

def Sec_lar_val(li):
    max = li[0]
    Slar = 0
    for ind in range(0, len(li)):
        if(li[ind] > max):
            Slar = max
            max = li[ind]
            
        elif(li[ind] >Slar):
            Slar = li[ind]
    return Slar

li = [45, 76, 87, 34, 65]

print("second largest element is", Sec_lar_val(li))