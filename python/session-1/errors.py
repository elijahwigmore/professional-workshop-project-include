import math

# Given a right angle triangle, with the length of hypotenuse, and the value of one angle,
# find the lengths of the other sides.

deg_to_rad_const = math.pi/180

hypotenuse = 42

top_angle = 40*deg_to_rad_const

#side 1 is the vertical side
side_1 = math.cos(top_angle)*hypotenuse
side_2 = math.sin(top_angle)*hypotenuse

print ("The vertical side has length " + str(side_1) + " and the base has length " + str(side_2))

