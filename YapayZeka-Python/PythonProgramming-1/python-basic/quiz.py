####################################################

# Given list
my_list = [3, 8, 1, 6, 0, -4, 5]

# Find the smallest element
min_value = min(my_list)

# Print the result
print("The smallest element:", min_value)

####################################################


def year_to_century(year):
    # Check if the input year is within the specified range
    if 1 <= year <= 2024:
        # Check if the year ends with "00"
        if year % 100 == 0:
            century = year // 100
            return century + 1
        else:
            # Convert the year to century
            century = (year - 1) // 100 + 1
            return century
    else:
        # If the input year is not within the range, return an error message
        return "Error: Year should be between 1 and 2024 (inclusive)."


# Test with specific years
years_to_test = [1600, 1750, 1899, 2000, 2025]

for year in years_to_test:
    century_result = year_to_century(year)
    print(f"The year {year} belongs to the {century_result}th century.")


####################################################


def print_info(age, name, *last_names, shoe_size=42):
    # Print type, length, and float representation of age
    print("Type of age:", type(age))
    print("Length of name:", len(name))
    print("Float representation of age:", float(age))

    # Print last names
    print("Last names:", last_names)

    # Print default shoe size
    print("Shoe size:", shoe_size)


# Test the function
age = 25
name = "John"
last_name1 = "Doe"
last_name2 = "Johnson"
shoe_size = 45

print_info(age, name, last_name1, last_name2, shoe_size=shoe_size)
