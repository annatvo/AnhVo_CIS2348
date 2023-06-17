# Anh Vo
# PSID: 2037824
# lab 3.19

import math
height = int(input('Enter wall height (feet):\n'))
width = int(input('Enter wall width (feet):\n'))
area = height * width
gallon = area/350
print(f'Wall area: {area} square feet')
print(f'Paint needed: {gallon:.2f} gallons')
print(f'Cans needed: {math.ceil(gallon)} can(s)\n')
color = input('Choose a color to paint the wall:\n')
if color == 'red':
    cost = 35 * math.ceil(gallon)
elif color == 'blue':
    cost = 25 * math.ceil(gallon)
elif color == 'green':
    cost = 23 * math.ceil(gallon)
else:
    cost = 0
print(f'Cost of purchasing {color} paint: ${cost}')