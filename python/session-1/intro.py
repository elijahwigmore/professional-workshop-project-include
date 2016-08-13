'''
Project Include: Python Workshop
Lesson 1: Introduction to Programming in Python
'''

# Statement that prints the content within the quotations.
# note: single quotations can also be used.
print("Hello, world!")

# Printing an integer number
print(2)

# Similarly, printing a floating point (decimal) number
print(3.14159)

# Variables are very useful in Python in order to keep track of the work you are doing.
# Variable declaration works as follows:
number = 4

# You can also define a variable for a String too:
word = "star"

# The type() function is used to denote the type of the variable.
# In the case below, the result is <type 'int'>.
print(type(number))

# In python, a program can also keep track of inputs from the user.
# The raw_input() function allows the program to "break" and wait for the user to provide input through the console.
# Note: the text arguments inside the brackets is what the program will display to the user. This is optional, but is
#       in good practice in order to make your program user-friendly.
favoriteMusic = raw_input("Enter your favourite type of music: ")

# Using the result from the above statement, this is how you would use the print statement with a variable.
print("My favorite is " + favoriteMusic)

# Be careful about the variable types! The following line will not execute:
# Error: print("My favorite number is " + 17)
# The above error is "TypeError: cannot concatenate 'str' and 'int' objects"
# Whenever you combine two variables of different types, you must cast!
# The following line of code is an example of type casting an integer to a string
print("My favorite number is " + str(17))

# Likewise, you can type cast from a floating point number to a string
print("PI: " + str(3.14159))

# An example of nested type cast: Lets convert a float to an integer, and then to a string
print("I hate decimale numbers: " + str(int(3.14159)))

# Type casting gets the job done, but it does not actually change the variable type. Let me show you what I mean:
phi = 1.61803399

# Here we need to type cast the floating point number "phi" to a string
print("PHI: " + str(phi))

# But here we confirm that phi is indeed still of type float.
print(type(phi))



