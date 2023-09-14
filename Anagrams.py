# Two strings are anagrams if you can make one from the other by rearranging the letters.
#
# Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams,
# and False otherwise.
#
# For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.

def is_anagram(a,b):
    number1 = list(a.lower())
    number2 = list(b.lower())

    number1.sort()
    number2.sort()

    if number1 == number2:
        return True
    else:
        return False


result = is_anagram("Josh", "johs")

print(result)

