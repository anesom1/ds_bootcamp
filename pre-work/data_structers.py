
################# STRINGS ##################################

#my_string = "Hello, World!"
print(my_string) # Output: "Hello, World!"

print(type(my_string)) # Output: <class 'str'>

my_string = "Hello, World!"
print(my_string[0]) # Output: "H"
print(my_string[7]) # Output: "W"
#------------------------------------------------------------------------


# Concatenating Strings

hello = "Hello"
world = "World"
print(hello + ", " + world + "!") # Output: "Hello, World!"
#------------------------------------------------------------------------


#String Slicing

my_string = "Hello, World!"
print(my_string[0:5]) # Output: "Hello"
print(my_string[7:]) # Output: "World!"
#------------------------------------------------------------------------

#Some String Methods
my_string = "Hello, World!"
print(my_string.lower()) # Output: "hello, world!"
print(my_string.upper()) # Output: "HELLO, WORLD!"
print(my_string.replace("H", "J")) # Output: "Jello, World!"
print(my_string.split(",")) # Output: ["Hello", " World!"]

#------------------------------------------------------------------------


#String formatting

name = "John"
age = 36
print("My name is " + name + ", and I am " + str(age) + " years old.") 
# Output: "My name is John, and I am 36 years old."


print("My name is {}, and I am {} years old.".format(name, age)) 
# Output: "My name is John, and I am 36 years old."

print(f"My name is {name}, and I am {age} years old.") 
# Output: "My name is John, and I am 36 years old."
# The above example demonstrates how to use f-strings to insert variables into
# a string. An f-string is a string literal prefixed with the letter f. The curly braces
# {} are placeholders replaced with the values of the variables passed to the
# f-string.

#------------------------------------------------------------------------------------------------------


#String escape sequences

print("Hello, World!") # Output: "Hello, World!"
print("Hello, \"World!\"") # Output: "Hello, "World!""
print("Hello, \'World!\'") # Output: "Hello, 'World!'"
print("Hello, \tWorld!") # Output: "Hello, World!"
print("Hello, \nWorld!")
# Output: "Hello,
# World!"

'''
The above example demonstrates how to use escape sequences to insert
special characters into a string. The backslash \ escapes the special character
that follows it. The escape sequence \" inserts a double quote into the string.
The escape sequence \' inserts a single quote into the string. The escape
sequence \t inserts a tab into the string. The escape sequence \n inserts a
new line into the string.
'''
#------------------------------------------------------------------------------------------------------

#String length

my_string = "Hello, World!"
print(len(my_string)) # Output: 13
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------


################# LISTS ##################################

# Modifying Individual Items in a List

my_list = ["apple", "banana", "cherry"]
my_list[1] = "kiwi"
print(my_list) # Output: ["apple", "kiwi", "cherry"]
#------------------------------------------------------------------------------------------------------


# Adding Items to a List

my_list = ["apple", "banana", "cherry"]
my_list.append("orange")
print(my_list) # Output: ["apple", "banana", "cherry", "orange"]

# The above example demonstrates how to add an item to the end of a list
# using the append() method.

#------------------------------------------------------------------------------------------------------

#Remove Item by Index

my_list = ["apple", "banana", "cherry"]
my_list.pop(1)
print(my_list) # Output: ["apple", "cherry"]



#------------------------------------------------------------------------------------------------------

# Remove Item by Value

my_list = ["apple", "banana", "cherry"]

my_list.remove("banana")
print(my_list) # Output: ["apple", "cherry"]



#------------------------------------------------------------------------------------------------------
# Slicing Lists

my_list = ["apple", "banana", "cherry", "orange", "kiwi",
"melon", "mango"]
print(my_list[2:5]) # Output: ["cherry", "orange", "kiwi"]

#------------------------------------------------------------------------------------------------------
#Checking if an Item Exists in a List

my_list = ["apple", "banana", "cherry"]
if "apple" in my_list:

    print("Yes, 'apple' is in the fruits list") 
# Output: "Yes,'apple' is in the fruits list"

#------------------------------------------------------------------------------------------------------
#Finding the Length of a List

my_list = ["apple", "banana", "cherry"]
print(len(my_list)) # Output: 3

#------------------------------------------------------------------------------------------------------
#Looping Through a List

my_list = ["apple", "banana", "cherry"]
for item in my_list:
    print(item) # Output: "apple", "banana", "cherry"

#------------------------------------------------------------------------------------------------------


################# TUPLES ##################################














################# SETS ##################################

#------------------------------------------------------------------------------------------------------
# 