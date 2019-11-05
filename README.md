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

# Entrega 6 mejorada #

Este código nace del programa anterior pero optimizado, con el fin de lograr que el timepo de funcionamiento aumente linealmente con el número de partículas a simular, a diferencia del código anterior que lo hacía de forma exponencial. Esto se logró a través de un cambio en el funcionamiento de la función de choque dentro del odeint, que es lo que más tardaba en el programa anterior. Es por esto que se separan las partículas que pueden chocar y las que no, de manera de acelerar el proceso ya que al no chocar el odeint se simplifica. Otra aspecto que se mejoró en esta entrega fue que los datos se guardaron en un archivo binario para luego leerlos y posteriormente graficarlos con un código aparte.

El programa tiene un paso de tiempo de 0.00001 segundos con un tiempo maximo de 0.05 segundos y se utilizaran los mismos archivos de posicionamiento del codigo anterior con 2, 5, 10 y 20 particulas.
También se tomo estos archivos con 1, 3, 10, 15, 20, 30, 45, 70, 100, 120 y 150 partículas.

## Entrega 6 mejorada Felipe Lorca
**Tiempo de simulación y Numero de particulas**

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

Se puede apreciar que con el código mejorado a medidad que se aumenta la cantidad de partículas, la velocidad con la que la simulación se ejecuta aumenta linealmente. Por lo que se alcanzó el objetivo de esta última entrega.

## Entrega 6 mejorada Benjamin Ceroni
**Tiempo de simulación y Numero de particulas**

	Simulaciones con dt de 0.00001 s y t max de 0.05 s

	Para la simulación  1:   5.3s	 	N = 1
	Para la simulación  2:   8.6s  		N = 3
	Para la simulación  3:   25.2s 		N = 10
	Para la simulación  4:   37.6s 		N = 15
	Para la simulación  5:   50.2s 		N = 20
	Para la simulación  6:   79.9s 		N = 30
	Para la simulación  7:   122.8s 	N = 45
	Para la simulación  8:   206.9s 	N = 70
	Para la simulación  9:   329.8s 	N = 100
	Para la simulación 10:   423.6s 	N = 120
	Para la simulación 11:   573.4s 	N = 150
	
**Tiempo simulación vs Numero de partículas**
![grafico](https://user-images.githubusercontent.com/53712580/68247994-b976fa80-fffa-11e9-9f6c-ef81fd55db80.png)

Como se logra observar una tendencia lineal al comparar el tiempo de simulacion en relación a la cantidad de partículas simuladas, se concluye que el objetivo de la entrega es exitoso.

Por la similitud existente entre los graficos obtenidos en los distintos equipos, omiti el implementarlos junto a mis resultados. 

## Entrega 6 mejorada Benjamín Greve

- Con 2 Particulas: tiempo total 10.7100000381 segundos.
![Dos particulas](https://user-images.githubusercontent.com/53497030/68216627-ece86380-ffbf-11e9-9833-2f9011dea036.PNG)

- Con 5 Particulas: tiempo total 22.5629999638 segundos.
![Cinco particulas](https://user-images.githubusercontent.com/53497030/68216628-ece86380-ffbf-11e9-909d-c9874416331d.PNG)

- Con 10 Particulas: tiempo total 44.6019999981 segundos.
![Dies particulas](https://user-images.githubusercontent.com/53497030/68216634-efe35400-ffbf-11e9-9efc-84ec594fe6fc.PNG)

- Con 20 Particulas: tiempo total 86.361000061 segundos.
![Veinte particulas](https://user-images.githubusercontent.com/53497030/68216637-efe35400-ffbf-11e9-946c-b76c1015d46e.PNG)

- Grafico N particulas vs Tiempo
![particulas vs tiempo](https://user-images.githubusercontent.com/53497030/68245290-7403fe80-fff5-11e9-9b45-b442473964d0.png)

## Entrega 6 mejorada Matías Real ##

- Con 2 Partículas: tiempo total 10.31 segundos.
![N_igual2](https://user-images.githubusercontent.com/53578787/68244824-6f8b1600-fff4-11e9-8d8c-1adfc01bc3fa.png)

- Con 5 Partículas: tiempo total 22.59 segundos.
![N_igual5](https://user-images.githubusercontent.com/53578787/68244837-76198d80-fff4-11e9-9e6d-33ffc9fb4c86.png)

- Con 10 partículas: tiempo total 41.70 segundos.
![N_igual10](https://user-images.githubusercontent.com/53578787/68244844-79147e00-fff4-11e9-8211-853ab9805dfd.png)

- Con 15 partículas: tiempo total 67.59 segundos.
![N_igual15](https://user-images.githubusercontent.com/53578787/68244855-7d409b80-fff4-11e9-8ad8-7138bb6cc0d1.png)

- Con 20 partículas: tiempo total 84.22 segundos. 
![N_igual20](https://user-images.githubusercontent.com/53578787/68244866-80d42280-fff4-11e9-8957-9030a8149856.png)

- Con 40 partículas: tiempo total 179.95 segundos.
![N_igual40](https://user-images.githubusercontent.com/53578787/68244873-85004000-fff4-11e9-9443-0eb8fbde84a1.png)

## Tiempo de simulación y Número de partículas 

![Grafico_Funcionamiento](https://user-images.githubusercontent.com/53578787/68246947-9ba89600-fff8-11e9-8f00-a3535ad653bd.png)


