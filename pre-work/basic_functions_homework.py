'''
Write a Python function that checks whether a passed string is palindrome or not. A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
Write a Python function that takes a number as a parameter and checks if the number is prime or not. A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.
Write a Python function to check whether a number is in a given range.
Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
Write a Python program to reverse a string.
Write a Python function to sum all the numbers in a list.
Write a Python function to find the Max of three numbers.
'''

# Function that checks whether a passed string is palindrome or not.

def is_palindrome(a):
        b = a.replace(" ", "").lower()
        result = b == b[::-1]
        if result:
                print(a + " is a palindrome")
        else:
                print(a + " is not a palindrome")
    
is_palindrome('madam')
is_palindrome('nurses run')
is_palindrome('umbrella')

# Function that takes a number as a parameter and checks if the number is prime or not. A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself. 
def is_prime(i):

        if i > 1:
                for x in range(2, i):
                        if i % x == 0:
                                print (str(i) + " is not a prime")
                                return
                print(str(i) + " is a prime")
        else:
                print(str(i) + " is not a prime")
               

is_prime(13)
is_prime(4)
is_prime(3)
is_prime(6)

# Function to check whether a number is in a given range.
def is_inrange(i, a, b):
        for x in range(a,b):
                if x == i:
                        print (str(i) + " is in a given range")
                        return
                
        print (str(i) + " is not in a given range")

def is_inrangeshort(i, a, b):
        if i in range(a,b):
                print(str(i) + " is in a given range")
        else:
                print(str(i) + " is not in a given range")
        
                

is_inrange(3,10,20)
is_inrange(-3,10,20)
is_inrange(17,10,20)
is_inrange(20,10,20)
is_inrange(10,10,20)

is_inrangeshort(10,10,20)

# Function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def calc_factorial(i):
        x = 1
        for n in range(1,i + 1):
                x = x * n
        print("Factorial of " + str(i) + " is " + str(x))
 

calc_factorial(4)


# Program to reverse a string.
def reverse_string(str):
        rev = str[::-1]
        print(rev)

reverse_string('mama')
                
# Function to sum all the numbers in a list.

def sum_up(*num):
        x = 0
        for n in num:
                x += n
        print(x)
        return x

sum_up(1,2,3)


def sum_up2(*num):
        x = sum(num)
        print(x)
        return x        

sum_up2(2,3,4)

# Function to find the Max of three numbers.
def find_max(*arg):
        x = max(arg)
        print(x)
        return x

find_max(3,15,8)
