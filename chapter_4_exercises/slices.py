kinds_of_pizza = ["roni", "chee", "supreme"]
for pizza in kinds_of_pizza:
    print(f"I love {pizza} pizza!")
print ("I really love pizza!!!")
#end of original exercise "pizzas.py"

kinds_of_pizza.append("veggie")
kinds_of_pizza.append("meat loverz")
kinds_of_pizza.append("dessert")
first_3 = kinds_of_pizza[0:3]
print(f"\nThe first three items in the list are:")
for pizza in first_3:
    print (pizza)
#Added some kinds of pizza (strings) to the list kinds_of_pizza. sliced the list and assigned slice to first_3 variable. 
#Printed each item in list.
    
middle_3 = kinds_of_pizza[1:4]
print(f"\nThree items from the middle of the list are:")
for pizza in middle_3:
    print(pizza)
# Sliced list (kinds_of_pizza) and printed each element.
    
print(f"\n{len(kinds_of_pizza)}")
#verifying list legnth

print(f"\nThe last three items in the list are:")
last_3 = kinds_of_pizza[3:]
for pizza in last_3:
    print(pizza)
# Sliced the list again and assigned slice to last_3 variable. Printed string (line 25) and elements in the last_3 variable.