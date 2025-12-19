#Convert distant given in feet and inches into meter and centimeter.

feet = float(input('Enter the distance in feet :'))

inches = float(input('Enter the distance in inches :'))

total_inches = (feet*12)+inches 

cm = total_inches*2.54 #(1 inch = 2.54)

meters = cm/100

print(f'Distance in meters {meters} and Distance in Centimeters {cm}.')