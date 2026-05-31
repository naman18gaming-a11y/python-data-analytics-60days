#shopping cart 
item = ["apple", "banana", "orange", "grape", "mango"]
print("Items in the cart:", item)
remove_item = input("Enter the item you want to remove from the cart: ")
if remove_item in item:
    item.remove(remove_item)
    print(f"{remove_item} has been removed from the cart.")
else:
    print("Item not found in the cart.")
    print("Current items in the cart:", item)
    print("Total items in the cart:", len(item))
    exit()