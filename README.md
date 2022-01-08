# Earth-curvature-calculator
Calculate the curvature of the Earth.

Representation of the Earth with distances and heights.
![[Earth-curve-calc]](Earth-curve-calc.png)


## Schematic of the spherical earth model
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

### 1. Pitagoras Theorem
- Teorema de Pitágoras: ![img](http://www.sciweavers.org/tex2img.php?eq=a²+b²=c²\Rightarrowc=\sqrt{a²+b²}&bc=White&fc=Black&im=jpg&fs=12)
- Para este caso a=d, b=R, c=R+h
  ![img](http://www.sciweavers.org/tex2img.php?eq=d^2+R^2=(R+h)^2 \Rightarrow d=\sqrt{(R+h)²-R²}=\sqrt{2Rh+h^2}&bc=White&fc=Black&im=jpg&fs=12)
	- Para h=1 Km:
	![img](http://www.sciweavers.org/tex2img.php?eq=d=\sqrt{(2 \cdot 6371 \cdot 1) + 1²}=112.885 Km&bc=White&fc=Black&im=jpg&fs=12)
- Función matemática, la distancia d (eje Y) depende de la  la altura h (eje X): 
<img src="https://render.githubusercontent.com/render/math?math=y=\sqrt{12742 x + x^2}"> ![img](http://www.sciweavers.org/tex2img.php?eq= &bc=White&fc=Black&im=jpg&fs=12)

![](Grafica-curvatura.png)
[Gráfica en Desmos](https://www.desmos.com/calculator/cbdgduxedl)

## 2. Perimeter of a circle
- Perímetro de un círculo
$$C=2 \pi R$$ ![img](http://www.sciweavers.org/tex2img.php?eq= &bc=White&fc=Black&im=jpg&fs=12)
- Angle (in rad) per unit (kilometer):
$$\alpha_{Km}=\frac{\alpha_T}{C}=\frac{2 \pi}{2 \pi R} = \frac{1}{R}$$ ![img](http://www.sciweavers.org/tex2img.php?eq= &bc=White&fc=Black&im=jpg&fs=12)
- Angle per distance (d):
$$\alpha=\alpha_{Km} \cdot d$$ ![img](http://www.sciweavers.org/tex2img.php?eq= &bc=White&fc=Black&im=jpg&fs=12)
- Calc of height (h):
$$h = r \cdot (1 - cos(\alpha)) = r \cdot \left(1-cos\left(\frac{d}{R}\right)\right)$$ ![img](http://www.sciweavers.org/tex2img.php?eq= &bc=White&fc=Black&im=jpg&fs=12)
	- Example for d=113 Km:
$$ h = 6371 \cdot \left(1 - cos \left(\frac{113}{6371} \right)\right) = 1.002 Km$$ ![img](http://www.sciweavers.org/tex2img.php?eq= &bc=White&fc=Black&im=jpg&fs=12)

## 3. Using trigonometry
- Formules
![img](http://www.sciweavers.org/tex2img.php?eq=sin^2(\alpha)+cos^2(α)=1&bc=White&fc=Black&im=jpg&fs=12)
![img](http://www.sciweavers.org/tex2img.php?eq=cos(α)=\frac{R}{R+h} \approx \frac{R-h}{R}&bc=White&fc=Black&im=jpg&fs=12)
![img](http://www.sciweavers.org/tex2img.php?eq=sin(α)=\frac{d}{R+h}&bc=White&fc=Black&im=jpg&fs=12)
![img](http://www.sciweavers.org/tex2img.php?eq=tg(α)=\frac{d}{R}&bc=White&fc=Black&im=jpg&fs=12)

1. Clearing
$$tg(α)=\frac{d}{R} \Rightarrow \alpha=arctg(\frac{d}{R})$$
$$cos(α)=\frac{R}{R+h} \Rightarrow h=R \cdot (sec(α)-1)$$
	Substituting for d=113 Km, hallar α y h:
	$$\alpha=arctg(\frac{113}{6371})$$ ![img](http://www.sciweavers.org/tex2img.php?eq= &bc=White&fc=Black&im=jpg&fs=12)
	$$h=6371 \cdot(\frac{1}{arctg(\frac{113}{6371})}-1)=1.187 Km$$ ![img](http://www.sciweavers.org/tex2img.php?eq= &bc=White&fc=Black&im=jpg&fs=12)
2. Cosin calculated subtracting the height
$$cos(\alpha)=\frac{R-h}{R} \Rightarrow h=R \cdot (1-cos(\alpha))$$
	Substituting for d=113 Km:
	$$h=6371 \cdot \left(1 - cos\left(arctg \left(\frac{113}{6371}\right)\right)\right)=1.001 Km$$ ![img](http://www.sciweavers.org/tex2img.php?eq= &bc=White&fc=Black&im=jpg&fs=12)
	
	
	
	
![img](http://www.sciweavers.org/tex2img.php?eq= &bc=White&fc=Black&im=jpg&fs=12)

<img src="https://render.githubusercontent.com/render/math?math=sen^2(α)+cos^2(α)=1">
![img](http://www.sciweavers.org/tex2img.php?eq=1%2Bsin%28mc%5E2%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=)
![img](http://latex.codecogs.com/svg.latex?%5Cfrac%7B%5Csigma%7D%7B%5Cmu%7D)

