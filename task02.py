# Write a function named mid that takes a string as its parameter. Your function should extract and return
# the middle letter. If there is no middle letter, your function should return the empty string.


def mid(word):
  length = len(word)
  if length % 2 == 0:
    return ""
  else:
    return word[length // 2]

word = "Joshua"
letter = mid(word)

print(letter)
