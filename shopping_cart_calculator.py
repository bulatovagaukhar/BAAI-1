#
# Gaukhar
# 2024/10/23
# Shopping cart calculator

num_items = int(input("How many items do you want to buy? "))
total_cost = 0

for i in range(num_items):
    item_name = input(f"Enter the name of item {i + 1}: ")
    item_price = float(input(f"Enter the price of {item_name}: "))
    item_quantity = int(input(f"Enter the quantity of {item_name}: "))
    item_total = item_price * item_quantity
    total_cost += item_total
    print(f"Total cost for {item_name}: {item_total}")

print(f"Total cost of your shopping cart: {total_cost}")