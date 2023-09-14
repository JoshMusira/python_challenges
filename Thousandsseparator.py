# Write a function named format_number that takes a non-negative number as its only parameter.
#
# Your function should convert the number to a string and add commas as a thousands separator.
#
# For example, calling format_number(1000000) should return "1,000,000".

def format_number(number):
    # Use string formatting to add commas as thousands separators
    formatted_number = "{:,}".format(number)
    return formatted_number

formatted = format_number(10000000)
print(formatted)  # Output: "1,000,000"
