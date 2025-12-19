given_days = int(input('Enter number of days:'))

years = given_days//365
weeks = (given_days%365)//7
days = given_days-(365*years)-(7*weeks)

print(f'Number of years {years}')
print(f'Number of weeks {weeks}')
print(f'Number of days {days}')

