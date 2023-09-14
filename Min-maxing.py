# Define a function named largest_difference that takes a list of numbers as its only parameter.
#
# Your function should compute and return the difference between the largest and smallest number in the list.
#
# For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.
#
# You may assume that no numbers are smaller or larger than -100 and 100.

def largest_difference(a):
   i = 0
   a.sort()
   length = len(a) - 1
   result = a[length] - a[0]

   print(result)


my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
largest_difference(my_list)