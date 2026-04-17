from data_package import remove_duplicates, strip_whitespaces, calculate_mean, find_maximum, find_minimum

user_input = input("Enter a comma-separated list of numbers (e.g., 12, 5, 12, 8 , 21): ")

try:
    parts = user_input.split(",")
    cleaned_strings = strip_whitespaces(parts)
    numbers = []
    for s in cleaned_strings:
        if s == "":
            continue
        numbers.append(float(s))
    unique_numbers = remove_duplicates(numbers)
    print("\nCleaned and unique data:", unique_numbers)
    print("-" * 20)
    print(f"Mean: {calculate_mean(unique_numbers):.2f}")
    print(f"Maximum: {find_maximum(unique_numbers):.1f}")
    print(f"Minimum: {find_minimum(unique_numbers):.1f}")
except ValueError:
    print("Data Error: Please make sure you only enter numbers separated by commas.")
