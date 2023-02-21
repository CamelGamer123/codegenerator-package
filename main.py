# This module is used to create all the combinations.
import itertools
import string
# perf_counter is used to time the program's execution
from time import perf_counter

startTime = perf_counter()

# This is the password you are trying to guess.
password = "5613"

# This is the list of all the possible digits in the combination
stuff = list(string.digits)

# This is the length of the password you are trying to guess
L = 4

# This creates a list of all possible combinations of 'stuff' that are 'l' long.
tupleCombinations = list(itertools.combinations_with_replacement(stuff, L))

# This creates an empty list for the string versions of 'tupleCombinations'
combinations = []

# This loops through every single item in 'tupleCombinations' and converts each item to a string, this is needed as the
# password that we are trying to guess is a string and comparing two different types of variable is impossible.
for li in tupleCombinations:
    temp = ""
    for item in li:
        temp += str(item)
    combinations.append(temp)

with open("file.txt", "w") as f:
    f.write("")
    f.write(str(combinations))
# This searches through the list of combinations and checks if the password is the current item in the list.
for counter, item in enumerate(combinations):
    if item == password:  # This is the actual check to see if the item is what you are searching for.
        endTime = perf_counter()
        exit(f"Password found: {item} in {counter} tries ({endTime-startTime} seconds)")

exit("Password not found.")
