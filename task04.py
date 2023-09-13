# Define a function, random_number, that takes no parameters. The function must generate a random integer
# between 1 and 100, both inclusive, and return it.
#
# Calling the function multiple times should (usually) return different numbers.
#
# For example, calling random_number() some times might first return 42, then 63, then 1

import random
# METHOD ONE
def random_number():
    return random.randint(1,100)

# METHOD TWO
def random_number():
    rand =  random.randrange(1,101)
    print(rand)

number = random_number()
number2 = random_number()
number3 = random_number()

print("A random number is ", number)
print("A random number is ", number2)
print("A random number is ", number3)