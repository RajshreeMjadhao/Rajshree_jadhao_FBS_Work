#WAP to calculate selling price of book based on cost price and discount.

cost = float(input('Enter the cost of book :'))
disc_percent = float(input('Enter the Discount percentage :'))

disc_amount = cost*(disc_percent/100)

sale_price = cost-disc_amount

print(f'Sale price of the book is {sale_price}')