kinds_of_pizza = ["roni", "chee", "supreme"]
for pizza in kinds_of_pizza:
    print(f"I love {pizza} pizza!")
print ("I really love pizza!!!")
#end of original exercise "pizzas.py"

friend_pizzas = kinds_of_pizza[:]
kinds_of_pizza.append("veggie")
friend_pizzas.append("meat loverz")
print(f"\nMy favorite pizzas are:")
for pizza in kinds_of_pizza:
    print(pizza)
print(f"\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
'''
Make a copy of the list of pizzas, and call it friend_pizzas . Then, do the following:
 •  Add a new pizza to the original list.
 •  Add a different pizza to the list friend_pizzas .
 •  Prove that you have two separate lists. Print the message My favorite pizzas are: , and then use a for loop to print the first list. 
    Print the message My friend's favorite pizzas are: , and then use a for loop to print the second list. 
    Make sure each new pizza is stored in the appropriate list.
'''