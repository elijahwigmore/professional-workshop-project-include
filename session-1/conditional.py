'''
Project Include: Python Workshop
Lesson 3: Introduction to Conditional Statements and Boolean Logic
'''

# Conditions:

#   greater than: >
print(1 > 2) # False

#   less than: <
print(1 < 2) # True

#   greater than or equal to: >=
print(1 <= 2) # True

#   less than or equal to: <=
print(1 >= 2) # False

#   equal to: ==
print(1 == 1) # True

#   not equal to: !=
print(1 != 2) # False

# Keywords:
x = True
y = False

# AND: True if and only if x and y are True. False if and only if x and y are False.
print(x and y) # False

# OR: True if either x or y is True. False is both x and y are False
print(x or y) # True

# NOT: True if x is True and y is False. False otherwise.
print(x and not y)  #

# Declaring Boolean Variables: True or False
pick = False
flag = True

# Conditional Statements

# if (2 == 2):
#     print("test")
#
#     if (1 == 3):
#         print("test 2")

if(pick == True and flag == True):
    variable = 1
    print("Hi")

elif(flag == False and pick == False):
    variable = 2
    print("The flag was set so I am running here")

else:
    variable = 3
    print("The value of pick is False, So I am running here")

# Be careful with declaring variables with conditional statements!
# The issue lies within scoping. We declare variable three times, once within each conditional statement. Because of
# this, our program does not crash. If we remove variable from any one of the conditional statements, we risk running
# into an error

print(variable)
