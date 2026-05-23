#
#numbers = [1, 2]
#items = ["John", "Sam", "tt"]
#for x in numbers:
#     for y in items:
#          print(x, y)


numbers = [1, 2]
for i in numbers:
    print(i)

for l in 'John':
     if l == 'o':
          pass
     print(l, end=", ")



# Function to print a string
def printstring(str):
    print(str)
    return

printstring("Hello World")
printstring("Hello World 2")


# Function with multiple arguments
def greet(name, message):
    print(f"{message}, {name}!")
    
# Calling the function
greet(message="Hello", name="Alice")