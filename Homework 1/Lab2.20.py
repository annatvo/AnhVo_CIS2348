# Anh Vo
# PSID: 2037824
# Lab 2.20

lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water_cups = float(input('Enter amount of water (in cups):\n'))
nectar_cups = float(input('Enter amount of agave nectar (in cups):\n'))
org_serving = int(input('How many servings does this make?\n'))
# FIXME (1): Finish reading other items into variables, then output the three ingredients
print(f'\nLemonade ingredients - yields {org_serving:.2f} servings')
print(f'{lemon_juice_cups:.2f} cup(s) lemon juice')
print(f'{water_cups:.2f} cup(s) water')
print(f'{nectar_cups:.2f} cup(s) agave nectar\n')
# FIXME (2): Prompt user for desired number of servings. Convert and output the ingredients
serving = int(input('How many servings would you like to make?\n'))
print(f'\nLemonade ingredients - yields {serving:.2f} servings')
print(f'{lemon_juice_cups*(serving/6):.2f} cup(s) lemon juice')
print(f'{water_cups*(serving/6):.2f} cup(s) water')
print(f'{nectar_cups*(serving/6):.2f} cup(s) agave nectar\n')
# FIXME (3): Convert and output the ingredients from (2) to gallons
print(f'Lemonade ingredients - yields {serving:.2f} servings')
print(f'{lemon_juice_cups*(serving/6)/16:.2f} gallon(s) lemon juice')
print(f'{water_cups*(serving/6)/16:.2f} gallon(s) water')
print(f'{nectar_cups*(serving/6)/16:.2f} gallon(s) agave nectar')
