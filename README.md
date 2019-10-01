# MCOC-Proyecto-2
## Descripción inicial del proyecto
La predicción del transporte de sedimentos está lejos de ser acertada porque no hay un profundo conocimiento sobre los procesos físicos que ocurren:
- Las predicciones sobre el transporte neto mediante simulaciones no son suficientes.
- Asumir que la velocidad de la partícula es igual a la velocidad del flujo no funciona con partículas que no son tan pequeñas (arenas, por ejemplo).
- Algunos procesos se descuidan (colisiones de partículas), turbulencia que se aumenta o disminuye, etc.
Una forma de predecir el transporte de sedimentos podría ser a través de una simulación numérica directa (resolver la ecuación de Navier-Stokes en cada cuadrícula de la celda) pero es muy caro y virtualmente imposible de hacer para miles o millones de partículas. Otra forma de predecir el transporte de sedimentos (la cual sería mejor opción) sería a modelar las fuerzas hidrodinámicas a partir de las grillas en que se conoce la velocidad. Esta forma es mucho más conveniente y es la que se tratará de modelar en este proyecto.

## Objetivos del proyecto
Implementar un modelo de simulacion numerico para transporte de sedimentos de fondo. Comprender aspectos de desempeño de aplicaciones de computación científica tales como IO y complejidad algorítmica.
