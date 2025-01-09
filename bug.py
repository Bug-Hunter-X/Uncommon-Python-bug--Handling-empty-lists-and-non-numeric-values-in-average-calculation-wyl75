def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

# Example usage with an empty list
average = calculate_average([])
print(f"Average: {average}")

#Example usage with a list containing non-numbers
my_list = [1,2,3,'a']
average = calculate_average(my_list)
print(f"Average: {average}")