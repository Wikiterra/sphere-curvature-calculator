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
