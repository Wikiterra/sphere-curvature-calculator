# Earth-curvature-calculator
Calculate the curvature of the Earth.

Representation of the Earth with distances and heights.
![[Earth-curve-calc]](Earth-curve-calc.png)


## Schematic of the spherical earth model
- Data:
	- $alpha$: angle variation
	- $d$: distance AB
	- h$: observer's hidden DB height
	- $R$: radius of the spherical Earth ($R=6371 Km=3959 miles$)
- Points:
	- A: observer on the edge of the sphere
	- B: vertical prolongation of the object at D
	- C: center of the circle
	- D: base of the hidden object

![](Trigonometry-sphere.png)

### 1. Pitagoras Theorem
- Teorema de Pitágoras: $$a²+b²=c² \Rightarrow c=\sqrt{a²+b²}$$
- Para este caso $a=d$, $b=R$, $c=R+h$
$$d^2+R^2=(R+h)^2 \Rightarrow d=\sqrt{(R+h)²-R²}=\sqrt{2Rh+h^2}$$
	- Para h=1 Km:
	$$d=\sqrt{(2 \cdot 6371 \cdot 1) + 1²}=112.885 Km$$
- Función matemática, la distancia d (eje Y) depende de la  la altura h (eje X): 
$$y=\sqrt{12742 x + x^2}$$

![](Grafica-curvatura.png)
[Gráfica en Desmos](https://www.desmos.com/calculator/cbdgduxedl)


## 2. Perimeter of a circle
- Perímetro de un círculo
$$C=2 \pi R$$
- Angle (in rad) per unit (kilometer):
$$\alpha_{Km}=\frac{\alpha_T}{C}=\frac{2 \pi}{2 \pi R} = \frac{1}{R}$$
- Angle per distance (d):
$$\alpha=\alpha_{Km} \cdot d$$
- Calc of height (h):
$$h = r \cdot (1 - cos(\alpha)) = r \cdot \left(1-cos\left(\frac{d}{R}\right)\right)$$
	- Example for d=113 Km:
$$ h = 6371 \cdot \left(1 - cos \left(\frac{113}{6371} \right)\right) = 1.002 Km$$

## 3. Using trigonometry
- Formules
$$sen^2(α)+cos^2(α)=1$$
$$cos(α)=\frac{R}{R+h} \approx \frac{R-h}{R}$$
$$sen(α)=\frac{d}{R+h}$$
$$tg(α)=\frac{d}{R}$$
1. Clearing
$$tg(α)=\frac{d}{R} \Rightarrow \alpha=arctg(\frac{d}{R})$$
$$cos(α)=\frac{R}{R+h} \Rightarrow h=R \cdot (sec(α)-1)$$
	Substituting for d=113 Km, hallar α y h:
	$$\alpha=arctg(\frac{113}{6371})$$
	$$h=6371 \cdot(\frac{1}{arctg(\frac{113}{6371})}-1)=1.187 Km$$
2. Cosin calculated subtracting the height
$$cos(\alpha)=\frac{R-h}{R} \Rightarrow h=R \cdot (1-cos(\alpha))$$
	Substituting for d=113 Km:
	$$h=6371 \cdot \left(1 - cos\left(arctg \left(\frac{113}{6371}\right)\right)\right)=1.001 Km$$
