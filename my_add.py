
#Gaukhar
#2024/11/06

def my_add(input_list):
    sum = 0
    for x in input_list:
        sum += int(x)
    return sum

# Ask the user for input
input_data = input("Enter numbers separated by spaces: ").split()

# Convert input data to a list of integers
input_data = [int(x) for x in input_data]

# Calculate the sum
result = my_add(input_data)

# Print the result
print(f"Answer: {result}")
