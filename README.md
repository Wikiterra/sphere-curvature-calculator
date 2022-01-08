# Earth curvature calculator
To calculate the curvature of the Earth, there are various methods

## 1. Pitagoras Theorem
```python
# Pitagoras with two heights

from numpy import*

# Data: R, h_0, h_1, d_0, d_1
## R: Earth radius (6371 Km)
## h_0: eye height at sea level (in Km)
## d_0: distance in straight line from the observer to the object (in Km)
## h_1: hidden height by curvature (in Km)
## d_1: distance to the geometrical horizon (in Km)
## d_2 = d_0 - d1; d_2: distancia from the geometrical horizon to the object (in Km)
## h_R: height along the distance. Example: if the observer and object are separated at the shore of a lake at 200 m of altitude, the height is the same along all the distance and is not at sea level. (Default h_R = 0, sea level)

h_R = 0   # user data
R = 6371 + h_R 

h_0 = 0.001 # user data
d_0 = 30 # user data

# By Pitagoras: (R+h_0)^2=d_1^2+R^2 and (R+h_1)^2=d_2^2+R^2
d_1 = sqrt(h_0**2+(2*R*h_0))
h_1 = sqrt((d_0-d_1)**2+R**2)-R

print("The distance to the geometrical horizon is %.3f Km and the hidden height is %.3f Km" % (d_1, h_1))
```

[Desmos graph](https://www.desmos.com/calculator/cbdgduxedl)
## 2. Perimeter of a circle
## 3. Using trigonometry

# Spherical Earth model scheme
- Data:
	- α: angle variation
	- d: distance AB
	- h: observer's hidden DB height
	- R: radius of the spherical Earth (R=6371 Km)
- Points:
	- A: observer on the edge of the sphere
	- B: vertical prolongation of the object at D
	- C: center of the circle
	- D: base of the hidden object
<img src="https://raw.githubusercontent.com/Curiosity432/Earth-curvature-calculator/main/Trigonometry-sphere.png" width=50% height=50%>

Representation of the Earth with distances and heights.
![[Earth-curve-calc]](Earth-curve-calc.png)

