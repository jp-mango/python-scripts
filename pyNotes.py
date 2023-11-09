#! Strings - act a lot like lists with modification

print("--Strings:--\n")
# An f-string allows you to embed expressions inside string literals by wrapping them in curly braces {}.
# print(f"Hello {name}, your favorite color is {color}")
first_name = "Justin"
last_name = "Menzies"

# [x] will select the first letter in a string.
print(first_name[0])

# selects the last letter in a string.
print(last_name[-1])

# prints certain characters in a string.
print(first_name[1:3])  # second to, but not including, fourth
print(first_name[::-1])  # backwards

# len() prints the length of a string.
print(len(first_name))

# .upper() changes string to uppercase.
print(first_name.upper())

# .lower() changes string to lowercase.
print(first_name.lower())

# .find() returns index of first occurrence of a character in a string. will return a -1 if not found.
print(first_name.find("n"))

# .replace() replaces the first occurrence of a character in a string. first value will be the character to be replaced.
# second value will be the replacement. Can replace multiple characters at once.
print(first_name.replace("n", "N"))

# "in" is a boolean expression to check if a character or word is in a string. case sensitive.
print("j" in first_name)

# .join() can be used to print the elements of a list as a string
word = ["b", "a", "c", "k", "w", "a", "r", "d", "s"]
rev_word = "".join(reversed(word))
print(rev_word)

# .strip() is used to get rid of extra spaces before and after the phrase
word = "    Hello     "
no_space_word = word.strip()
print(no_space_word)

# .split() will break a phrase up into a list. Each word being its on value within the list
phrase = "this is a sentence"
print(phrase.split())

# .title() will uppercase every beginning letter in a phrase
movie = "spider man into the spiderverse"
print(movie.title())

print("\n")
#! Lists/ Tuples
print("--Lists:--\n")
list_example = [1, 2, 3, 4, 4, 4]
print(list_example)
# Get the data type of the element at the specified index
data_type = type(list_example[0]).__name__
print(data_type)

# set() will remove ALL duplicates from a list
list_example = list(set(list_example))
print(list_example)

# use .append() to add a new item to a list.
list_example.append(1)
print(list_example)

# use.extend() to add multiple items to a list.
list_example.extend([2, 3, 4])
print(list_example)

# use.insert() to insert a new item into a list. first value will be the
# index where the new item will be inserted. second value will be the new item.
list_example.insert(0, 5)
print(list_example)

# use.remove() to remove an item from a list. need a loop to remove every instance
list_example.remove(5)
print(list_example)

# can reverse a list with use of .reverse()
count = [1, 2, 3, 4, 5]
count.reverse()
print(count)

# use[-1] to get the last item in a list.
print(list_example[-1])

# replace a certain item in a list.
list_example[0] = 7
print(list_example)

# list method to count the number of occurrences of an item in a list. will return 0 if not found.
print(list_example.count(7))

# list method to remove an element from a specific index or from the end of a list.
print(list_example.pop())
print(list_example)

# used to create a sequence of numbers from 2-10. Can change the increment with a third input
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# an easy way to find common elements in 2 lists is to use intersection()
list2 = [4, 5, 6]
common_elements = list(set(list_example).intersection(set(list2)))
print(f"{common_elements} is in both lists")  # will return 4 because 4 is in both lists

# built in function use to sort a list.
unsorted_list = [2, 1, 4, 3]
sorted_list = sorted(unsorted_list)  # can also use unsorted_list.sort()
backwards_sorted_list = sorted(
    unsorted_list, reverse=True
)  # can also use unsorted_list.sort(reverse=True). This will sort the list in reverse order.
print(sorted_list)

# slicing lists is done separating the beginning and end of the desired portion with a colon.
print(list_example)
print(list_example[1:3])
print(
    list_example[:3]
)  # An empty first spot selects everything before. If nothing is placed after the colon, the whole list is returned.

# tuples are a semi-permanent list. Cannot change the ordering or add and remove elements.
# Generally used to store data that is not similar, but to keep it grouped
my_tuple = ("Justin", 25, "Electrician")
print(my_tuple)
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:3])


# combining and sorting 2 lists.
def combine_sort(my_list1, my_list2):
    combined_list = my_list1 + my_list2
    new_list = sorted(combined_list)
    return new_list


print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

# can combine lists using the zip() function. Will return a list of tuples.
names = ["Jenny", "Alexis", "Sam", "Grace"]
heights = [61, 70, 67, 64]
zipped_list = zip(names, heights)
converted_list = list(zipped_list)
print(list(converted_list))
print("\n")

