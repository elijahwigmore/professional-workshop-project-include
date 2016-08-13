# WEEK 1 LECTURE 2

#Single line comment. Anything after the pound sign is ignored.

print "Python will print this, but not anything after the pound" # like this.

'''
Block comment. Use triple single quotes or double quotes. Anything between the sets of 3 quotes will be ignored.
Like this line.
And this one.
'''

"""

Good idea to be consistent with quotes for same reason we want to be consistent with quotes in strings.
'''Maybe we want to use the other kind of quotes inside our block quote.
"""


print 1 + 1 # should equal 2

print 1 - 1 # should equal 0

print 4 * 2 # should equal 8

print 9 / 5 # will equal 1, even though 9 / 5 = 1.8

# If there's any float in division, we will perform float division, but if there's only ints, we will treat result as an
# int. This is important because sometimes if we perform division with ints, the actual answer could be a non-integer,
# but if we perform integer division the answer will be truncated.

# Note, for all arithmetic operations, any value being a float will make it a float operation returning a float.
# If all of the values involved are ints, we will perform an integer operation, returning an int.

print 9.0 / 5 # should equal 1.8

print 9 % 5, # 9 / 5 = 1 with a remainder of 4, will return 4


print 9.99 % 5.45



print int(5.999)

