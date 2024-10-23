#
# Gaukhar
# 2024/10/23
# Tip calculator

num_people = int(input("How many people are dining? "))

total_amount = 0

for i in range(1, num_people + 1):

    amount = float(input(f"Enter the amount spent by person {i}: "))

    total_amount += amount

tip_percentage = float(input("Enter the tip percentage: "))

tip_amount = total_amount * (tip_percentage / 100)

total_bill = total_amount + tip_amount

print(f"The total bill including tip is: ${total_bill:.2f}")