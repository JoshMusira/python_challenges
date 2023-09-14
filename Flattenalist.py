# Write a function that takes a list of lists and flattens it into a one-dimensional list.
#
# Name your function flatten. It should take a single parameter and return a list.
#code .

# For example, calling:
#
# flatten([[1, 2], [3, 4]])
# Should return the list:
#
# [1, 2, 3, 4]

def flatten(lst):
    # a = [1,2,3]
    # b = [4,5]
    # c = a + b
    # return  c
    return [item for sublist in lst for item in sublist]

# Example usage:
nested_list = [[1, 2], [3, 4]]
flattened_list = flatten(nested_list)
print(flattened_list)