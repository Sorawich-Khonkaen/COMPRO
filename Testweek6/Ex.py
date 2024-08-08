inventory = [
    ["Apple", 50, 0.75],
    ["Banana", 100, 0.50],
    ["Orange", 75, 0.80]
]

def update_inventory(inventory, item_name, quantity_sold):
    for item in inventory:
      if item_name == item[0]:
          item[1] = item[1] - quantity_sold 
            
def calculate_total_value(inventory):
    total_value = sum(item[1] * item[2] for item in inventory)
    return total_value

def find_most_expensive(inventory):
    most_expensive = max(inventory, key=lambda item: item[2])
    return most_expensive[0]

def add_item(inventory, item_name, quantity, price):
    for item in inventory:
        if item_name == item[0]:
            item[1] = quantity
            item[2] = price
            return
    inventory.append([item_name, quantity, price])


update_inventory(inventory,"Banana",20)
print(inventory)
total_value = calculate_total_value(inventory)
print(total_value)
most_expensive = find_most_expensive(inventory)
print(most_expensive)
add_item(inventory, "Eggs", 30, 0.25)
print(inventory)