#! Loops
#! For
print("--For Loops:--\n")

# printing a list with a for loop
for i in range(5):
    print(i, end="")
print()

# Looping over a list of numbers and printing each element:
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# Looping over a string and printing each character:
string = "Hello, world!"
for char in string:
    print(char)

# Looping over a range of numbers and printing each value:
for i in range(len(numbers) + 1):
    print((f"% ") * i)

# Looping over a list of tuples and unpacking the values:
fruits = [("apple", 0.5), ("banana", 0.3), ("orange", 0.7)]
for fruit, price in fruits:
    print(f"{fruit}: ${price:.2f}")

# looping through a dictionary
# Create a dictionary
person = {"name": "John", "age": 30, "gender": "Male"}
for key in person:  # Loop through the keys in the dictionary
    print(key)
for value in person.values():  # Loop through the values in the dictionary
    print(value)
for key, value in person.items():  # Loop through the key-value pairs in the dictionary
    print(f"{key}: {value}")

print("\n")

#! While

print("--While Loops:--\n")
# Counting from 1 to 10 using a while loop:
i = 1
while i <= 10:
    print(i)
    i += 1

# Repeatedly prompting the user for input until a valid response is entered:
# commented out because i dont want it to interfere with execute
# ? while True:
# ?     try:
# ?         num = int(input("Please enter a valid integer: "))
# ?         break
# ?     except ValueError:
# ?         print("Invalid input. Please try again.")

# Looping over a list and removing elements until a certain condition is met:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while len(numbers) > 5:
    numbers.pop()
print(numbers)

# Repeatedly flipping a coin until it comes up heads:
import random

flip = "tails"
while flip == "tails":
    flip = random.choice(["heads", "tails"])
    print(flip)
print("\n")

#! Functions
print("--Functions:--\n")


# Positional arguments - In this example, the greet function takes two positional arguments: name and age.
# When we call the function on the last line, we pass in the values for these arguments in the order
# they appear in the function definition. The output will be "Hello, Alice! You are 25 years old."
def pos_greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")


pos_greet("Justin", 25)


# Keyword arguments - we are calling the same greet function as before, but this time we are passing
# in the arguments as keyword arguments. That is, we are explicitly specifying which argument corresponds
# to which parameter using the parameter names. The output will be the same as before:
# "Hello, Alice! You are 25 years old."
def key_greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")


key_greet(age=25, name="Justin")


# Default arguments - In this example, we have modified the greet function to give a default value of
# 30 for the age parameter. When we call the function with just a name argument, it will use the default
# value for age. When we call the function with both a name and an age argument, it will use the specified
# value for age. The first call to greet will output "Hello, Alice! You are 30 years old." and the second
# call will output "Hello, Bob! You are 25 years old."
def greet(name, age=30):
    print(f"Hello, {name}! You are {age} years old.")


greet("Bob")  # Uses the default value for age (30)
greet("Justin", 25)  # Uses the specified value for age (25)
print("\n")
#! Modules
print("--Modules:--\n")
# provides access to mathematical functions and constants.
import math

print(math.sqrt(16))
print(math.sin(math.pi / 2))
print(math.cos(math.pi / 3))
print(math.pi)

import random

print(random.random())
print(random.randint(1, 10))
print(random.choice(["apple", "banana", "cherry"]))

import datetime

today = datetime.date.today()
print(today)
now = datetime.datetime.now()
print(now)
one_hour = datetime.timedelta(hours=1)
next_hour = now + one_hour
print(next_hour)
print("\n")

#! Dictionaries - A dictionary is defined using curly braces {} and a comma-separated list of key-value pairs in the form key: value.
print("--Dictionaries:--\n")

# creates a dictionary of fruits and prices
my_dict = {"apple": 1.5, "banana": 0.5, "cherry": 2.0}
print(my_dict)

# access the value of a key in a dictionary
print(my_dict["apple"])  # Output: 1.5

# Modify the value associated with the key 'banana'
my_dict["banana"] = 0.75
print(my_dict["banana"])  # Output: 0.75

# Add a new key-value pair for 'orange' to the end of the dictionary
my_dict["orange"] = 1.25
print(my_dict)

# to remove a key-value pair use "del"
del my_dict["apple"]

# prints all keys in the dictionary
print(my_dict.keys())

# prints all values in the dictionary
print(my_dict.values())

