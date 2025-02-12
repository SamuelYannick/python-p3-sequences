
# Steps: 
# Define 2 inital variables 0 and 1
# Use for loop n times while adding the previous value with the current value
# Print the values(the sum of the last 2 numbers) as the current value

def print_fibonacci(length):
    value_1, value_2 = 0, 1
    print(value_1, end = ", ")
    print(value_2, end = ", ")
    for i in range(length):
        new_value = value_1 + value_2
        print(new_value, end = ", ")
        value_1 = value_2
        value_2 = new_value

print_fibonacci(10)

