#Define the menu of restaurant
menu = {
    'Pizza':40,
    'Pasta':50,
    'Noodles':60,
    'Coffee':30,
    'Burger':45,
    'Momos':20,
    'Spring roll':25,
}

#Greet
print("WELCOME TO PYTHON RESTAURANT")
print("pizza: Rs40\nPasta: Rs50\nNoodles: Rs50\nCoffee: Rs30\nBurger: Rs45\nMomos: Rs20\nSpring roll: Rs25 ")
order_total = 0
#40 + 25 = 65

item_1 = input("Enter the name of item you wanrt to order = ")
if item_1 in menu:
    order_total += menu[item_1]  #0 + 50
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not avaialable yet!")

another_order = input("Do you want to add another item? (Yes/No) ") 
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item{item_2} is not avaialable! ")

print(f"The total amount of items to pay is {order_total}")        