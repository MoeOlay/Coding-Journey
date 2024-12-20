menu_dict = {
    "Hot Dog" : 1.50,
    "Slice of Pizza": 1.99,
    "Whole Pizza": 9.95,
    "Soft Drink": 0.59
}
hot_dogs= int(input("Please enter the number of Hot Dogs: "))
pizza_slices= int(input("Please enter the number of Pizza Slices: "))
whole_pizzas=int(input("Please enter the number of Whole Pizzas: "))
soft_drinks=int(input("Please ener the number of Soft Drinks: "))
total_cost= menu_dict["Hot Dog"]*hot_dogs + menu_dict["Slice of Pizza"]*pizza_slices+menu_dict["Whole Pizza"]*whole_pizzas+menu_dict["Soft Drink"]*soft_drinks
print(f'The total cost of the order is ${total_cost:.2f}')