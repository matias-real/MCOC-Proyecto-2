# MCOC-Proyecto-2
Proyecto 2 Métodos computacionales para Obras Civiles

integrantes:
- Ceroni Gonzalez, Benjamijn Andres [https://github.com/Benjaceroni]
- Greve Velasco, Benjamin Andres [https://github.com/bagreve]
- Lorca Yañez, Felipe Ignacio [https://github.com/naxolorca]
- Real Santis, Matias Guillermo [https://github.com/matias-real]

## Descripción inicial del proyecto
La predicción del transporte de sedimentos está lejos de ser acertada porque no hay un profundo conocimiento sobre los procesos físicos que ocurren:
- Las predicciones sobre el transporte neto mediante simulaciones no son suficientes.
- Asumir que la velocidad de la partícula es igual a la velocidad del flujo no funciona con partículas que no son tan pequeñas (arenas, por ejemplo).
- Algunos procesos se descuidan (colisiones de partículas), turbulencia que se aumenta o disminuye, etc.

Una forma de predecir el transporte de sedimentos podría ser a través de una simulación numérica directa (resolver la ecuación de Navier-Stokes en cada cuadrícula de la celda) pero es muy caro y virtualmente imposible de hacer para miles o millones de partículas. Otra forma de predecir el transporte de sedimentos (la cual sería mejor opción) sería a modelar las fuerzas hidrodinámicas a partir de las grillas en que se conoce la velocidad. Esta forma es mucho más conveniente y es la que se tratará de modelar en este proyecto.

## Objetivos del proyecto
Implementar un modelo de simulación numérico para transporte de sedimentos de fondo. Comprender aspectos de desempeño de aplicaciones de computación científica tales como IO y complejidad algorítmica.

Para comenzar, primero se realizará la simulación del movimiento de una sola partícula en dos dimensiones. Esto con la finalidad de simplificar la situación.

Luego se implementará el código de manera que simule el movimiento para varias partículas, ya que en la realidad hay más de una partícula. En esta implementación al haber más de una partícula, no solo se producirán interacciones partícula-suelo, sino que también partícula-partícula. 

Una vez implementado el código para la simulación del movimiento de varias partículas, cada uno de los integrantes creará un repositorio aparte en el cual deberá subirá el código. En cada uno de los README.md, los integantes mencionarán las propiedades de su computador y correrán el código para un distinto número de partículas (todos deben hacerlo para las mismas cantidades), de manera de comparar el tiempo de funcionamiento del código en los distintos computadores.

## Links de los repositorios aparte de cada uno de los integrantes
- https://github.com/matias-real/MCOC-Proyecto-2-Entrega-4
- https://github.com/naxolorca/MCOC-Proyecto-2-Entrega-4
- https://github.com/bagreve/MCOC-Proyecto-2-Entrega-4
- https://github.com/Benjaceroni/MCOC-Proyecto-2


**Entrega 6 mejorada Felipe Lorca**
## Tiempo de simulación y Numero de particulas

	Simulaciones con dt de 0.00001 s y t max de 0.05 s

	Para la simulación  1:   3.01s  	N = 1
	Para la simulación  2:   7.34s  	N = 3
	Para la simulación  3:   20.09s 	N = 10
	Para la simulación  4:   30.29s 	N = 15
	Para la simulación  5:   39.3s 		N = 20
	Para la simulación  6:   60.53s 	N = 30
	Para la simulación  7:   91.71s 	N = 45
	Para la simulación  8:   161.23s 	N = 70
	Para la simulación  9:   257s 		N = 100
	Para la simulación 10:   334.62s 	N = 120
	Para la simulación 11:   433.89s 	N = 150

**Simulación 1**

![Grafico_1](https://raw.githubusercontent.com/matias-real/MCOC-Proyecto-2/master/Felipe_Lorca/grafico/1.png)

**Simulación 2**

![Grafico_2](https://raw.githubusercontent.com/matias-real/MCOC-Proyecto-2/master/Felipe_Lorca/grafico/3.png)

**Simulación 3**

![Grafico_3](https://raw.githubusercontent.com/matias-real/MCOC-Proyecto-2/master/Felipe_Lorca/grafico/10.png)

**Simulación 4**

![Grafico_4](https://raw.githubusercontent.com/matias-real/MCOC-Proyecto-2/master/Felipe_Lorca/grafico/15.png)

**Simulación 5**

![Grafico_5](https://raw.githubusercontent.com/matias-real/MCOC-Proyecto-2/master/Felipe_Lorca/grafico/20.png)

**Simulación 6**

![Grafico_6](https://raw.githubusercontent.com/matias-real/MCOC-Proyecto-2/master/Felipe_Lorca/grafico/30.png)

**Simulación 7**

![Grafico_7](https://raw.githubusercontent.com/matias-real/MCOC-Proyecto-2/master/Felipe_Lorca/grafico/45.png)

**Simulación 8**

![Grafico_8](https://raw.githubusercontent.com/matias-real/MCOC-Proyecto-2/master/Felipe_Lorca/grafico/70.png)

**Simulación 9**

![Grafico_9](https://raw.githubusercontent.com/matias-real/MCOC-Proyecto-2/master/Felipe_Lorca/grafico/100.png)

**Simulación 10**

![Grafico_10](https://raw.githubusercontent.com/matias-real/MCOC-Proyecto-2/master/Felipe_Lorca/grafico/120.png)

**Simulación 11**

![Grafico_11](https://raw.githubusercontent.com/matias-real/MCOC-Proyecto-2/master/Felipe_Lorca/grafico/150.png)

**Grafico N particulas vs Tiempo**

![Grafico_11](https://raw.githubusercontent.com/matias-real/MCOC-Proyecto-2/master/Felipe_Lorca/grafico.png)

## Discusión

	Utilizando este codigo podemos apreciar en el ultimo grafico, que el tiempo que se
	demora en ejecutar aumenta de forma lineal al aumentar la cantidad de particulas.
