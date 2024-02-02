# Pythagorean theorem with observer height, input (d, h0, R) & output (h1)

from numpy import*

# Data: R, h0, h1, d, d1 with same unit (e.g. Km)
## hR: elevated area along all the distance. Example: if the observer and object are separated at the shore of a lake at 200 m of altitude, 
       ## the height is the same along all the distance and is not at sea level, so would be hR = 0.2 Km. (Default hR = 0, sea level)

# User data in same unit (Km)
d = 30
h0 = 0.01 #  h0 = 0.01 Km = 10 m
hR = 0
R = 6371 + hR

# Pythagorean theorem: 
# d2 = d_0 - d1, (R+h0)^2=d1^2+R^2 and (R+h1)^2=d2^2+R^2
d1 = sqrt(h0**2+(2*R*h0))
h1 = sqrt((d-d1)**2+R**2)-R

print("The distance to the geometrical horizon is %.3f Km and the hidden height is %.3f Km" % (d1, h1))