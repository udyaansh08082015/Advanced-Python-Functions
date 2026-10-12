items= ["pencil","eraser","sharpener","glue","notebook"]
stock_counts = [12,0,4,23,5]

inventory = {item : count for item,count in zip(items,stock_counts)}
print("Full Inventory ;",inventory)

in_stock_items = [item for item in items if inventory[item]>0]
print("Items in stock:",in_stock_items)


choose  = str(input("Choose an item you want to buy")).lower()

if choose not in inventory or inventory[choose]==0:
    print(choose,"item not in stock")
    exit()

prices = [5,25,30,15,40]
markup = int(input("Enter the markup amount for the items"))

marked_up_prices = list(map(lambda p: p + markup,prices))
print("Marked Up Prices",marked_up_prices)

item_index = items.index(choose)
chosen_price = marked_up_prices[item_index]
print("price:",chosen_price)

inventory[choose] = inventory[choose] - 1
print(choose,"Purchased!")

print("==================================")
print("======SCHOOL INVENTORY CHECKER======")
print("Item Bought",choose)
print("Price Paid",chosen_price)
print("Updated Inventory",inventory)
print("=================================")