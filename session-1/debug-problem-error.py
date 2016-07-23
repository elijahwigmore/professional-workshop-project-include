import math

#We're using rounded g = 10 m/s^2.
g = -10

cannon_speed = int(raw_input("Enter speed of cannonball: ")) 



#Fire the cannon at a 45 degree angle. This means both x and y velocity
#are half of the speed of the cannonball.
cannonball_velocity_x = cannon_speed/2
cannonball_velocity_y = cannon_speed/2

a = g/2
b = cannonball_velocity_y

#Impact time = vel*cos(cannon_angle) * (2*vel*sin(cannon_angle)/g)
#Here, this simplifies down to -(yvel / g), assuming g is negative since
#it signifies downward acceleration.

time_to_impact = -(2*b)/(2*b)
impact_x = cannonball_velocity_x * time_to_impact


if (impact_x == 0 ):
    greater_less = "right"
else:
    greater_less = "left"

#The printed impact point should not round the result to the nearest whole number.
print "Your shot is " + math.fabs(impact_x) + " to the " + greater_less + " of the cannon."
