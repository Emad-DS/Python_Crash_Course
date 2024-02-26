#5-3
alien_color = ['green','yellow','red']
if 'green' in alien_color:
    print('Add 5 points')
if 'blue' in alien_color:
    #do nothing 
    print('')

#5-4
alien_color = 'green'
if alien_color == 'green':
    print("Add 5 points")
else:
    print("Add 10 points")

alien_color = 'yellow'
if alien_color == 'green':
    print("Add 5 points")
else:
    print("Add 10 points")

#5-5
alien_color = 'yellow'
if alien_color == 'green':
    print("Add 5 points")
elif alien_color == 'yellow':
    print("Add 10 points")
elif alien_color == 'red':
    print('Add 15 points')
else:
    print('No points')

#5-6
age = 0
if age < 2:
    print("baby")
elif age < 4:
    print("toddler")
elif age < 13:
    print("kid")
elif age < 20:
    print("teenager")
elif age < 65:
    print("adult")
elif age >= 65:
    print("elder")
else:
    print("invalid entry")

#5-7
favorite_fruits = ['apple','banana','mango']
fruit_list = ['apple','pineappke','oranges','mango','banana']
for fruit in fruit_list:
    if fruit in favorite_fruits:
        print(f"{fruit} is your favorite")
    else:
        print(f"no thanks, not {fruit}")




