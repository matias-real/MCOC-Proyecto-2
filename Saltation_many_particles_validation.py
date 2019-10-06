#python 2.7
#particulas en ejes paralelos
from matplotlib.pylab import *
from scipy.integrate import odeint
import random

#Unidades base SI
_m = 1.
_kg = 1.
_cm = 1e-2*_m
_mm = 1e-3 *_m
_gr = 1e-3 * _kg
_s = 1.


def particula(z,t): 
	xi = z[:2]
	vi = z[2:]
	vf = array([vfx, vfy])
	vrel = vf - vi
	fD = (0.5*Cd*rho_agua*norm(vrel)*A)*vrel
	# fL=3.0/4.0*alpha*Cd*()
	Fi = W + fD +fB
	
	if xi[1] < 0: # Si la posicion de la particula es negativa significa que ya choco. Le aplico k_penal para que la particula suba (rebote)
		Fi[1] += -k_penal(v0)*xi[1]

	zp = zeros(4) #Crea arreglo de 4 ceros (zp =[0, 0, 0, 0])
	zp[:2] = vi # Iguala los ultimos 2 elementos de zp con los 2 elementos de vi (zp = [0, 0, vx, vy] )	
	zp[2:] = Fi/m # Iguala los 2 primeros elementos de zp a la aceleracion (zp = [ax, ay, vx, vy]) 
	return zp

N = 3 #numero de particulas

# Lista para guardar resultados
Resultados_x = [] 
Resultados_v = [] 
#velocidades iniciales del flujo
vfx = 5.0*_m/_s #m/s 
vfy = 0.0*_m/_s #m/s 

Cd = 0.47 # Particula esferica
g = 9.81 *_m/_s**2
d= 1*_mm  # Diametro de la particula
rho_agua = 1000.*_kg/(_m**3) 
rho_particula = 2650. * _kg/(_m**3)

A = pi*(d/2)**2 # Area de la particula
V = (4./3.)*pi*(d/2)**3 # Volumen de la particula
m = rho_particula*V   # Masa de la particula


dt= 1e-3*_s # Paso de tiempo
tmax = 2.*_s # tiempo maximo de simulacion

ti = 0.*_s #tiempo actual


#For para ver cada particula
for particle in range(N):

	vrand = random.random()
	xrand = random.random()
	x0 = array([0.,xrand*_mm], dtype =double) #en milimetros
	v0 = array([1.,vrand*2.*_m/_s], dtype =double)

	#velocidad y posicion actual
	xi = x0 # =zeros(2, dtype=double)
	vi = v0 #=zeros(2, dtype=double)

	#velocidad y posicion en el instante mas 1
	xim1 =zeros(2, dtype=double)
	vim1 =zeros(2, dtype=double)


	
	W = array([0, -m*g])   # Fuerza de gravedad
	fB = array([0,rho_agua*V*g]) # Fuerza buoyante

	t 	= arange(0,tmax,dt)  
	Nt = len(t)

	norm = lambda v: sqrt(dot(v,v))

	k_penal = lambda v: 1000*0.5*Cd*rho_agua*A*norm(v)/(1*_mm)    # El k_penal hace que la particula rebote cuando choca con el suelo
	
	z0 = zeros(4)
	z0[:2] = x0
	z0[2:] = v0
	z=odeint(particula,z0,t)
	Resultados_x.append(z[:,:2])
	Resultados_v.append(z[:,2:])

#grafico todo
figure()
for i in Resultados_x:	
	plot(i[:,0],i[:,1],label="vx = "+str(v0[0])+" vy = "+str(v0[1]))
	ylim(0,5*_mm) #limite del eje y	
plt.legend()
show()

'''
#Grafico de particula (trayectoria)
figure()
plot(x[:,0],x[:,1])
ylim(0,5*_mm) #limite del eje y


figure()
subplot(2,1,1)
plot(t,x[:,0],label="x")
plot(t,x[:,1],label="y")
plt.legend()
subplot(2,1,2)
plot(t,v[:,0],label="vx")
plot(t,v[:,1],label="vy")
plt.legend()
show()
'''