# can also use the get() function to access a key-value pair in a dictionary
banana_price = my_dict.get("banana")
print(banana_price)
print("\n")

#! Files
print("--Files:--\n")

# Open file for reading, will error if the file doesn't exist
with open("file.txt", "r") as file:
    # Read the entire file
    contents = file.read()
    # Print the file contents
    print(contents)

# Overwrites the file 'file.txt' in the current directory. If no file with that name exists, it will create it
with open("file.txt", "w") as f:
    f.write("Now the file says this")
# read the file contents
with open("file.txt", "r") as file:
    # Read the entire file
    contents = file.read()
    # Print the file contents
    print(contents)

# Open file for appending
with open("file.txt", "a") as f:
    # Append some text to the file
    f.write("\nThis is some additional text.")
    # read the file contents
with open("file.txt", "r") as file:
    # Read the entire file
    contents = file.read()
    # Print the file contents
    print(contents)

# reading a file line by line
# Open file for reading
with open("file.txt", "r") as file:
    # Read the file line by line
    for line in file:
        # Print each line
        print(line)

# If with statement not used, file must be manually closed like this:
# Open file for reading
file = open("file.txt", "r")
# Read the file
contents = file.read()
# Print the file contents
print(contents)
# Close the file
file.close()

# csvs are very similar to files, but you have to import the csv module
import csv

with open("data1.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # this skips the header row
    for row in reader:
        name, age, gender = row
        print(f"{name} is a{age} year old{gender}")

print("\n")
#! Sets
print("--Sets:--\n")

# Creating a set
fruits = {"apple", "banana", "cherry"}
print(fruits)

# Adding an element to the set
fruits.add("orange")
print(fruits)

# Removing an element from the set
fruits.remove("banana")
print(fruits)

# Checking if an element is in the set
print("apple" in fruits)

# Set operations: union, intersection, difference
other_fruits = {"grape", "apple", "kiwi"}
print(fruits.union(other_fruits))
print(fruits.intersection(other_fruits))
print(fruits.difference(other_fruits))

print("\n")
#! Conditionals
print("--Conditionals:--\n")

x = 10
y = 20

if x < y:
    print("x is less than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is greater than y")

# Using logical operators: and, or, not
if x < 15 and y > 15:
    print("Both conditions are true")

# Inline if-else
message = "x is less than y" if x < y else "x is greater or equal to y"
print(message)

print("\n")
#! Exceptions
print("--Exceptions:--\n")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("Division successful!")
finally:
    print("This block always executes")

print("\n")
#! Classes and Objects
print("--Classes and Objects:--\n")


class Dog:
    # Class variable
    species = "Canis familiaris"

    # Initializer
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


# Creating objects of the Dog class
mikey = Dog("Mikey", 6)
print(mikey.description())
print(mikey.speak("Gruff gruff"))

print("\n")
#! Lambda Functions
print("--Lambda Functions:--\n")


# Regular function
def add(x, y):
    return x + y


# Lambda function
add_lambda = lambda x, y: x + y

print(add(5, 3))
print(add_lambda(5, 3))

print("\n")
#! List Comprehensions
print("--List Comprehensions:--\n")

numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)

# With condition
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(even_squares)

print("\n")

#! Match Case
print("--Match Case (Python 3.10+):--\n")

# Simple example
x = "a"

match x:
    case "a":
        print("Matched a")
    case "b":
        print("Matched b")
    case _:
        print("No match")

# Using patterns with match case
point = (1, 2)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y-axis, y = {y}")
    case (x, 0):
        print(f"X-axis, x = {x}")
    case (x, y):
        print(f"Point is at ({x}, {y})")
    case _:
        print("Not a point")

# Matching on data types
value = "Hello"

match value:
    case int():
        print("It's an integer!")
    case str():
        print("It's a string!")
    case list():
        print("It's a list!")
    case _:
        print("Unknown type")


# Matching on instance variables of classes
class Point:
    x: int
    y: int


p = Point()
p.x = 2
p.y = 3

match p:
    case Point(x=0, y=y):
        print(f"Point is on Y-axis at {y}")
    case Point(x=x, y=0):
        print(f"Point is on X-axis at {x}")
    case Point():
        print("Point is somewhere else on the plane")
    case _:
        print("Not a point")

# Using OR patterns in match
day = "Monday"

match day:
    case "Monday" | "Tuesday" | "Wednesday":
        print("It's one of the first three weekdays")
    case _:
        print("It's some other day")
