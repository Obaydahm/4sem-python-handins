import math

# 1. Create 5 list comprehensions to solve the following 5 problems:
print("1. Create 5 list comprehensions to solve the following 5 problems:")
# a. Iterate a list of names to return a list of the names starting with H
print("a. Iterate a list of names to return a list of the names starting with H")
names = ["Peter", "Michael", "Hans", "Hanne", "Hassan", "Jens"]
for name in names:
    if name.startswith("H"):
        print(name)

# b. In one line create a list of the numbers 1-100 to the power of 3
print("\nb. In one line create a list of the numbers 1-100 to the power of 3")
numbers = [x ** 3 for x in range(1, 101)]
print(numbers)

# c. Iterate a list of names to create a list of tuples where the tuples first value is the length of the name and the second is the name
print(
    "\nc. Iterate a list of names to create a list of tuples where the tuples first value is the length of the name and the second is the name"
)
names2 = [(len(name), name) for name in names]
print(names2)

# d. Iterate over each character in a string and get only those that are numeric
print(
    "\nd. Iterate over each character in a string and get only those that are numeric"
)
string = "hel1lo4br8o"
for char in string:
    if char.isdigit():
        print(char)

# e. Using only a list comprehension wrapped in set() get all possible combination from throwing 2 dice
print(
    "\ne. Using only a list comprehension wrapped in set() get all possible combination from throwing 2 dice"
)
dice = set([(x, y) for x in range(1, 7) for y in range(1, 7)])
print(dice)

########################################################################

# 2. Create 2 dictionary comprehensions to solve the following:
print("\n2. Create 2 dictionary comprehensions to solve the following:")

# a. Iterate a list of names and create a dictionary where key is the name and value is the length of the name
print(
    "\na. Iterate a list of names and create a dictionary where key is the name and value is the length of the name"
)
dict_names = {name: len(name) for name in names}
print(dict_names)

# b. Iterate a list of numbers and create a dictionary with (key, value) being (number, squareroot of number)
print(
    "\nIterate a list of numbers and create a dictionary with (key, value) being (number, squareroot of number)"
)
dict_numbers = {x: math.sqrt(x) for x in range(2, 11, 2)}
print(dict_numbers)

########################################################################

# 3. Progammatically using loops create a small program to produce a dictionary with all the 2 dice throw combinations as keys and their likelyhood in percent as values
print(
    "\n3. Progammatically using loops create a small program to produce a dictionary with all the 2 dice throw combinations as keys and their likelyhood in percent as values"
)

total_combinations = len(dice)
prc = float(100 / total_combinations)

total = {x: 0 for x in range(2, 13)}
print(total_combinations)

for combi in dice:
    total[combi[0] + combi[1]] += 1

for key, value in total.items():
    total[key] = "{:.2f}".format(prc * value)

print(total)
