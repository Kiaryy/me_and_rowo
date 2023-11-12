import os #! This library lets you do stuff with the os in this case i'll be using it to execute a terminal command

total_sales = 0
while True:
    shopping_cart = list() # Empty list that will contain the items. 
    # The list will look like this: [(name, price, quantity), ("burger pack", 25, 1)]
    print("---------Checkout---------\nEnter 'quit' at any moment to close the program.")
    while True:
        try:
            item_name = input("Enter the name of the product: ").lower() # Gets a string and converts it to lower case
            if item_name == "quit": # If the string equals 'quit', the program will break from the while loop
                break
            
            item_price = input("Enter the price of the product: $").lower()
            if item_price == "quit":
                break
            item_price = float(item_price) # Casts the variable to int
            
            item_quantity = input("How many items will be purchased: ").lower()
            if item_quantity == "quit":
                break
            item_quantity = int(item_quantity)
            
            while item_quantity<1: # If the user inputs an item quantity lesser than 1, the program will asks for another input
                print("There cannot be zero items.")
                item_quantity = int(input("How many items will be purchased: "))
        except ValueError:
            print("ERROR: Invalid Input")
            continue
        
        print("---------Item Added---------")
        shopping_cart.append((item_name, item_price, item_quantity)) # Adds the item to the shopping cart

    os.system("cls") #! This will exeute the command 'cls' in the terminal. cls is used to clear the terminal.
    print("---------Receipt---------")
    total = 0
    for item in shopping_cart: # Prints out the shopping cart, item by item
        print(f"---------Item №{shopping_cart.index(item)+1}---------")
        print(f"Name: {item[0].title()}")
        print(f"Price: ${item[1]}")
        total += (item[1]*item[2])
        print(f"Quantity: {item[2]}")
        print("-------------------------")
        print(f"\tTotal: {total}")
    
    total_sales += total
    
    if input("Do you want to make another receipt? Y/n: ").lower() == 'n':
        print(f"Today's total sales were of ${total_sales}")
        print("-------------------------")
        print("Goodbye.")
        break
    os.system("cls")