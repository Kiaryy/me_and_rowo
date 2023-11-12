# "i was thinking like, making a receipt thing, like, you input an item and its price and how many of them,
# and then you print the receipt"
# - my silly hot and cute bf

# variable defining
total = 0
cart = []

# user friendly input
print('This program will create a receipt for multiple items inputted. Type "quit" during item selection to quit.')

# while loop
while True:
    item = input('What is the item? ')
    if item.upper() == 'QUIT':
        break
    price = float(input("What is the item's price? "))
    quantity = int(input('How many is there? '))
    cart.append((item, price, quantity))
    total = total + (price * quantity)

print('--------------------')

for item in cart:
    print(f'Item: {item[0]}')
    print(f'Price: ${item[1]}')
    print(f'Quantity: {item[2]}')
    print('--------------------')

print(f'Total: ${total}')
print('--------------------')