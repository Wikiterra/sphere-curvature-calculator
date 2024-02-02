# Trigonometry at sea level

from numpy import*

# Data: R, h1 (same units, e.g. Km)
R = 6371
h1 = array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]) # Target hidden height

# Target distance : d
d = R*arccos(R/(R+h1))

# Print the result
for i in range(len(h1)):
  print("The hidden height is %.1f Km for a distance of %.2f Km" % ((h1[i], d[i])))