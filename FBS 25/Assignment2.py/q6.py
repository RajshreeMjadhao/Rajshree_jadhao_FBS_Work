#WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.
basic = float(input('Enter the basic salary :'))

da = 0.10*basic
ta = 0.12*basic
hra = 0.15*basic

total_salary = basic + ta + da + hra
print(f'Dearness Allowance {da} ,Travel Allowance {ta} and House Rent Allowance{hra}')
print(f'Total salary of the employee is {total_salary}')