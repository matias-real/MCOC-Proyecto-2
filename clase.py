#python 2.7
from matplotlib.pylab import *

#Unidades base SI
_m = 1.
_kg = 1.
_mm = 1e-3 *_m
_gr = 1e-3 * _kg
_s = 1.

#velocidades iniciales
vfx = 5.0*_m/_s #m/s 
vfy = 0.0*_m/_s #m/s 

x0 = array([0.,1.], dtype =double)
v0 = array([1.,1.], dtype =double)

#velocidad y posicion actual
xi =zeros(2, dtype=double)
vi =zeros(2, dtype=double)

#velocidad y posicion en el instante mas 1
xim1 =zeros(2, dtype=double)
vim1 =zeros(2, dtype=double)


Cd = 0.47 # particula esferica
g = 9.81 *_m/_s**2
d= 1*_mm
rho = 2700 * _kg/(_m**3)
m = rho *(4./3./8.)*pi*(d**3)   # masa de la particula

#Inicializar Euler en x0

dt= 0.1 #paso de tiempo
tmax = 20. # tiempo maximo de simulacion


ti = 0. #tiempo actual

W = array([0, -m*g])
vf =array([vfx,vfy])


Nt = int32(2*tmax /dt) 
x_store = zeros((2,Nt))
v_store = zeros((2,Nt))
t_store = zeros((Nt))

#Metodo de euler
i = 0
while ti < tmax:

	print "ti =",ti
	print "xi =",xi
	print "vi =",vi
	#evaluar velocidad relativa
	vrel = vf - vi
	norm_vrel = sqrt(dot(vrel,vrel)) #norma de vrel

	#evaluar fuerzas sobre la particula
	fD = 0.5*Cd*norm_vrel*vrel
	Fi = W +fD

	print "Fi =",Fi

	#evaluar aceleracion
	ai = Fi / m 

	#integrar
	xim1 = xi + vi*dt +ai*(dt*2/2)

	#avanzar en el tiempo
	
	x_store[:,i] = xi 
	v_store[:,i] = vi 
	t_store[i] = ti 
	ti += dt
	i +=1
	xi = xim1
	vi = vim1

#guardar ultimo paso
x_store[:,i] = xi 
v_store[:,i] = vi 
t_store[i] = ti 
	
print x_store

figure()
plot(x_store[0,:Nt],x_store[1,:Nt])
show()