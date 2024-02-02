# Angle of curvature of a given perimeter, at sea level.

from numpy import*

## Input data (same units, e.g. Km)
R = 6371
C = 2*pi*R # C=12742*pi=40030.14 Km
d = 30

# Angle (in degrees) per unit, convert python defaults radians to degrees
alfa_km = 2*pi/C

# Angle for given distance (d):
alfa = alfa_km*d

# Calculus of the hidden height h1:
h1 = R*(1-cos(alfa))

print("At a distance of %.2f km at sea level the hidden height by curvature is %.2f km." % (d, h1))