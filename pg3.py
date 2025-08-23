items = ["Apple", "Banana", "Cherry", "milk", "Date"]
print("Original list:", items)
print(items[0])
print(items[1])
print(items[1:3])

items.append("bread")
print(items)

if "milk" in items:
    print("Milk is in the list")
else:
    print("milk is not in the list")

items.remove("milk")
print(items)

items_inventory = {
    "Apple": {"price": 30, "quantity": 10},
    "Banana": {"price": 10, "quantity": 15},
    "Cherry": {"price": 50, "quantity": 7},
    "Date": {"price": 60, "quantity": 5},
    "bread": {"price": 20, "quantity": 8}
}

while True:
    print("\n1) Add 2) View 3) Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        item = input("Enter item to add: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        items.append(item)
        items_inventory[item] = {"price": price, "quantity": quantity}
        print(items)
    
    elif choice == "2":
        for i, it in enumerate(items, start=1):
            if it in items_inventory:
                data = items_inventory[it]
                print(i, it, "- Price:", data["price"], "Quantity:", data["quantity"])
            else:
                print(i, it, "- No inventory data")
    
    elif choice == "3":
        break  

print("\n📊 Fruit Inventory:")
print("{:<10} {:>10} {:>10}".format("Name", "Price", "Quantity"))
print("-" * 32)
for name, details in items_inventory.items():
    print("{:<10} {:>10} {:>10}".format(name, details["price"], details["quantity"]))
 