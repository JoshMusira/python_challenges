# Write a function named capital_indexes. The function takes a single parameter,
# which is a string. Your function should return a list of all the indexes in the string
# that have capital letters.

# METHOD ONE
def capital_indexes(word):
  array = []
  for i in range(len(word)):
    if word[i].isupper():
      array.append(i)

  return array

input = "My Name Is Josh"
result = capital_indexes(input)

print(result)

# METHOD TWO

from string import uppercase
def capital_indexes(s):
    return [i for i in range(len(s)) if s[i] in uppercase]