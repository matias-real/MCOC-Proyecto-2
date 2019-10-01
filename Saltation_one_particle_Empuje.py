#python 2.7
from matplotlib.pylab import *

#Unidades base SI
_m = 1.
_kg = 1.
_cm = 1e-2*_m
_mm = 1e-3 *_m
_gr = 1e-3 * _kg
_s = 1.

#velocidades iniciales
vfx = 5.0*_m/_s #m/s 
vfy = 0.0*_m/_s #m/s 

x0 = array([0.,1.*_mm], dtype =double) #en milimetros
v0 = array([1.,1.], dtype =double)

#velocidad y posicion actual
xi = x0 # =zeros(2, dtype=double)
vi = v0 #=zeros(2, dtype=double)

#velocidad y posicion en el instante mas 1
xim1 =zeros(2, dtype=double)
vim1 =zeros(2, dtype=double)


Cd = 0.47 # particula esferica
g = 9.81 *_m/_s**2
d= 1*_mm
rho_agua = 1000.*_kg/(_m**3) 
rho_particula = 2650. * _kg/(_m**3)

A = pi*(d/2)**2
V = (4./3.)*pi*(d/2)**3
m = rho_particula*V   # masa de la particula


dt= 1e-3*_s #paso de tiempo
tmax = 2.*_s # tiempo maximo de simulacion

ti = 0.*_s #tiempo actual

W = array([0, -m*g])
fB = array([0,rho_agua*V*g])

t=arange(0,tmax,dt)
Nt = len(t)

norm = lambda v: sqrt(dot(v,v))

k_penal = 1000*0.5*Cd*rho_agua*A*norm(v0)/(1*_mm)

def particula(z,t):
	xi = z[:2]
	vi = z[2:]
	vf = array([vfx, vfy])
	vrel = vf - vi
	fD = (0.5*Cd*rho_agua*norm(vrel)*A)*vrel
	#fL=3.0/4.0*alpha*Cd*()
	Fi = W + fD +fB

	if xi[1] < 0:
		Fi[1] += -k_penal*xi[1]

	zp = zeros(4)
	zp[:2] = vi

	
	zp[2:] = Fi/m
	return zp

from scipy.integrate import odeint
z0 = zeros(4)
z0[:2] = x0
z0[2:] = v0
z=odeint(particula,z0,t)
x = z[:,:2]
v = z[:,2:]

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