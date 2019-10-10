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

Una vez implementado el código para la simulación del movimiento de varias partículas cada uno de los integrantes creará un repositorio aparte, en el cual se subirá el código. En el README.md cada uno de los integantes mencionará las propiedades de su computador y correrá el código para un distinto número de partículas (todos deben hacerlo para las mismas cantidades), de manera de comparar el tiempo de funcionamiento del código en los distintos computadores.

## Links de los repositorios aparte de cada uno de los integrantes
- https://github.com/matias-real/MCOC-Proyecto-2-Entrega-4
