def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 #Handle list with no numbers
    return sum(numeric_numbers) / len(numeric_numbers)

# Example usage with an empty list
average = calculate_average([])
print(f"Average: {average}")

#Example usage with a list containing non-numbers
my_list = [1,2,3,'a']
average = calculate_average(my_list)
print(f"Average: {average}")

# Example usage with a list of numbers
my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"Average: {average}") 