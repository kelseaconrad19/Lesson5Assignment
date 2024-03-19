# Task 1: Write a function that lets the user add items to a list.
def add_to_list():
    shopping_list = []
    correct_input = True
    while correct_input:
        feature = input("Add an item or remove an item? Type 'add', 'remove', or 'exit': ").lower()
        if feature == "add":
            new_item = input("What do you want to add?: ")
            shopping_list.append(new_item)
        # Task 2: Include a feature to remove items from the list.
        elif feature == "remove":
            remove_item = input("What would you like to remove?: ")
            shopping_list.remove(remove_item)
        else:
            correct_input = False
    return shopping_list


# Task 3: Add a function that prints out the entire list in a formatted way.
def print_list(shopping_list):
    for item in shopping_list:
        print(item, sep="\n")


grocery_list = add_to_list()
print_list(grocery_list)
