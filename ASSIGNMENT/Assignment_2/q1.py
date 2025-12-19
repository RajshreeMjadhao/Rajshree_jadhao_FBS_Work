#Convert the time entered in hh,min and sec into seconds.

num = int(input('Enter the number :'))

hour = num//3600
hour1 =  num%3600
minute = hour1//60
second = hour1%60

print(f'hour {hour},minute {minute} and second {second}')