def Sec_max_val(li):
    max = li[0]
    Smax = 0
    for ind in range(0, len(li)):
        if(li[ind] > max):
            Smax = max
            max = li[ind]
            
        elif(li[ind] >Smax):
            Smax = li[ind]
    return Smax

li = [45, 76, 87, 34, 65]

print("second max value is", Sec_max_val(li))