# Define a function named all_equal that takes a list and checks whether all elements in the list are the same.
#
# For example, calling all_equal([1, 1, 1]) should return True.

def all_equal(lst):
    # Check if the list is empty; if it is, return True because there are no elements to compare.
    if not lst:
        return True

    # Compare all elements to the first element.
    first_element = lst[0]
    return all(element == first_element for element in lst)

result = all_equal([1, 1, 1])
print(result)  # Output: True

result = all_equal([1, 2, 1])
print(result)  # Output: False
