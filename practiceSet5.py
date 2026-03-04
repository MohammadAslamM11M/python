# Write a program to create a dictionary of Hindi words with values as their English translation.
# Provide user with an option to look it up!

# hindi_words = {
#     "aao": "come",
#     "jao": "go",
# }

# word = input("Enter the word you want meaning of: ")

# print(hindi_words.get(word))

# ----------------------------------------

# Write a program to input eight numbers from the user and display all the unique numbers (once).

# numbers = set()

# for i in range(8):
#     user_nums = int(input("Enter eight numbers"))
#     numbers.add(user_nums)

# print(numbers)

# ----------------------------------------

# Can we have a set with 18(int) and "18" (str) as a value in it ?

# s = set()
# s = {18, "18"}

# print(s)            # yes we can

# ----------------------------------------

# What will be the length of following set s:

# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20')

# print(len(s))     # We assume that answer is 3, but python sees it as 20 == 20.0 -> true, Hence answer is 2

# ----------------------------------------

# s = {} What is the type of s ?

# s = {}
# print(type(s))

# ----------------------------------------

# Create an empty dictionary. Allow 4 friends to enter their favorite languages as value and use key as their names.
# Assume that the names are unique.

language_details = {}

for i in range(4):
    add_name = input("Enter your name: ")
    add_language = input("Enter your language: ")

    language_details.update({add_name: add_language})

print(language_details)

# ----------------------------------------

# If the names of 2 friends are same; what will happen to the program above ?

# name and language associated to that friend is updated, since we used update() method

# ----------------------------------------

# If the languages of 2 friends are same; what will happen to the program above ?

# name and language associated to that friend is included, same values are allowed

# ----------------------------------------

# Can you change the values inside a list which is contained in set S ?

s = {8, 7, 12, "Harry", [1,2]}
# answer is no...
# a list cannot be included in a set
# a set requires all its elements to be immutable and hashable