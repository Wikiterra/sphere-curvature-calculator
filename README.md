# Earth curvature calculator
To calculate the curvature of the Earth, there are various methods

## 1. Pitagoras Theorem
```python
# Pitágoras con dos alturas

from numpy import*

# Datos: R, h_0, h_1, d_0, d_1
## R: radio terrestre
## h_0: altura del observador
## d_0: distancia al objeto
## h_1: Ocultación del objeto observado
## d_1: Distancia al corte por curvatura
## d_2 = d_0 - d1; d_2: distancia del corte por curvatura la objeto

R = 6.4*10**3  # Radio de la Tierra en Km
h_0 = 0.001  # Altura del observador en Km
d_0 = 30 # Distancia total en Km

# Por Pitágoras: (R+h_0)^2=d_1^2+R^2 y (R+h_1)^2=d_2^2+R^2

d_1 = sqrt(h_0**2+(2*R*h_0))
h_1 = sqrt((d_0-d_1)**2+R**2)-R

print("La distancia al corte por curvatura es de %.3f Km y la altura ocultada es %.3f Km" % (d_1, h_1))
```

[Desmos graph](https://www.desmos.com/calculator/cbdgduxedl)
## 2. Perimeter of a circle
## 3. Using trigonometry

# Spherical Earth model scheme
- Data:
	- α: angle variation
	- d: distance AB
	- h: observer's hidden DB height
	- R: radius of the spherical Earth (R=6371 Km=3959 mi)
- Points:
	- A: observer on the edge of the sphere
	- B: vertical prolongation of the object at D
	- C: center of the circle
	- D: base of the hidden object
<img src="https://raw.githubusercontent.com/Curiosity432/Earth-curvature-calculator/main/Trigonometry-sphere.png" width=50% height=50%>

Representation of the Earth with distances and heights.
![[Earth-curve-calc]](Earth-curve-calc.png)

