from matplotlib.pylab import *

datos = loadtxt("resultados.txt")


d = 0.15e-3

Nparticulas = (datos.shape[1]-1)/4
figure()

color = "006B93"
ax = gca()
colorlist = []
for i in range(Nparticulas):
	xi = datos[:,1]













show()