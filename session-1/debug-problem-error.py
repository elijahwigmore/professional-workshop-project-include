import math

#We're using rounded g = 10 m/s^2.
g = -10

cannon_velocity = int(raw_input("Enter velocity of cannonball: ")) 



#Fire the cannon at a 45 degree angle.
cannonball_velocity_x = cannon_velocity/2
cannonball_velocity_y = cannon_velocity/2

a = g/2
b = cannonball_velocity_y

#Impact = vel*cos(cannon_angle) * (2*vel*sin(cannon_angle)/g)

time_to_impact = -(2*b)/(2*a)
impact_x = cannonball_velocity_x * time_to_impact


if (impact_x >= 0 ):
    greater_less = "right"
else:
    greater_less = "left"

#The printed impact point should not round the result to the nearest whole number.
print "Your shot is " + math.fabs(impact_x) + " to the " + greater_less + " of the cannon."
