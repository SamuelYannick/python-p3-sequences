
# Steps: 
# Define 2 inital variables 0 and 1
# Use for loop n times while adding the previous value with the current value
# Print the values(the sum of the last 2 numbers) as the current value

def print_fibonacci(length):
    value_1, value_2 = 0, 1
    results_list = []
    
    if length > 0:
        results_list.append(value_1)
    if length > 1:
        results_list.append(value_2)
    
    for _ in range(2, length):
        new_value = value_1 + value_2
        value_1 = value_2
        value_2 = new_value
        results_list.append(new_value)
    
    print(results_list)

print_fibonacci(10)
